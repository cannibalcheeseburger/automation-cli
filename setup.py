import setuptools
from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()
with open('requirements.txt', 'r') as f:
    requirements = [line.strip() for line in f.readlines()]

setup(
    name='automate',
    version='1.0'
    description='automation cli',
    author='Kashish srivastava',
    url="https://github.com/cannibalcheeseburger/automation-cli",
    packages=find_packages(), 
    include_package_data=True,
    install_requires=requirements,

    entry_points='''
        [console_scripts]
        automate=automate:cli
        ''' ,

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7.6',
    ],
    license='MIT License',
)