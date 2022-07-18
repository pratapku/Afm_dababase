import random
from datetime import datetime



variable = None
vb = None
otp = None
photo = None

def get_variable():
    return variable

def create_new_ref_number():
    global random
    variable =(random.randint(10000000,999999999))
    print(variable)


    return variable

def dt():
    global vb
    vb = datetime.today().strftime('%Y-%m-%d')
    return vb

def otplogin():
    global otp
    otp = str(random.randint(111111, 999999))
    return otp