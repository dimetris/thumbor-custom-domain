#!/usr/bin/env python
from setuptools import setup


setup(name='thumbor-custom-domain',
      version='0.0.1',
      description='Custom domain loader',
      packages=['custom_domain_loader'],
      install_requires=[
            "tornado>=4.1.0,<5.0.0",
            "thumbor>=6.1.5,<7"
      ],
      url='https://github.com/dimetris/thumbor-custom-domain',
      license='MIT',
      classifiers=['Intended Audience :: Developers',
                   'Topic :: Software Development :: Libraries',
                   'Development Status :: 3 - Alpha',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.3'])