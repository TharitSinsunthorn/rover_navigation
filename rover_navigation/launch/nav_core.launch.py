import os

from ament_index_python.packages import get_package_share_directory

from launch_ros.actions import Node
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.event_handlers import OnProcessExit
from launch.launch_description_sources import PythonLaunchDescriptionSource

# this is the function launch  system will look for


def generate_launch_description():
    
    use_sim_time = LaunchConfiguration('use_sim_time')
    
    twist_mux_params = os.path.join(get_package_share_directory('rover_navigation'), 'config', 'twist_mux.yaml')
    
    twist_mux = Node(
        package='twist_mux',
        executable='twist_mux',
        parameters=[twist_mux_params],
        remappings=[('/cmd_vel_out', '/diff_cont/cmd_vel_unstamped')]
    )



    # create and return launch description object
    return LaunchDescription(
        [
            twist_mux,
        ]
    )