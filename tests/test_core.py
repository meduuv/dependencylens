import pytest
from dependencylens import duplicate_names, package_name, summarize


def test_package_name():
    assert package_name("Requests>=2.0") == "requests"


def test_duplicates():
    assert duplicate_names(["a>=1", "b", "a<3", "b"]) == ["a", "b"]


def test_summary():
    assert summarize(["a", "b", "a"]) == {"count": 3, "unique": 2, "duplicates": ["a"]}


def test_invalid():
    with pytest.raises(ValueError):
        package_name("!!!")
