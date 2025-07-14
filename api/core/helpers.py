import string
import random
import datetime

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def generate_otp_number(length=6):
    return ''.join(random.choices(string.digits, k=length))


def remove_gmail(email):
    return email.split('@')[0]

def get_current_date_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")