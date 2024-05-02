import sys
import rclpy
from rclpy.node import Node

from geometry_msgs.msg import PoseWithCovarianceStamped, PointStamped

# This node set the initial location of the robot by subscribe to the /clicked_point topic and publish to /initialpose

class initial_pose_node(Node):

    def __init__(self):
        super().__init__('initial_pose_pub_node')
        self.clicked_point_sub = self.create_subscription(PointStamped, '/clicked_point', self.clicked_point_callback, 1)
        self.clicked_point_sub # prevent unused variable warning
        
        self.coor_publisher = self.create_publisher(PoseWithCovarianceStamped, 'initialpose', 1)

    def clicck_point_callback(self, msg):
        self.get_logger().info(f'Received Data:\n X: {msg.point.x} \n Y: {msg.point.y} \n Z: {msg.point.z}')
        self.coor_publish(msg.point.x, msg.point.y)

    def coor_publish(self, x, y):
        msg = PoseWithCovarianceStamped()
        msg.header.frame_id = '/map'
        msg.pose.pose.position.x = x
        msg.pose.pose.position.y = y
        self.get_logger().info(f'Publishing Initial Position \n X = {msg.pose.pose.position.x} \n Y = {msg.pose.pose.position.y}')
        self.coor_publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    publisher = initial_pose_node()
    rclpy.spin(publisher)
    publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()