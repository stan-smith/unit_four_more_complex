import lib.age_checker
from lib.age_checker import AgeChecker
import datetime
from datetime import date
from datetime import datetime


def test_check_AgeChecker_func_exists():
    assert hasattr(lib.age_checker, 'AgeChecker')

def test_user_enters_age_too_young():
    assert AgeChecker("2015-06-20") == 'Access Denied! You are 10 you need to be 16'

def test_user_enters_age_old_enough():
    assert AgeChecker("1990-02-18") == "Access granted!"

def test_user_enter_16():
    assert AgeChecker("2009-06-20") == "Access granted!"

def test_user_enters_incorrect_dob():
    AgeChecker("092390") == "Please enter a datetime in YYYY-MM-DD"