from setuptools import find_packages, setup

setup(
    name='retail_ml_pipeline',
    version='0.0.1',
    author='Phylis Oji',
    author_email='Phylisoji@gmail.com',
    packages=find_packages(include=['src','src.*']),
    python_requires='>=3.8',
    install_requires=['pandas',
                      'numpy',
                      'matplotlib',
                      'seaborn'],
    description="The design of a Machine Learning Pipeline for a retail Company"
)