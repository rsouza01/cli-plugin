# -*- coding: utf-8 -*-
# from setuptools import setup, find_packages
import setuptools


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setuptools.setup(
    name='cli-plugin',
    packages=['cli-plugin'],
    version='0.2.3',
    description='CLI tool with plugin support - TEMPLATE PROJECT',
    # long_description=readme,
    # long_description_content_type="text/markdown",
    author='Rodrigo de Souza',
    author_email='rsouza01@gmail.com',
    url='https://github.com/rsouza01/cli-plugin',
    download_url='https://github.com/rsouza01/cli-plugin/archive/v_0.1.1.tar.gz',
    license=license,
    install_requires=[],    
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
