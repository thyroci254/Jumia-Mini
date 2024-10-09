import re
def Verifypassword(password):
    if len(password) <6:
        return "Your password is too short"
    elif re.search(r"[A-Z]", password):
        return "Atleast 1 Uppercase letter"
    elif re.search(r"[a-z]", password):
        return "Atleast 1 lowercase letter"
    elif re.search("[0-9]",password):
        return "Atleast 1 digit"
    elif re.search("[!@#$%^&*]"):
        return "Atleast one special character"
    else:
        return True
    
    

