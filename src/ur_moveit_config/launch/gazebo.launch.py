import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node



def generate_launch_description():


    

    package_name='ur_moveit_config' 

    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','rsp.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
             )

   
    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'my_bot'],
                        output='screen')

    joint_state_publisher = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output='screen'
    )

    spawn_controllers = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','spawn_controllers.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    moveit_rviz = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','moveit_rviz.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    move_group = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','move_group.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    static_virtual_joint_tfs = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','static_virtual_joint_tfs.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )
  
    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity,
        joint_state_publisher,
        spawn_controllers,
        moveit_rviz,
        move_group,
        static_virtual_joint_tfs,
    ])
