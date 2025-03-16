from setuptools import setup

package_name = 'lidar_intensity_listener'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools', 'rclpy', 'sensor_msgs', 'matplotlib', 'pandas'],
    zip_safe=True,
    author='Your Name',
    author_email='your_email@example.com',
    maintainer='Your Name',
    maintainer_email='your_email@example.com',
    description='ROS2 package to subscribe to /scan and save intensity data.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'lidar_intensity_listener = lidar_intensity_listener.listener:main'
        ],
    },
)
