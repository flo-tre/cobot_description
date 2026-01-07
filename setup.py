from setuptools import find_packages, setup

package_name = 'cobot_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/urdf', [
            'urdf/camera.xacro',
            'urdf/cobot_camera.urdf.xacro',
            'urdf/cobot_macro.xacro',
            'urdf/cobot.ros2_control.xacro',
        ]),
        ('share/' + package_name + '/meshes/sensors/camera', [
            'meshes/sensors/camera/kinetic.dae',
            'meshes/sensors/camera/kinetic.stl',
            'meshes/sensors/camera/xtion_pro_live.png',
        ]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='florian.tretter13@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
        ],
    },
)
