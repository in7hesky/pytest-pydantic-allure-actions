# pytest-pydantic-allure-actions
### Project Description ###

A pytest-pydantic-allure framework wrapped in a docker container with github-actions integration.

System Under Test (SUT): - [Swagger](https://petstore.swagger.io/?url=https://release-gs.qa-playground.com/api/v1/swagger.json). 

List of main tools and libraries used:

- pytest
- pydantic
- faker
- allure-pytest
- docker-compose
- github-actions workflow

## 1. Prerequisites
For local test run make sure you have installed:
- pyenv / python interpreter (the tested version can be found in `.python-version` file)
- [Optional] Allure (2.32.0 tested) to generate reports manually. See https://allurereport.org/docs/ \
  for installation guidance

## 2. Running tests locally
### 2.1 Installing
Just `git clone` the repo to any desired location, `cd` to it and run the following (Linux):
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Done.
#### 2.2 Executing run command
Being in the project's `root` directory you may just execute:
```
pytest
```
The defaults for the command are set in `pyproject.toml`.
#### 3. Generating the report
Now you may proceed with generating an **allure report**. To do this, specify the path to the report's directory:
```
allure serve allure-results
```
Again, the location is set in `pyproject.toml` and can be overwritten before test run.
