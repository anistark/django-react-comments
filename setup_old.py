"""
See:
https://github.com/anistark/django-react-comments
"""

from setuptools import setup, find_packages
# from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='django-react-comments',

    version='0.0.4',

    description='Django comment module using in reactJS',
    long_description='Django comment module using in reactJS. Currently only stores to db and uses a dummy user and post.',

    url='https://github.com/anistark/django-react-comments',

    author='Kumar Anirudha<anirudhastark@yahoo.com>, Puja Singh<singhpuja0708@gmail.com>',
    author_email='anirudhastark@yahoo.com, singhpuja0708@gmail.com',

    license='MIT',

    classifiers=[
        'Framework :: Django',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='django comment module djangothon anistark puja0708 reactJS',

    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    install_requires=[],

    extras_require={},

    package_data={},

    data_files=[],

    entry_points={},
)
