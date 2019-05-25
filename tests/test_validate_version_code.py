from validate_version_code import validate_version_code

def test_validate_version_code():
    assert validate_version_code("1.0.0")
    assert validate_version_code("1.0.0")
    assert not validate_version_code("1")
    assert not validate_version_code("1.2")
    assert not validate_version_code("1.2.a")
    assert not validate_version_code("beta")