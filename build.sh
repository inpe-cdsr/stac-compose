
#!/bin/bash

##### DEPLOY

echo
echo "BUILD STARTED"
echo

echo
echo "NEW TAG - API STAC_COMPOSE:"
read API_STAC_COMPOSE_TAG

IMAGE_API_STAC_COMPOSE="registry.dpi.inpe.br/brazildatacube/stac_compose"

IMAGE_API_STAC_COMPOSE_FULL="${IMAGE_API_STAC_COMPOSE}:${API_STAC_COMPOSE_TAG}"

docker build -t ${IMAGE_API_STAC_COMPOSE_FULL} -f docker/prod.Dockerfile .

docker push ${IMAGE_API_STAC_COMPOSE_FULL}