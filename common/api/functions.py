import hashlib
import string
import random
import datetime
import re
from faker import Faker

fake_data = Faker()


def md5(arg):
    """
    md5 encrypted
    :param arg: Target String
    :return: Encrypted String
    """
    hash_string = hashlib.md5()
    hash_string.update(arg.encode("utf-8"))
    return hash_string.hexdigest()


def name():
    """
    Generate random English name
    :return:
    """
    return fake_data.name()


def address():
    """
    Generate random address
    :return: 
    """
    return fake_data.address()


def phone_number():
    """
    Generate random phone number
    :return:
    """
    return fake_data.phone_number()


def randomint(length):
    """
    Generates a number of the specified length
    :param length: number length
    :return:
    """
    s = [str(i) for i in range(10)]
    return ''.join(random.sample(s, length))


def randomstr(length=20):
    """
    Generates random combination of uppercase and lowercase with the specified length
    :param length:
    :return:
    """
    return fake_data.pystr(max_chars=length)


def randomstrwithnum(length):
    """
    Generates random combination of number, uppercase and lowercase with the specified length
    :param length:
    :return:
    """
    return ''.join(random.sample(string.ascii_letters + string.digits + string.digits, length))


def now(pattern="%Y-%m-%d %H:%M:%S", hours=0):
    """
    Generate current time
    :param pattern: eg:  %Y-%m-%d %H:%M:%S
    :param hours: Set the hour offset  eg:  hours=1  it means that current time plus one hour.
    :return:
    """
    return (datetime.datetime.now() + datetime.timedelta(hours=hours)).strftime(pattern)


def regex(target_str, pattern, index=0):
    """
    RegExp match
    :param target_str: target string
    :param pattern: RegExp
    :param index: list index
    :return: All the matching results, list form
    """
    results = re.findall(pattern, target_str)
    return results[index] if results != [] else results
