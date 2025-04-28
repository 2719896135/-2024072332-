import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class NodeA(Node):
    def __init__(self):
        super().__init__('node_a')
        self.publisher_ = self.create_publisher(String, 'hello_topic', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)  # 每秒调用一次
        self.get_logger().info("NodeA is running...")

    def timer_callback(self):
        msg = String()
        msg.data = "Hello, ROS2!"
        self.publisher_.publish(msg)
        self.get_logger().info('Published: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node_a = NodeA()
    rclpy.spin(node_a)
    node_a.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
