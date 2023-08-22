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

def generateChannelName() -> str:
    return secrets.token_hex(16)

