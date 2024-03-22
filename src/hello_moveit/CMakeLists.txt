cmake_minimum_required(VERSION 3.8)
project(hello_moveit)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(moveit_ros_planning_interface REQUIRED)
find_package(rclcpp REQUIRED)

add_executable(home src/home.cpp)
target_include_directories(home PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)
target_compile_features(home PUBLIC c_std_99 cxx_std_17)  # Require C99 and C++17
ament_target_dependencies(
  home
  "moveit_ros_planning_interface"
  "rclcpp"
)

# Add executable for clean_toilet.cpp
add_executable(clean_toilet_node src/clean_toilet.cpp)  
target_include_directories(clean_toilet_node PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)
target_compile_features(clean_toilet_node PUBLIC c_std_99 cxx_std_17)  # Require C99 and C++17
ament_target_dependencies(
  clean_toilet_node
  "moveit_ros_planning_interface"
  "rclcpp"
)

# Add executable for clean_toilet.cpp
add_executable(clean_western_node src/clean_western.cpp)  
target_include_directories(clean_western_node PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)
target_compile_features(clean_western_node PUBLIC c_std_99 cxx_std_17)  # Require C99 and C++17
ament_target_dependencies(
  clean_western_node
  "moveit_ros_planning_interface"
  "rclcpp"
)
# Add executable for gripper.cpp
add_executable(gripper src/gripper.cpp)  
target_include_directories(gripper PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)
target_compile_features(gripper PUBLIC c_std_99 cxx_std_17)  # Require C99 and C++17
ament_target_dependencies(
  gripper
  "moveit_ros_planning_interface"
  "rclcpp"
)

# Add executable for pick_sprayer.cpp 
add_executable(pick_sprayer src/pick_sprayer.cpp)  # Renamed to clean_toilet_node
target_include_directories(pick_sprayer PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)
target_compile_features(pick_sprayer PUBLIC c_std_99 cxx_std_17)  # Require C99 and C++17
ament_target_dependencies(
  pick_sprayer
  "moveit_ros_planning_interface"
  "rclcpp"
)

install(TARGETS
  home
  clean_toilet_node 
  clean_western_node
  gripper
  pick_sprayer 
  DESTINATION lib/${PROJECT_NAME})

  # Install launch files
install(DIRECTORY launch/
DESTINATION share/${PROJECT_NAME}/launch)

install(DIRECTORY config/
DESTINATION share/${PROJECT_NAME}/config)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
