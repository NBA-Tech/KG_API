import string
import random
from datetime import datetime

def generate_random_string(length, id_type="student", curr_number=0):
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    number_str = str(curr_number + 1).zfill(3)  # zero-padded to 3 digits
    
    if id_type == "student":
        return f"ENR{year}{month}{number_str}"
    
    elif id_type == "event":
        prefix = "EVENT"
        random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        return f"{prefix}-{year}{month}-{random_part}"
    
    elif id_type == "staff":
        prefix = "STAFF"
        random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        return f"{prefix}-{year}{month}-{random_part}"
    
    elif id_type == "gallery":
        prefix = "GALLERY"
        random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        return f"{prefix}-{year}{month}-{random_part}"
    
    elif id_type == "setting":
        prefix = "SETTING"
        random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        return f"{prefix}-{year}{month}-{random_part}"
    
    elif id_type=="contact":
        prefix = "CONTACT"
        random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        return f"{prefix}-{year}{month}-{random_part}"
    
    else:
        # fallback to a generic random string
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_otp_number(length=6):
    return ''.join(random.choices(string.digits, k=length))


def remove_gmail(email):
    return email.split('@')[0]

def get_current_date_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")