# BE Test

**Warning: Work In Progress**

This is a PoC setup demonstrating how to utilize different frameworks and run tests from the same codebase—for example, functional tests using __Pytest__ and performance tests using __Locust__. To see it in action, follow the examples below and run them against the server simulator (`./tools/server-simulator.py`), [Petstore](https://petstore.swagger.io/), [MockAPI](https://mockapi.io/), or implement new API methods to run them against your own backend.

## Setup
Install the required libraries from `requirements.txt` or run `./setup.sh` in the terminal to create a Python virtual environment and set it up automatically. The main configuration is stored in the `./pyproject.toml` file, and environment-specific configuration is stored in the `./configs/` directory.

## Tests implementation

Test example: `./tests/test_example.py`

Ensure that the system environment variables are set according to the specified configuration, for example:

```
BET_ENV=local|prod
BET_TYPE=e2e|perf
```

Refer to the documentation for each testing framework for detailed instructions.

### Pytest Functional Tests

Run from the terminal:

```
pytest
```

### Locust Performance Tests

Run from the terminal:

```
locust
```

## Test runner

Run tests automatically based on the `BET_TYPE` system variable using the `./run_tests.sh` script.
