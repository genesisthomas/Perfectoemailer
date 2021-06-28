#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: genesisthomas
"""

import sys

from setuptools import find_packages, setup

OPTIONS = {}
mainscript = 'perfecto/perfectoai.py'
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
     name='perfectoai',
    #   version='1.0.31', #testpypi
      version='1.0.31',
     author="Genesis Thomas",
     author_email="gthomas@perforce.com",
     description="perfectoAI is an automated emailable reporter along with AI graphs & predictions",
     long_description=long_description,
     long_description_content_type="text/markdown",
     license='GPLv3',
     keywords = ['Perfecto', 'appium', 'selenium', 'testing', 'api', 'automation'],
     url="https://github.com/genesisthomas/PerfectoAI.git",
     install_requires=[
            'json2html','jenkinsapi','requests','configparser','termcolor','numpy','cython','pandas==1.2.4','retrying','ephem','pymeeus','easydict', 'psutil', 'korean-lunar-calendar','MarkupSafe','jinja2','matplotlib', 'colorama','LunarCalendar','holidays','cmdstanpy==0.9.68','convertdate','openpyxl','wheel','pystan==2.19.1.1','xlrd','jinja2','tzlocal','plotly','prophet==1.0.1'
      ],
     packages=find_packages(),
     include_package_data=True,
     classifiers=[
         'Programming Language :: Python :: 3',
         'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
         'Operating System :: OS Independent'
     ],
     entry_points={"console_scripts": ["perfectoai=perfecto.perfectoai:main"]}
 )
