from validate_version_code import extract_version_code, validate_version_code


def test_extract_version_code():
    assert validate_version_code(extract_version_code("validate_version_code"))
    assert validate_version_code(extract_version_code())
