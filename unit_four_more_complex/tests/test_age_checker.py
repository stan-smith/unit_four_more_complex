import lib.age_checker
from lib.age_checker import AgeChecker


def test_check_AgeChecker_func_exists():
    assert hasattr(lib.age_checker, 'AgeChecker')

def test_user_enters_age_too_young():
    assert AgeChecker("2015-06-20") == 'Access Denied! You are 10 you need to be 16'
