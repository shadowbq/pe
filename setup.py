
import sys
from os.path import abspath, dirname, join, realpath
from setuptools import setup, find_packages


setup(
    name='pe',
    version='0.1.2',
    description='Yet-Another-PE-Tool',
    url='https://github.com/shadowbq/pecli',
    author='Shadowbq',
    author_email='shadowbq@gmail.com',
    keywords='malware',
    include_package_data=True,
    install_requires=['pefile', 'yara-python','ssdeep-windows','python-magic-bin'],
    license='MIT',
    python_requires='>=3.5',
    packages=find_packages(exclude=["*.tests", "*.test", "tests", "test"]),
    package_dir={'pe.lib': 'pe/lib'},
    package_data={'pe': ['pe/data/*.yara']},
    scripts=['pecli.py'],

)
