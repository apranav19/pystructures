from setuptools import setup, find_packages

setup(name='pystructures',
      version='0.0.1',
      description='Data Structures made simple',
      url='http://github.com/apranav19/pystructures',
      author='Pranav Angara',
      author_email='apranav19@gmail.com',
      license='MIT',
      packages=find_packages(exclude=['tests*']),
      zip_safe=False)
