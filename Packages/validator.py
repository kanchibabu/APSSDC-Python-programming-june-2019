import re

def phonenumbervalidator(number):
    pattern = '^([6-9][0-9]{9}$)|^([0][9876][0-9]{9})$|([+][9][1][6-9][0-9])$'
    if re.match(pattern,str(number)):
        return True
    return False
phonenumbervalidator(9876543111)

email =input("enter email")


def emailvalidator(email):

    pattern = '^[a-z0-9._]{2,20}[@][1-9a-z]{3,18}[.][a-z]{2,4}$'
    if re.match(pattern,email):
        return True
    return False