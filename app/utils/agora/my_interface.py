
import time
from app.utils.agora.src.RtcTokenBuilder import *

appID = "67fa993d64a346e1a2587f4a8b96f569"
appCertificate = "534094b2fbda4bb7b93fbdcfb55daf79"
uid = 0
expireTimeInSeconds = 14400
currentTimestamp = int(time.time())
privilegeExpiredTs = currentTimestamp + expireTimeInSeconds


def generateTokenMentor(channelName):
    token = RtcTokenBuilder.buildTokenWithUid(appID, appCertificate, channelName, uid, Role_Publisher, privilegeExpiredTs)
    return token

def generateTokenClient(channelName):
    token = RtcTokenBuilder.buildTokenWithUid(appID, appCertificate, channelName, uid, Role_Subscriber, privilegeExpiredTs)
    return token