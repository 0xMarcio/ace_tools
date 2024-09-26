from setuptools import setup, find_packages

setup(
    name="acetools",
    version="1.0.0",
    description="A collection of handy tools for data handling, visualization, and reporting.",
    author="0xMarc",
    author_email="marc@codepwn.win",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.2.3",
        "numpy>=2.1.1",
        "matplotlib>=3.9.2",
        "plotly>=5.24.1",
        "scikit-learn>=1.5.2",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
)
