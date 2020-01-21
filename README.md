# Search STAC - Brazil Data Cube

API to search surface reflectance by STAC


## Structure

- [`bdc_search_stac`](./bdc_search_stac) python scripts to search surface reflectance by STAC
- [`spec`](./spec) Spec of API bdc_search_stac
- [`docs`](./docs) Documentation of bdc_search_stac


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
pyenv virtualenv 3.6.8 stac_compose
```

Activate the environment:

```
pyenv activate stac_compose
```

Install the requirements:

```
pip install -r requirements.txt
```


## Running

```
pyenv activate stac_compose
python manage.py run
```


### Running with docker

```
docker-compose build
docker-compose up -d
```

Build image:

```
docker build -t inpe-cdsr-stac_compose -f docker/dev.Dockerfile . --no-cache
docker build -t registry.dpi.inpe.br/dgi/stac_compose:0.1.2 -f docker/prod.Dockerfile . --no-cache
```

Push image to registry:

```
docker push registry.dpi.inpe.br/dgi/stac_compose:0.1.2
```
