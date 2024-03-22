from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import TimerAction

def generate_launch_description():

  # Define nodes
  home_node1 = Node(
      package='hello_moveit',
      executable='home',
      name='home',
      output='screen'
  )

  pick_sprayer_node1 = Node(
      package='hello_moveit',
      executable='pick_sprayer',
      name='pick_sprayer',
      output='screen'
  )



  clean_western_node = Node(
      package='hello_moveit',
      executable='clean_western_node',
      name='clean_western_node',
      output='screen'
  )

  pick_sprayer_node2 = Node(
      package='hello_moveit',
      executable='pick_sprayer',
      name='pick_sprayer',
      output='screen'
  )

  home_node2 = Node(
      package='hello_moveit',
      executable='home',
      name='home',
      output='screen'
  )

  # Define delay in seconds
  timer_period1 = 5.0
  timer_period2 = 8.0
  timer_period3 = 22.0
  timer_period4 = 50.0
  timer_period5 = 10.0

  # Launch the nodes with delays using TimerAction
  return LaunchDescription([
      home_node1,

      TimerAction(
          period=timer_period2,
          actions=[pick_sprayer_node1]
      ),

      TimerAction(
          period=timer_period3,
          actions=[clean_western_node]
      ),

      TimerAction(
          period=timer_period4,
          actions=[pick_sprayer_node2]
      ),

      TimerAction(
          period=timer_period5,
          actions=[home_node2]
      ),
  ])
