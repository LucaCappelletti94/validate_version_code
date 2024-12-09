# validate_version_code

![PyPI](https://badge.fury.io/py/validate-version-code.svg)  
![Downloads](https://pepy.tech/badge/validate-version-code)
[![License](https://img.shields.io/github/license/LucaCappelletti94/validate_version_code)](https://github.com/LucaCappelletti94/validate_version_code/blob/master/LICENSE)
[![Github Actions](https://github.com/LucaCappelletti94/validate_version_code/actions/workflows/python.yml/badge.svg)](https://github.com/LucaCappelletti94/validate_version_code/actions/)

Python package to validate version codes.

## How do I install this package?

As usual, just download it using pip:

```bash
pip install validate_version_code
```

## Tests Coverage

Since coverage tools can yield slightly different results, here are three coverage reports:

![Coveralls](https://coveralls.io/repos/github/LucaCappelletti94/validate_version_code/badge.svg?branch=master)  
![SonarCloud Coverage](https://sonarcloud.io/api/project_badges/measure?project=LucaCappelletti94_validate_version_code&metric=coverage)  
![Code Climate Coverage](https://api.codeclimate.com/v1/badges/4edd0e56c8b989a77b7c/test_coverage)

## Usage Example

Here’s a basic how-to:

```python
from validate_version_code import validate_version_code

valid_version_code = "1.2.3"
invalid_version_code = "beta.3"

assert validate_version_code(valid_version_code)
assert not validate_version_code(invalid_version_code)
```
