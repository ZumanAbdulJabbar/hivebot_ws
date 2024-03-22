#include <memory>
#include <rclcpp/rclcpp.hpp>
#include <moveit/move_group_interface/move_group_interface.h>

// Define a structure to store joint positions
struct JointPosition {
  double shoulder_pan_joint;
  double shoulder_lift_joint;
  double elbow_joint;
  double wrist_1_joint;
  double wrist_2_joint;
  double wrist_3_joint;
  double ee_fixed_joint;
};

int main(int argc, char * argv[]) {
  // Initialize ROS and create the Node
  rclcpp::init(argc, argv);
  auto const node = std::make_shared<rclcpp::Node>(
      "hello_moveit",
      rclcpp::NodeOptions().automatically_declare_parameters_from_overrides(true)
  );

  // Create a ROS logger
  auto const logger = rclcpp::get_logger("hello_moveit");

  // Create the MoveIt MoveGroup Interface
  using moveit::planning_interface::MoveGroupInterface;
  auto move_group_interface = MoveGroupInterface(node, "arm");

  // Define the four joint configurations (replace with your actual values)
  JointPosition points[4] = {
    {1.5000, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0},
    {1.5000, -0.4513, 1.900, 0.0, 0.0, 0.0, 0.0},
    {0.7200, -0.4513, 1.900, 0.0, 0.0, 0.0, 0.0},
    {1.0760, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0}
  };

  // Loop through each point and plan & execute the motion
  for (int i = 0; i < 4; ++i) {
    moveit::planning_interface::MoveGroupInterface::Plan plan;

    // Set the joint target for the current point
    move_group_interface.setJointValueTarget({
      points[i].shoulder_pan_joint,
      points[i].shoulder_lift_joint,
      points[i].elbow_joint,
      points[i].wrist_1_joint,
      points[i].wrist_2_joint,
      points[i].wrist_3_joint,
      points[i].ee_fixed_joint
    });

    // Plan the motion
    bool success = (move_group_interface.plan(plan) == moveit::core::MoveItErrorCode::SUCCESS);

    // Execute the plan (check success and handle errors as needed)
    if (success) {
      move_group_interface.execute(plan);
      RCLCPP_INFO(logger, "Robot moved to point %d.", i + 1);
    } else {
      RCLCPP_ERROR(logger, "Failed to plan to point %d.", i + 1);
      // Add error handling here (e.g., retry planning or exit)
    }
  }

  // Shutdown ROS
  rclcpp::shutdown();
  return 0;
}
