import os

from setuptools import setup, find_packages

current_dir = os.path.dirname(os.path.realpath(__file__))
requirementPath = current_dir + '/requirements.txt'
install_requires = []
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

setup(
    name='rs-tools',
    version='0.1',
    packages=find_packages(),
    install_requires=install_requires
)
