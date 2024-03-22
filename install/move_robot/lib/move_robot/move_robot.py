import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from moveit_msgs.msg import MoveItErrorCodes
from moveit_msgs.srv import GetPositionIK
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

class MoveArm(Node):
    def __init__(self):
        super().__init__('move_arm')
        self.ik_client = self.create_client(GetPositionIK, 'compute_ik')
        while not self.ik_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Service "compute_ik" not available, waiting...')

    def move_to_home_position(self):
        request = GetPositionIK.Request()
        request.group_name = 'arm'
        request.ik_request.avoid_collisions = True
        request.ik_request.attempts = 10
        request.ik_request.pose_stamped.header.frame_id = 'base_link'  # Adjust frame_id if necessary

        # Set the home position
        home_pose = PoseStamped()
        home_pose.pose.position.x = 90.0  # Adjust as needed
        home_pose.pose.position.y = 90.0  # Adjust as needed
        home_pose.pose.position.z = 0.0  # Adjust as needed
        home_pose.pose.orientation.x = 0.0
        home_pose.pose.orientation.y = 0.0
        home_pose.pose.orientation.z = 0.0
        home_pose.pose.orientation.w = 1.0
        request.ik_request.pose_stamped = home_pose

        future = self.ik_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result() is not None:
            if future.result().error_code.val == MoveItErrorCodes.SUCCESS:
                joint_trajectory = future.result().solution.joint_state
                self.execute_trajectory(joint_trajectory)
            else:
                self.get_logger().error('IK failed with error code: %d', future.result().error_code.val)
        else:
            self.get_logger().error('Service call failed')

    def execute_trajectory(self, joint_trajectory):
        joint_names = ['shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 
                       'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint', 'ee_fixed_joint']

        trajectory_msg = JointTrajectory()
        trajectory_msg.joint_names = joint_names

        point = JointTrajectoryPoint()
        point.positions = joint_trajectory.position
        point.time_from_start.sec = 1  # Adjust as needed
        trajectory_msg.points.append(point)

        # Publish trajectory to MoveIt for execution
        self.get_logger().info('Executing trajectory to home position...')
        self.publisher = self.create_publisher(JointTrajectory, 'execute_trajectory', 10)
        self.publisher.publish(trajectory_msg)

def main(args=None):
    rclpy.init(args=args)
    move_arm = MoveArm()
    move_arm.move_to_home_position()
    rclpy.spin(move_arm)
    move_arm.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
