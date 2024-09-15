import re

def is_email(email):
    ans = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email)
    if ans:
        return True
    else:
        return False


def give_date(string):
    return re.findall(r'\d{2}/\d{2}/\d{4}', string)


def is_phone_number(phone):
    ans = re.match(r'\+\d{1,}.\d{3}.\d{3}.\d{3,}', phone)
    if ans:
        return True
    else:
        return False


def get_link(text):
    return re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
