import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class PySubscriber(Node):
    def __init__(self):
        super().__init__('py_sub_node')
        # Đăng ký nhận dữ liệu từ topic "number_topic"
        self.subscription = self.create_subscription(
            Int32,
            'number_topic',
            self.listener_callback,
            10)
        self.get_logger().info('Python Subscriber đã sẵn sàng nhận lệnh!')

    def listener_callback(self, msg):
        self.get_logger().info(f'Python nhận được: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = PySubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()