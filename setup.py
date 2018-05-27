
import sys
from os.path import abspath, dirname, join, realpath
from setuptools import setup, find_packages


setup(
    name='pe',
    version='0.1.1',
    description='Another PE info tool',
    url='https://github.com/Te-k/pe',
    author='Tek',
    author_email='tek@randhome.io',
    keywords='malware',
    include_package_data=True,
    install_requires=['pefile', 'yara-python'],
    license='MIT',
    python_requires='>=3.5',
    packages=find_packages(exclude=["*.tests", "*.test", "tests", "test"]),
    package_dir={'pe.lib': 'pe/lib'},
    package_data={'pe': ['pe/data/*.yara']},
    scripts=['pecli.py'],

)
