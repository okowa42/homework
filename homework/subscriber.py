# SPDX-FileCopyrightText: 2025 AkariHirohara <a.hirohara.0526@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class BitcoinSubscriber(Node):
    def __init__(self):
        super().__init__("bitcoin_price_subscriber")
        self.create_subscription(String,"bitcoin_price",self.subscriber_callback,10)

    def subscriber_callback(self,msg):
        self.get_logger().info(f"{msg.data}")

def main():
    rclpy.init()
    node = BitcoinSubscriber()
    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()
