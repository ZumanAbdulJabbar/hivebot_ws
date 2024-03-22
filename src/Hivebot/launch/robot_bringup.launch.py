import launch
from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['ros2', 'launch', 'hivebot', 'launch_sim.launch.py', 'world:=./src/Hivebot/worlds/toilet2.world'],
            output='screen'
        ),
        ExecuteProcess(
            cmd=['ros2', 'launch', 'hivebot', 'online_async_launch.py', 'map:=toilet_save.yaml'],
            output='screen'
        ),
        ExecuteProcess(
            cmd=['ros2', 'launch', 'hivebot', 'navigation_launch.py'],
            output='screen'
        ),
        ExecuteProcess(
            cmd=['ros2', 'launch', 'hivebot', 'localization_launch.py', 'map:=toilet_save.yaml'],
            output='screen'
        ),
        ExecuteProcess(
            cmd=['rviz2'],
            output='screen'
        )
        # ExecuteProcess(
        #     cmd=['ros2', 'launch', 'ur_moveit_config', 'demo.launch.py'],
        #     output='screen'
        # ),

        # ExecuteProcess(
        #     cmd=['ros2', 'launch', 'yolobot_recognition', 'launch_yolov8.launch.py'],
        #     output='screen'
        # )
        
    ])
