import pip
from subprocess import call
from sys import argv

for dist in pip.get_installed_distributions():
	call("pip install --upgrade " + dist.project_name, shell=True)
