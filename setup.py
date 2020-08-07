with open("README.md", "r") as fh:
    long_description = fh.read()


from setuptools import setup, find_packages

setup(
    name='lcd-controller2',
    version='',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='',
    license='',
    author='Lukas Brennauer, Samuel Kroiss',
    author_email='',
    description=long_description,
    install_requires=[
        'setuptools',
    ],
)
