import os
import sys
import subprocess

# Set the environment variable to disable frozen modules
os.environ["PYTHONBREAKPOINT"] = "debugpy.breakpoint"

# Construct the command to run solara with the -X option
command = [sys.executable, "-Xfrozen_modules=off", "-m", "solara", "run", "sol.py"]

# Run the command
subprocess.run(command)