import datetime
from datetime import date
from datetime import datetime

def AgeChecker(dob):
    required_age = 16
    current_date = datetime.today()
    converted_usr_input = datetime.strptime(dob, "%Y-%m-%d")
    user_age = 0
    
    print(current_date)
    print(converted_usr_input)


    if user_age < 16:
        return f'Access Denied! You are {user_age} you need to be {required_age}'
