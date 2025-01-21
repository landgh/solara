## Kill orphaned python in powershell
```powershell
Get-Process python | ForEach-Object { Stop-Process -Id $_.Id -Force }  539  cd solara
```

## How to Standup Solara Tutorial Locally
Create venv within solara/solara, activate it, pip install -r requirements-dev.txt to the failure point. Then run, install missing packages repetatively till completion. Collect requirements into req.ld.txt

```bash
solara run solara.website.pages --auto-restart
pip freeze > req.ld.txt
```

Remove solara package if installed. Otherwise, code inside will be executed.
```bash
(venv2) /d/mypython/solara master $ pip uninstall solara
(venv2) /d/mypython/solara master $ find . -name "__pycache__" -exec rm -r {} +
```

Install in Editable Mode: Use pip to install the local version in editable mode (-e flag): This creates a link between your Python environment and the local source, so changes to the source are reflected immediately.

```bash
(venv2) /d/mypython/solara master $ pip install -e .
Obtaining file:///D:/mypython/solara
  Installing build dependencies ... done
  Checking if build backend supports build_editable ... done
  Getting requirements to build editable ... done
  Installing backend dependencies ... done
  Preparing editable metadata (pyproject.toml) ... done
  ...

(venv2) /d/mypython/solara master $ python -c "import solara; print(solara.__file__)"
D:\mypython\solara\solara\__init__.py
```

Unstall ptvsd (outdated debugger), and install debugpy
```bash
 pip uninstall ptvsd
 pip install debugpy

solara run solara.website.pages --auto-restart
```
## How to Setup Remote Debug