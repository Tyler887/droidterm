from distutils.core import setup

from setuptools import find_packages

setup(

    name='Droidterm',

    version='0.1',

    description='Droidterm',

    author='Tyler887',

    author_email="tylermageeshields@gmail.com",

    packages=find_packages(),


    package_data={'droidterm': ['main.py']}

)
