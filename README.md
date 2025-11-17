# REST API test automation suite

## Pytest-based automated testing for Restful Booker API & Swagger Petstore API

This is a project for comprehensive, simulating real-world API testing framework built with Python and pytest, 
designed to demonstrate automated API validation, coverage strategy, and maintainable test architecture.

The suite tests two public REST APIs:
- Restful Booker API: Typically stable and well-documented API with ~50+ tests covering functional,
negative, and edge-case scenarios.
- Swagger Petstore API: Larger and more complex API with ~80 tests, in case of this suite highlighting also some
real-world challenges such as inconsistent documentation, validation issues, and flaky behavior. Because of this, the
coverage in the end is also not as thorough as with Restful Booker.

## Features
### Reusable API client layer

The `resources/api_clients` module encapsulates all HTTP logic (using `requests` library), ensuring clean and 
maintainable tests with minimal duplication.

### Data factories

The `resources/data_factories` module provides dynamic payload generation for bookings, pets, users, orders, etc.,
removing hardcoded data, supporting parametrization, and enabling more scalable test design.

### Pytest features utilized

The test suite leverages several pytest features for clean and robust test execution:
- Re-usable fixtures via `conftest.py`
- Cross-fixture usage for setup chains
- Parametrization for broader coverage with less code
- Custom markers (smoke, regression, integration)
- Expected failures, skips, and handling of flaky tests via `pytest-rerunfailures`

### Code quality

- `ruff` - linting and style enforcement
- `isort` - automatic import organization
Pre-commit hooks ensure consistent code quality across the project.

### CI/CD integration

A lightweight GitHub Actions pipeline, defined in `.github/workflows/API-pytest-junit.yml`, executes:
- pytest with `pytest-xdist` for parallel execution of the entire test suite
- Simple JUnit XML report generation

## Suite setup

This project was developed using Python 3.13.  
It’s recommended to use the same version to ensure compatibility.  

Install dependencies:
```bash
pip install -r requirements.txt
```

(Optional) install pre-commit hooks:
```bash
pre-commit install
```

## Running tests

Run all tests:
```bash
pytest
```

Run all tests in parallel with `pytest-xdist`:
```bash
pytest -n auto
```
(or replace `auto` with as many workers as you want to utilize)


Run specific tests based on pytest markers defined in `pytest.ini`:
```bash
pytest -m regression
```