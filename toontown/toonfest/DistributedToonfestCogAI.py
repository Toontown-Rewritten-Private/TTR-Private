from panda3d.core import *
from direct.interval.IntervalGlobal import *
from direct.fsm.FSM import FSM
from toontown.toonfest import DistributedToonfestTowerAI
import random
from otp.distributed.OtpDoGlobals import *
from direct.task import Task
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal

class DistributedToonfestCogAI(DistributedObjectAI, FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedToonfestTowerAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        FSM.__init__(self, 'ToonfestCogFSM')
        self.position = (0, 0, 0)
        self.cogid = 0
        self.state = 'Down'
        self.air = air

    def enterOff(self):
        self.requestDelete()

    def generate(self):
        self.toggleCogTask()

    def setProperties(self):
        self.setCogPosId(self.position[0], self.position[1], self.position[2], self.cogid)

    def toggleCogTask(self):
        taskMgr.doMethodLater(10, self.toggleCog, 'toggle-cog', extraArgs=[])

    def toggleCog(self):
        if self.state == 'Down':
            self.state = 'Up'
            self.enterUp()
        elif self.state == 'Up':
            self.state = 'Down'
            self.enterDown()
        taskMgr.doMethodLater(10, self.toggleCog, 'toggle-cog', extraArgs=[])

    def setCogPosId(self, x, y, z, cogid):
        self.sendUpdate('setCogPosId', [x, y, z, cogid])

    def setCogId(self, cogid):
        self.sendUpdate('setCogId', [cogid])

    def setCogPos(self, x, y, z):
        self.sendUpdate('setCogPos', [x, y, z])

    def enterDown(self):
        self.cogDown = True
        self.sendUpdate('toggleCog', ['Down'])

    def enterUp(self):
        self.cogUp = True
        self.sendUpdate('toggleCog', ['Up'])

    def updateTower(self, avName):
        base = random.randrange(0, 3)
        validOperations = ['SpeedUp', 'SlowDown', 'Reverse']
        for operation in validOperations:
            operation = random.choice(validOperations)
        if not DistributedToonfestTowerAI or not self.air.toonfestTower:
            print('DistributedToonfestCogAI: ERROR! Could not find the ToonFest Tower.')
        else:
            if random.randrange(0, 100) >= 80:
                self.air.toonfestTower.d_updateTower(operation, base, avName)
        print('DistributedToonfestCogAI: Told Tower to ' + operation + ' base number ' + str(base + 1))
