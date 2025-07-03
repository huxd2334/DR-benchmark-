import os
from setuptools import find_packages, setup

setup(
    name="bdlb",
    version="0.0.2",
    description="BDL Benchmarks",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
        "pandas",
        "matplotlib",
        "seaborn",
        "scikit-learn",
        "kaggle",
        "opencv-python",
        "tensorflow",
        "tensorflow-probability",
        "tensorflow-datasets",
    ],
    python_requires=">=3.7",
)