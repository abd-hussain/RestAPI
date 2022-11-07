import random
import secrets
from random import randint

def generateAPIKey() -> str:
    return secrets.token_hex(32)


def generateOTP() -> str:
        range_start = 10**(5)
        range_end = (10**6)-1
        return randint(range_start, range_end)


def generateActvationCode() -> str:
        range_start = 10**(5)
        range_end = (10**6)-1
        return randint(range_start, range_end)


# TODO: Handle Request_id in each request
def generateRequestId() -> str:
    try:
        return str(random.sample(range(1, 999999999999999999), 1)[0])
    except ValueError:
        print('Sample size exceeded population size.')
        return "0"
