from setuptools import setup
from glob import glob
import os

package_name = 'tb3_rfid'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
	(os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='adev',
    maintainer_email='developer.lorenz@yahoo.com',
    description='Package handles publishing Data read with RFID using RC522 as well as subscribing to that data',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "rfid_publisher = tb3_rfid.publish_taginfo_node:main",
            "rfid_subscriber = tb3_rfid.taginfo_subscriber:main" ,
        ],
    },
)
