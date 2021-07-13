# coding:utf-8

from setuptools import setup, find_packages
from byteplus_sdk import VERSION

setup(
    name="byteplus-sdk",
    version=VERSION,
    keywords=("pip", "byteplus", "byteplus-sdk-python"),
    description="The BytePlus SDK for Python",
    license="MIT Licence",

    url="https://github.com/byteplus-sdk/byteplus-sdk-python",
    author="BytePlus SDK",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["requests", "pytz", "pycryptodome", "protobuf", "google", "six"]
)
