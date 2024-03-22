#include <memory>
#include <rclcpp/rclcpp.hpp>
#include <moveit/move_group_interface/move_group_interface.h>

int main(int argc, char * argv[])
{
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

    // Load the home position
    move_group_interface.setNamedTarget("home");

    // Plan to reach the home position
    moveit::planning_interface::MoveGroupInterface::Plan plan;
    bool success = (move_group_interface.plan(plan) == moveit::core::MoveItErrorCode::SUCCESS);


    // Execute the plan
    if(success) {
        move_group_interface.execute(plan);
        RCLCPP_INFO(logger, "Robot moved to home position.");
    } else {
        RCLCPP_ERROR(logger, "Failed to plan to home position.");
    }

    // Shutdown ROS
    rclcpp::shutdown();
    return 0;
}
