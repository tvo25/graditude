# Graditude

[![pipeline status](https://travis-ci.com/tomvothecoder/graditude.svg?branch=master)](https://travis-ci.com/tomvothecoder/graditude)
[![Codecov Coverage](https://codecov.io/gh/tomvothecoder/graditude/branch/master/graph/badge.svg)](https://codecov.io/gh/tomvothecoder/graditude)

Graditude is a project designed for new graduate software engineers to land their next job. Graditude's design is based on minimalism in order to provide a streamlined job hunting experience. Whether the focus is in software engineering or web dev, we've got you covered.

## Repository Structure

This project contains directories for both sides of the stack and Traefik for production HTTP reverse proxy and load balancing.

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

## Getting Started for Local Development

Carefully follow the steps below for a smooth experience.

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [docker-compose](https://docs.docker.com/compose/install/)
- Python >= 3.8 for Pre-commit (contributors)

### 1. Set up Pre-commit (contributors)

This repo has default integration with [pre-commit](https://pre-commit.com/), a tool for identifying simple issues before submission to code review. These checks are performed for all staged files using `git commit` before they are committed to a branch.

#### 1.1 Integrated tools

| Platform              | Code Styling                                     | Linting                                          | Type Checking                 |
| --------------------- | ------------------------------------------------ | ------------------------------------------------ | ----------------------------- |
| Python                | [black](https://black.readthedocs.io/en/stable/) | [flake8](https://github.com/PyCQA/flake8#flake8) | [mypy](http://mypy-lang.org/) |
| JavaScript/TypeScript | [prettier](https://prettier.io/)                 | [ESLint](https://eslint.org/)                    | N/A                           |

#### 1.2 Install

```bash
cd backend

# Create a python3 virtual environment using system-level Python
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install local requirements
pip install -r requirements/local.txt

# Install pre-commit hooks
pre-commit install
```

**Note**, any update to `.pre-commit.config.yaml` requires a re-installation of the hooks.

### 2. Set up Back-end

Open the project in a terminal and `cd backend`.

#### 2.1 Build and Run the Stack

This can take a while, especially the first time you run this particular command on your development system but subsequent runs will occur quickly:

```bash
docker-compose -f docker-compose.yml up --build
```

Remove the `--build` flag when you don't need to rebuild (e.g. no updates to Docker/docker-compose related files).

[Useful Django Management Commands](backend/README.md)

#### 2.3 Accessible Services

- Django: `localhost:8000`

### 3. Set up Front-end

Open the project in a terminal and `cd frontend`.

#### 3.1 Build and Run the Stack

This can take a while, especially the first time you run this particular command on your development system but subsequent runs will occur quickly:

```bash
docker-compose -f docker-compose.yml up --build
```

Remove the `--build` flag when you don't need to rebuild (e.g. no updates to Docker/docker-compose related files).

[Useful React Scripts Commands](frontend/README.md)

#### 3.2 Accessible Services

- React: `localhost:3000`

## Getting Started for Production

Building the production environment involves the same steps as local; however, use `docker-compose.production.yml` instead. The environment also needs to be configured.

### 1. Traefik

You will need to configure each router's `rule`, which is used to route a request to a service (e.g. django, react).

1. Enter directory `./backend/docker/production/traefik/`
2. Open `traefik.yml` in your editor
3. Edit rules for routers
   - Change `example.com` to the domain name (e.g. `graditude.com`)
   - **OPTIONAL:** Change `/prefix` to the domain subdirectory for the service
     - For example, the `PathPrefix` for the rules of backend can be `/graditude-api` and frontend can be `/graditude`.
     - **If you don't use a subdirectory, delete `` PathPrefix(`prefix`) `` for the service**

Once configured, Traefik will get you a valid certificate from Lets Encrypt and update it automatically.

### 2. Back-end

1. Enter directory: `./backend/.envs/.production/`
2. Copy env files `.django.template` and `.postgres.template`
3. Rename files as `.django` and `.postgres`
   | Service | Environment Variable | Description | Documentation | Type | Example |
   |---------- |---------------------------------------------------------------------------------------------------- |------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |--------------------------------------------------------------------------------- |------------------ |-------------------------------------------------------------------------------------------------------------------------- |
   | Django | `DJANGO_READ_DOT_ENV_FILE` | Read the .env file generated using `merge_production_dotenvs_in_dotenv.py` script | | boolean | `DJANGO_READ_DOT_ENV=True` |
   | Django | `DJANGO_SECRET_KEY` | A secret key for a particular Django installation. This is used to provide cryptographic signing, and should be set to a unique, unpredictable value. | [Link](https://docs.djangoproject.com/en/3.0/ref/settings/#secret-key) | string | `DJANGO_SECRET_KEY=YAFKApvifkIFTw0DDNQQdHI34kyQdyWH89acWTogCfm4SGRz2x` |
   | Django | `DJANGO_ADMIN_URL` | The url to access the Django Admin page. It should be set to a unique, unpredictable value (not `admin/`). | | string | `DJANGO_ADMIN_URL=11hxhSu03aSBTOZWCysDvSvcDfa16kFh/` |
   | Django | `DJANGO_ALLOWED_HOSTS` | A list of strings representing the host/domain names that this Django site can serve. This is a security measure to prevent HTTP Host header attacks, which are possible even under many seemingly-safe web server configurations. | [Link](https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts) | array of strings | `DJANGO_ALLOWED_HOSTS=graditude.com`<br><br>Local environment:<br>`DJANGO_ALLOWED_HOSTS=localhost` |
   | Django | `DOMAIN_NAME` | The domain linked to the server hosting the Django site. | | string | `DOMAIN_NAME=graditude.com`<br><br>Local environment:<br>`DOMAIN_NAME=localhost` |
   | Django | `DOMAIN_SUBDIRECTORY` | **OPTIONAL** The domain subdirectory that is proxied to the Django site (e.g. graditude.com/graditude-api). Omit backslash and match backend rules' `PathPrefix` in `traefik.yml`. | | string | `DOMAIN_SUBDIRECTORY=graditude-api` |
   | Django | `CORS_ORIGIN_WHITELIST` | List of origins that are authorized to make HTTP requests. Make sure to add the URL of the front-end here. | [Link](https://github.com/adamchainz/django-cors-headers#cors_origin_whitelist) | array of strings | `CORS_ORIGIN_WHITELIST=https://graditude.com`<br><br>Local environment:<br>`CORS_ORIGIN_WHITELIST=http://localhost:3000` |
   | Django | `CELERY_FLOWER_USER` | The login username for the Celery Flower service. Recommended to make a secured username. | | string | `CELERY_FLOWER_USER=IfVEHezeCxRGRiYSWjsxLfJylfVXuOaa` |
   | Django | `CELERY_FLOWER_PASSWORD` | The login password for the Celery Flower service. Recommended to make a secure password. | | string | `CELERY_FLOWER_PASSWORD=EwP2spXEEXcaXJkdqdvbWSDokkYW77SnEFItlkITmKuW0uROzXnX0rSwAgCEjl0P` |
   | Postgres | `POSTGRES_HOST` <br> `POSTGRES_PORT`<br> `POSTGRES_DB`<br> `POSTGRES_USER`<br> `POSTGRES_PASSWORD` | The default Postgres environment variables are self-explanatory and can be updated if needed. | | string | N/A |

### 3. Front-end

1. Enter directory: `./frontend/.envs/.production/`
2. Copy env file `.react.template` and rename as `.react`

| Service | Environment Variable | Description                    | Documentation | Type   | Example                                                                                                               |
| ------- | -------------------- | ------------------------------ | ------------- | ------ | --------------------------------------------------------------------------------------------------------------------- |
| React   | `REACT_APP_API_URL`  | The URL for the Graditude API. |               | string | `REACT_APP_API_URL=https://api.graditude.com/`<br><br>Local environment:<br>`REACT_APP_API_URL=http://localhost:8000` |
