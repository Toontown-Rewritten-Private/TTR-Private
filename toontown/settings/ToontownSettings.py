from direct.directnotify import DirectNotifyGlobal
from panda3d.core import loadPrcFileData
from otp.otpbase.Settings import Settings

class ToontownSettings:
    notify = DirectNotifyGlobal.directNotify.newCategory('ToontownSettings')

    def __init__(self):
        self.settings = Settings()
        self.loadFromSettings()

    def loadFromSettings(self):
        mongoDB = self.settings.getBool('game', 'mongodb-client', False)
        loadPrcFileData('toonBase Settings MongoDB', 'want-mongo-client %s' % mongoDB)
        self.settings.updateSetting('game', 'mongodb-client', mongoDB)

        localServerAutoStart = self.settings.getBool('game', 'auto-start-server', True)
        loadPrcFileData('toonBase Auto Start Server', 'auto-start-server %s' % localServerAutoStart)
        self.settings.updateSetting('game', 'auto-start-server', localServerAutoStart)

        electionEvent = self.settings.getBool('game', 'elections', False)
        loadPrcFileData('toonBase Settings Election', 'want-doomsday %s' % electionEvent)
        self.settings.updateSetting('game', 'elections', electionEvent)

        electionDifficulty = self.settings.getInt('game', 'election-difficulty', 1)
        loadPrcFileData('toonBase Settings Election Difficulty', 'election-difficulty %s' % electionDifficulty)
        self.settings.updateSetting('game', 'election-difficulty', electionDifficulty)

        smoothAnimations = self.settings.getBool('game', 'smoothanimations', True)
        loadPrcFileData('toonBase Settings Smooth Animations', 'want-smooth-animations %s' % smoothAnimations)
        self.settings.updateSetting('game', 'smoothanimations', smoothAnimations)

        newTTR = self.settings.getBool('game', 'retro-rewritten', False)
        loadPrcFileData('toonBase Settings Original TTR Start', 'want-retro-rewritten %s' % newTTR)
        self.settings.updateSetting('game', 'retro-rewritten', newTTR)
