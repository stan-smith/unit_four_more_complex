```
As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied
And telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.
```


E.g. if today's date was 2022-11-01:

>>> age_checker("1960-10-21")
"Access granted!"



Optionally, if you want another 🌶️ and have time left in today's pairing session ...

As an admin
So that invalid entries are rejected
I want to generate an exception when the date of birth isn't the right type or format.


***Design Recipie***
1. Describe problem:
The admin wants to be able to check whether users are old enough/verify their age before they can be "granted access"

2.What are we going to call our func?
AgeChecker

3. What will this function do?
Gets current date time
Gets the users DOB
compares the two
returns whether the user is above or at the age required

***Params***
Date Time parameter serving as DOB of the user.

***Returns:***
String(Access has been granted/not granted)
String(f'Access Denied! You are {User_age} you need to be {required_age}!')

***Side effects***
Just prints to stdout the result of their input, no data manipulated

Examples:

Not needed due to being tested through behaviour
<!-- def test_required_age():
    assert AgeChecker.required_age == 16 -->

def test_user_enters_age_too_young():
    assert AgeChecker(10) == 'Access Denied! You are 10 you need to be 16'

