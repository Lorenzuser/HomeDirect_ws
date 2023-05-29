from setuptools import setup

package_name = 'nav_main'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dev',
    maintainer_email='dev@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # 'controller_main = nav_main.controller_main:main',
            'commander = nav_main.commander:main',
            'service = nav_main.controller_main:main',
            'client = nav_main.example_client:main',
            'room_save = nav_main.room_saver:main',            

        ],
    },
)
