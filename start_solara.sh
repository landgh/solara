#!/bin/sh

#python -m venv venv
#source venv/Scripts/activate
#source ~/.bashrc

# there are VSCode link problem, then "cl" problem in installing from requirements.txt or requirements-dev.txt.
# The way to get by is to follow https://solara.dev/documentation/getting_started/installing to install all the 
# basics. Then trying to start "solara run solara.website.pages:Page" to fail due to missing module, install, restart. At the end, I was able to restart server then collect req into req.ld.txt
find . -name "__pycache__" -exec rm -r {} +
pip install -r req.ld.txt

pip install -e .

solara run solara.website.pages -a 
