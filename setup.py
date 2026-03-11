#!/usr/bin/env python3
"""
Setup script for wedgebox-hpc
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name='wedgebox-hpc',
    version='1.0.0',
    author='WedgeBox Team',
    author_email='wedgebox.team@gmail.com',
    description='GPU Performance Monitor for HPC Clusters',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/wedgebox/wedgebox-hpc',
    project_urls={
        'Bug Tracker': 'https://github.com/wedgebox/wedgebox-hpc/issues',
        'Documentation': 'https://github.com/wedgebox/wedgebox-hpc',
        'Source Code': 'https://github.com/wedgebox/wedgebox-hpc',
    },
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: System :: Monitoring',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: POSIX :: Linux',
        'Environment :: Console',
    ],
    python_requires='>=3.8',
    install_requires=[
        'psutil>=5.8.0',
    ],
    entry_points={
        'console_scripts': [
            'wedgebox-hpc=wedgebox_hpc.cli:main',
        ],
    },
    keywords='gpu monitoring hpc machine-learning performance nvidia amd',
    license='MIT',
)