# Backend Functional and Performance Tests

**Warning: Work In Progress**

This is an PoC setup demonstrating how to use different clients and run backend API tests with various frameworks from the same codebase—e.g., functional tests using __Pytest__ and performance tests using __Locust__. To see it in action, follow the examples below and run them against the server simulator (`./tools/server-simulator.py`), [Petstore](https://petstore.swagger.io/), [MockAPI](https://mockapi.io/), or implement new API methods to run them against your own backend.

## Setup
Install the required libraries from `requirements.txt` or run `./setup.sh` in the terminal to create a Python virtual environment and set it up automatically.

## Tests

Below are working examples of test-level implementations. Ensure the `BET_ENV` system environment variable is set according to the given configuration. Refer to the documentation for each testing framework for detailed instructions.

### Pytest Functional Tests

Test example: `./tests/functional_test_example.py`

**Run from the terminal:**

```
pytest
```

### Locust Performance Tests

Test example: `./tests/performnace_test_example.py`

**Run from the terminal:**

```
locust
```
