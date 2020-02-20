# STAC Compose

API to search surface reflectance by STAC


## Structure

- [`stac_compose`](./stac_compose) python scripts to search surface reflectance by STAC
- [`spec`](./spec) Spec of API stac_compose
- [`docs`](./docs) Documentation of stac_compose


## Installation

### Requirements

Make sure you have the following libraries installed:

- [`Python 3`](https://www.python.org/)

Install [`pyenv`](https://github.com/pyenv/pyenv#basic-github-checkout) and [`pyenv-virtualenv`](https://github.com/pyenv/pyenv-virtualenv#installing-as-a-pyenv-plugin). After that, install Python 3.6.8 using pyenv:

```
pyenv install 3.6.8
```

Create a Python environment with the Python version above through pyenv-virtualenv:

```
pyenv virtualenv 3.6.8 inpe-cdsr-stac-compose
```

Activate the environment:

```
pyenv activate inpe-cdsr-stac-compose
```

Install the requirements:

```
pip install -r requirements.txt
```


## Running

```
pyenv activate inpe-cdsr-stac-compose
python manage.py run
```


### Running with docker

```
docker-compose build
docker-compose up -d
```

Build image:

```
docker build -t inpe-cdsr-stac-compose -f docker/dev.Dockerfile . --no-cache
docker build -t registry.dpi.inpe.br/inpe-cdsr/stac-compose:0.0.2 -f docker/prod.Dockerfile . --no-cache
```

Push image to registry:

```
docker push registry.dpi.inpe.br/inpe-cdsr/stac-compose:0.0.2
```
