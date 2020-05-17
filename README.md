# Graditude

[![pipeline status](https://travis-ci.com/tomvothecoder/graditude.svg?branch=master)](https://travis-ci.com/tomvothecoder/graditude)
[![Codecov Coverage](https://codecov.io/gh/tomvothecoder/graditude/branch/master/graph/badge.svg)](https://codecov.io/gh/tomvothecoder/graditude)

Graditude is a project designed for new graduate software engineers to land their next job. Graditude's design is based on minimalism in order to provide a streamlined job hunting experience. Whether the focus is in software engineering or web dev, we've got you covered.

## Repository Structure

This project is structured as a mono-repo, encompassing two separate sub-projects for the front-end and back-end. Please navigate to their respective directories for more information, or click the links below.

### Getting Started

#### Setup pre-commit

This repo has default integration with pre-commit for identifying simple issues before submission to code review. Since this a Python package, you will need to setup the Python virtual environment to install pre-commit hooks into your local git repo.

The linters and stylers include:

- Code styling: prettier, black
- Linting: ESLint, flake8
- Static Type Checking: mypy

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r config/requirements/local.txt

pre-commit install
```

## Frontend

[![dependencies Status](https://david-dm.org/tomvothecoder/graditude/status.svg?path=frontend)](https://david-dm.org/tomvothecoder/graditude?path=frontend)
[![devDependencies Status](https://david-dm.org/tomvothecoder/graditude/dev-status.svg?path=frontend)](https://david-dm.org/tomvothecoder/graditude?path=frontend&type=dev)

[Getting started](frontend/README.md)

## Backend

[![Made with Django.](https://www.djangoproject.com/m/img/badges/djangomade124x25.gif)](http://www.djangoproject.com)

[![Updates](https://pyup.io/repos/github/tomvothecoder/graditude/shield.svg)](https://pyup.io/repos/github/tomvothecoder/graditude/)
[![Python 3](https://pyup.io/repos/github/tomvothecoder/graditude/python-3-shield.svg)](https://pyup.io/repos/github/tomvothecoder/graditude/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[Getting started](backend/README.md)
