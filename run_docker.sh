set -e

source .env

docker run \
    -v "$GOOGLE_APPLICATION_CREDENTIALS":/key.json \
    -e GOOGLE_APPLICATION_CREDENTIALS=/key.json \
    -e PANGEO_TEST_BUCKET="$PANGEO_TEST_BUCKET" \
    pangeo/integration

