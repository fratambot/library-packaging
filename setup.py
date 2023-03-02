import os

from dotenv import load_dotenv
from setuptools import setup

load_dotenv()

setup(
    name=os.environ.get("NAME"),
    version=os.environ.get("VERSION"),
    author="Francesco Tamborra",
    author_email="francescotamborra@gmail.com",
    description="A python library wrapping several open-source QRS algorithm",
    long_description=open('README.md').read(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/fratambot/library-packaging",
    license="MIT",
    package_dir={"":"src"},
    python_requires='>=3.9',
    tests_require=["pytest"],
)