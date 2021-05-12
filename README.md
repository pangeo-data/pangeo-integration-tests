# pangeo-integration-tests
Integration testing for the Pangeo cloud ecosystem

## Running the tests locally

Save the following output to a `.env`, adjusting the values to match your local
configuration:
```
# needed for google
GOOGLE_APPLICATION_CREDENTIALS=<path to service account key>
# a bucket you have read/write access to
PANGEO_TEST_BUCKET=<path to bucket>
```

Run the tests:

	tox

## Dependency management

This project uses [pip-tools](https://github.com/jazzband/pip-tools) to lock
its dependencies. The user should edit the `requirements.in` file and run `make
lock` to compile these abstract requirements into a concrete list of
dependencies with pinned versions in the `requirements.txt` file.

To update the lock with the latest versions from PyPI run:

	rm requirements.txt
	make lock
