from setuptools import setup

setup(
    name='Shapes',
    version='0.1.0',
    description='A utility for working with shapes',
    author='Damien Irving',
    author_email='irving.damien@gmail.com',
    license='MIT',
    zip_safe=False,
    packages=['shapes'],
    scripts=['bin/shapes'],
    tests_require=['pytest', 'pytest-cov'],
    setup_requires=['pytest-runner'],
    )
    

# packages is the directory where it lives (path relative to setup.py location)