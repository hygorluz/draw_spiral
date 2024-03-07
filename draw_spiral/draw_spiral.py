#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist 
from turtlesim.msg import Pose
import math

class DrawSpiralNode(Node):

    def __init__(self):
        super().__init__("draw_spiral")
        self.get_logger().info("Draw spiral node has started.")
        self.linear_x = 1.0
        self.angular_z = math.pi
        self.cmd_vel_pub = self.create_publisher(msg_type=Twist, topic="/turtle1/cmd_vel", qos_profile=10)
        self.pose_sub = self.create_subscription(msg_type=Pose, topic="/turtle1/pose", callback=self.get_pose, qos_profile=10)
        self.create_timer(timer_period_sec=1,callback=self.send_vel)
        
    def send_vel(self):
        vel: Twist = Twist()
        vel.linear.x = self.linear_x
        vel.angular.z = self.angular_z
        self.cmd_vel_pub.publish(msg=vel)
        self.linear_x += 0.2

    def get_pose(self, pose_msg = Pose()):
        self.pose_x = pose_msg.x
        self.pose_y = pose_msg.y
        self.pose_theta = pose_msg.theta

        if round(self.pose_y) == 10:
            self.get_logger().warn(f"The turtle is about the reach the wall. Position at x:{self.pose_x} y:{self.pose_y}")
        else:
            self.get_logger().info(f"The turtle position at x:{self.pose_x} y:{self.pose_y} theta: {pose_msg.theta}")
        
        


def main(args=None):
    rclpy.init(args=args)
    drawNode: DrawSpiralNode = DrawSpiralNode()
    rclpy.spin(drawNode)
    rclpy.shutdown()