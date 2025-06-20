import datetime
from datetime import date
from datetime import datetime

def AgeChecker(dob):
    required_age = 16
    current_date = datetime.today()
    try: 
        converted_usr_input = datetime.strptime(dob, "%Y-%m-%d")
        age_in_days = str(current_date - converted_usr_input).split(" ")
        user_age =  (int(int(age_in_days[0])/365.25))
        if user_age < 16:
            return f'Access Denied! You are {user_age} you need to be {required_age}'
        else:
            return "Access granted!"
        
    except ValueError as ve:
        print("Please enter a datetime in YYYY-MM-DD")

    # print(current_date)
    # print(converted_usr_input)
    #print(f"testing age {(current_date - converted_usr_input)}")