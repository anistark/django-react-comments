"""
See:
https://github.com/anistark/django-react-comments/tree/puja
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='django-react-comments',

    version='0.0.1',

    description='a django project with the comment system implemented in reactJS',

    url='https://github.com/anistark/django-react-comments/tree/puja',

    author=' ',
    author_email=' ',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        'License :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='django commenting system in reactJS',

    
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    
    install_requires=[ ],

    
    extras_require={
        
    },

    
    package_data={
        
    },

    
    data_files=[ ],

    
    entry_points={
        
    },
)
