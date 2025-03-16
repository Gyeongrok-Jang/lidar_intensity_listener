from setuptools import setup

package_name = 'lidar_intensity_listener'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools', 'rclpy', 'sensor_msgs', 'matplotlib', 'pandas'],
    zip_safe=True,
    author='Gyeongrok-Jang',
    author_email='jjkr4966@pukyong.ac.kr',
    maintainer='Gyeongrok-Jang',
    maintainer_email='jjkr4966@pukyong.ac.kr',
    description='ROS2 package to subscribe to /scan and save intensity data.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'lidar_intensity_listener = lidar_intensity_listener.listener:main'
        ],
    },
)
