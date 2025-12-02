from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sudoku-engine",
    version="0.1.0",
    description="A Python implementation of a Sudoku solver using a backtracking algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Kai-353",
    url="https://github.com/kai-353/sudoku-solver-engine-python",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
