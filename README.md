![Test status](https://github.com/thisistheplace/joint_model/actions/workflows/test.yml/badge.svg?event=push)

# gcp-fastapi
FastAPI service to provide services for running jobs on GCP cloud run.

## Components
### REST API
The guts of this project are deployed as a service which can be accessed via a REST API. The REST API
is developed using [FastAPI](https://fastapi.tiangolo.com).

This API is deployed here: ...

### Cloud Run
Dockerfiles are provided for each component which can be used to run the services separately using
a cloud service provider:
- Build the REST API using [Dockerfile-rest](Dockerfile-rest)

# Testing
Tests are written using [pytest](https://docs.pytest.org). To run the tests in `docker` execute:

```
bash test.sh
```

# License
The API is distributed under the terms of the [GNU General Public License (GPL)](LICENSE).