#include <memory>
#include <rclcpp/rclcpp.hpp>
#include <moveit/move_group_interface/move_group_interface.h>

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

  // Define the target joint configuration
  std::vector<double> target_joint_positions = {-0.8678, -1.2844, 2.1175, 0.0, 0.0, 0.0, 0.0};

  // Set the joint target
  move_group_interface.setJointValueTarget(target_joint_positions);

  // Plan the motion
  moveit::planning_interface::MoveGroupInterface::Plan plan;
  bool success = (move_group_interface.plan(plan) == moveit::core::MoveItErrorCode::SUCCESS);

  // Execute the plan (check success and handle errors as needed)
  if (success) {
    move_group_interface.execute(plan);
    RCLCPP_INFO(logger, "Robot moved to target position.");
  } else {
    RCLCPP_ERROR(logger, "Failed to plan to target position.");
    // Add error handling here (e.g., retry planning or exit)
  }

  // Shutdown ROS
  rclcpp::shutdown();
  return 0;
}
