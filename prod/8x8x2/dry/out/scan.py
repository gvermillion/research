import os
import subprocess
root_dir = '.'

for directory, subdirectories, files in os.walk(root_dir):
    for f in files:
	subprocess.call(["echo", f])
