#password validator
#code:-
def check_password(password):
    if len(password) < 8:
        return "Too short!"
    elif not any(char.isdigit() for char in password):
        return "Add atleast one number!"
    elif not any(char.isupper() for char in password):
        return "Add atleat one uppercase letter"
    else:
        return "Password is strong💪"
    
passw = input("Enter your password :")
print(check_password(passw))    