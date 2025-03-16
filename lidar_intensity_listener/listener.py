import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import pandas as pd
import matplotlib.pyplot as plt
import time
from rclpy.qos import QoSProfile, ReliabilityPolicy, DurabilityPolicy

class LidarIntensityListener(Node):
    def __init__(self):
        super().__init__('lidar_intensity_listener')

        qos_profile = QoSProfile(
            depth=10, 
            reliability=ReliabilityPolicy.RELIABLE,  
            durability=DurabilityPolicy.TRANSIENT_LOCAL  
        )

        self.subscription = self.create_subscription(
            LaserScan,
            'scan',  
            self.listener_callback,
            qos_profile  
        )

        self.data = [] 
        self.start_time = time.time() 
        self.duration = 10  

    def listener_callback(self, msg):
        if time.time() - self.start_time < self.duration:  

            intensity = msg.intensities[0]  
            current_time = time.time() - self.start_time  

            self.data.append({'time': current_time, 'intensity': intensity})

    def save_and_plot_data(self):
        if not self.data:
            self.get_logger().info('No data collected.')
            return


        df = pd.DataFrame(self.data)


        df.to_csv('/home/imsl/ros2_ws/src/lidar_intensity_listener/data/lidar_intensity_data.csv', index=False)
        self.get_logger().info('Data saved to /home/imsl/ros2_ws/src/lidar_intensity_listener/data/lidar_intensity_data.csv')


        plt.plot(df['time'], df['intensity'], label='Lidar Intensity')

        mean_intensity = df['intensity'].mean()

        plt.axhline(y=mean_intensity, color='r', linestyle='--', label=f'Mean Intensity ({mean_intensity:.2f})')

        plt.xlabel('Time (seconds)')
        plt.ylabel('Intensity')
        plt.title('LiDAR Intensity over Time')
        plt.legend()
        plt.grid(True)

        plt.savefig('/home/imsl/ros2_ws/src/lidar_intensity_listener/data/lidar_intensity_plot.png')
        self.get_logger().info('Graph saved to /home/imsl/ros2_ws/src/lidar_intensity_listener/data/lidar_intensity_plot.png')

def main(args=None):
    rclpy.init(args=args)
    node = LidarIntensityListener()
    
    # 10초 동안 spin 반복
    while time.time() - node.start_time < node.duration:
        rclpy.spin_once(node)
    
    node.save_and_plot_data()

    rclpy.shutdown()

if __name__ == '__main__':
    main()
