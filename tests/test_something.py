from python_tester.collect.fixtures import fixture


@fixture
def something_three():
    return "three"


def test_something_or_other():
    raise ValueError()
    assert 1 + 1 == 2
