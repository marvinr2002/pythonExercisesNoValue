# Re-run this cell and examine the docstring of each function
from python_functions import validate_name, validate_email, validate_password, top_level_domains

def register_user():

    user_name = input("Enter a valid name")
    user_email = input("Enter a valid email")
    user_password = input ("Enter a password")

    x = validate_name(user_name)
    y = validate_email(user_email)
    z = validate_password(user_password)

    if x or y or z is False:
        return False
    
    user_data = {
        "user": user_name,
        "email":user_email,
        "password": user_password
    }

    print ("Valid user")
    
