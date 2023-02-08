from to_do import TODO


def task10():
    return'''
    INPUT: New customer email address.
    INPUT: Create password longer than six characters.
    CALCULATE: Verify email is valid, if not return error stating why and offering 
    opportunity to amend. If email is valid then check password has 5 or less
    characters, if so then return error stating why and offering opportunity 
    to amend, if 6 or more then send verification email to address to complete.
    OUTPUT: Create new customer account that requires a valid email and at least 
    6 characters in the password'''