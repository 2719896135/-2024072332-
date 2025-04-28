import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class NodeB(Node):
    def __init__(self):
        super().__init__('node_b')
        self.subscription = self.create_subscription(
            String,
            'hello_topic',
            self.listener_callback,
            10)
        self.subscription  # 防止未使用的变量警告
        self.get_logger().info("NodeB is running...")

    def listener_callback(self, msg):
        self.get_logger().info('Received: "%s"' % msg.data)
        self.get_logger().info("学号：2024072332 姓名：张殷瑞")

def main(args=None):
    rclpy.init(args=args)
    node_b = NodeB()
    rclpy.spin(node_b)
    node_b.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
