from setuptools import find_packages, setup

package_name = 'draw_spiral'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hygor',
    maintainer_email='hygor.c.luz@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "counter_node = draw_spiral.counter_node:main",
            "draw_spiral = draw_spiral.draw_spiral:main"
        ],
    },
)
