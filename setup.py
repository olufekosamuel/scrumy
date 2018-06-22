import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
	README = readme.read()

setup(
	name ='olufekoscrumy',
	version='1.0',
	packages=find_packages(),
	include_package_data = True,
	license = 'BSD Lincense',
	description = 'Scrumy App;ication',
	long_description = README,
	author = 'Samuel Olufeko',
	author_email = 'mololuwasamuel12@gmail.com',

)