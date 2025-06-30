import subprocess
import sys

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

for package in requirements:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package]) 