import setuptools
from distutils.core import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="srmpy",
    version="0.1.0",
    author="Shailesh Mishra",
    author_email="mshaileshr@gmail.com",
    description="A package for mathematical calculations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ishaileshmishra/srmpy.git",
    packages=setuptools.find_packages(),
    setup_requires=['wheel'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires='>=3.6',
)
