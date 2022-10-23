import random
import secrets


def generateAPIKey() -> str:
    return secrets.token_hex(32)


def generateOTP() -> str:
    try:
        return str(random.sample(range(1, 999999), 1)[0])
    except ValueError:
        print('Sample size exceeded population size.')
        return "000000"

def generateinvetationCode() -> str:
    try:
        return str(random.sample(range(1, 999999), 1)[0])
    except ValueError:
        print('Sample size exceeded population size.')
        return "000000"

# TODO: Handle Request_id in each request
def generateRequestId() -> str:
    try:
        return str(random.sample(range(1, 999999999999999999), 1)[0])
    except ValueError:
        print('Sample size exceeded population size.')
        return "0"
