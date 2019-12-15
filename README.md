![](https://github.com/Markus-Ende/adventofcode2019/workflows/Python%20application/badge.svg)
[![codecov](https://codecov.io/gh/Markus-Ende/adventofcode2019/branch/master/graph/badge.svg)](https://codecov.io/gh/Markus-Ende/adventofcode2019)

# Advent of code 2019

Python solutions for
https://adventofcode.com/2019

## Setup with dev container

Prerequisites:
* Visual studio code with [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension
* under linux you may need to adjust your username and uid in `.devcontainer/devcontainer.json` and `.devcontainer/Dockerfile`, see comments in the files
* Docker
* **No** python needed

Open repository in visual studio code, then choose "reopen in container" to build the dev-container. After this, you can build and run python from the visual studio code internal terminal.

## Run Tests

```bash
pytest
```

## Run Tests on save

```bash
ptw
```

## Show test coverage

```bash
pytest --cov
```
