> [!WARNING]
> branch not made to be pushed (as of this commit), only for explaining

# Usage python native
0. install git (not explaining that, you know it)
1. clone repo `git clone https://github.com/bterwijn/PythonLearningGame.git`
2. cd into repo `cd PythonLearningGame`
3. run setup script (doesnt activate venv since its only in the scope of the bash script)
4. activate venv `source venv/bin/activate`
5. run game `python main.py`

# Usage uv
0. install git and uv (uv is just one console comamnd `curl -LsSf https://astral.sh/uv/install.sh | sh`, windows similar)
1. clone repo `git clone https://github.com/bterwijn/PythonLearningGame.git`
2. cd into repo `cd PythonLearningGame`
3. setup project `uv sync`
4. run game `uv run main.py`

# Diff
## files added
 - [`.python-version`][1]
 - [`pyproject.toml`][2]
 - [`uv.lock`][3]

## files removed
 - [`setup.bat`][4]
 - [`setup.sh`][5]

[1]:https://github.com/p1geondove/PythonLearningGame/blob/switch_to_uv/.python-version
[2]:https://github.com/p1geondove/PythonLearningGame/blob/switch_to_uv/pyproject.toml
[3]:https://github.com/p1geondove/PythonLearningGame/blob/switch_to_uv/uv.lock
[4]:https://github.com/bterwijn/PythonLearningGame/blob/main/setup.bat
[5]:https://github.com/bterwijn/PythonLearningGame/blob/main/setup.sh
