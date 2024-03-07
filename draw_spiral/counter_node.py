#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


class MyNode(Node):

    def __init__(self):
        super().__init__("counter_node")
        self.get_logger().info("ROS2 Node started")        
        self.counter = 0
        self.create_timer(callback=self.timer_callback,timer_period_sec=1)

    def timer_callback(self):
        self.get_logger().info(f"Triggered {self.counter} times")
        self.counter += 1


def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()