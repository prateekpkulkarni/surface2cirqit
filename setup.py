from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="surface2cirqit",
    version="0.1.0",
    author="Prateek P Kulkarni",
    author_email="pkulkarni2425@gmail.com",
    description="A package to generate quantum circuits for Surface Codes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prateekpkulkarni/surface2cirqit",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy",
        "qiskit",
    ],
)