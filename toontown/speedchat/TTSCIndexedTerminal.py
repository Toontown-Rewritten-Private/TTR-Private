from otp.speedchat.SCTerminal import *
from otp.otpbase.OTPLocalizer import SpeedChatStaticText
TTSCIndexedMsgEvent = 'SCIndexedMsg'

def decodeTTSCIndexedMsg(msgIndex):
    return SpeedChatStaticText.get(msgIndex, None)


class TTSCIndexedTerminal(SCTerminal):

    def __init__(self, msg, msgIndex):
        SCTerminal.__init__(self)
        self.text = msg
        self.msgIndex = msgIndex

    def handleSelect(self, event):
        event = str(event)
        if not event.startswith('mouse3'):
            SCTerminal.handleSelect(self, event)
            messenger.send(self.getEventName(TTSCIndexedMsgEvent), [self.msgIndex])
