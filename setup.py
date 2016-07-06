# -*- encoding: utf-8 -*-
from __future__ import absolute_import

from setuptools import find_packages, setup

import banana


version = banana.__version__

entry_points = {
    'console_scripts': [
        'banana = banana.commands.manage:execute_from_command_line',
    ],
}

install_requires = [
    'pluggy>=0.1.0,<1.0',
]
test_extras = [
    'pytest',
    'pytest-cov'
]

setup(
    name='Banana',
    version=version,
    url='https://github.com/banana-framework/banana-framework',
    author='Sergey Tsaplin',
    author_email='me@sergeytsaplin.com',
    description=('A high-level Python framework for microservices '
                 'development'),
    license='BSD',
    extras_require={
        'tests': test_extras,
    },
    install_requires=install_requires,
    packages=find_packages(),
    entry_points=entry_points,
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Framework :: banana',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
