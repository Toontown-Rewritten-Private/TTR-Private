import urllib.request, urllib.parse, urllib.error
import os
from panda3d.core import HTTPClient, Ramfile
from direct.directnotify import DirectNotifyGlobal

class BanManagerAI:
    notify = DirectNotifyGlobal.directNotify.newCategory('BanManagerAI')
    BanUrl = config.ConfigVariableString('ban-base-url', 'http://vapps.disl.starwave.com:8005/dis-hold/action/event').getValue()
    App = config.ConfigVariableString('ban-app-name', 'TTWorldAI').getValue()
    Product = config.ConfigVariableString('ban-product', 'Toontown').getValue()
    EventName = config.ConfigVariableString('ban-event-name', 'tthackattempt').getValue()

    def __init__(self):
        self.curBanRequestNum = 0
        self.channels = {}
        self.ramFiles = {}

    def ban(self, avatarId, dislid, comment):
        parameters = ''
        parameters += 'app=%s' % self.App
        parameters += '&product=%s' % self.Product
        parameters += '&user_id=%s' % dislid
        parameters += '&event_name=%s' % self.EventName
        commentWithAvatarId = 'avId-%s ' % avatarId
        commentWithAvatarId += comment
        parameters += '&comments=%s' % urllib.parse.quote(str(commentWithAvatarId))
        baseUrlToUse = self.BanUrl
        osBaseUrl = os.getenv('BAN_URL')
        if osBaseUrl:
            baseUrlToUse = osBaseUrl
        fullUrl = baseUrlToUse + '?' + parameters
        self.notify.info('ban request %s dislid=%s comment=%s fullUrl=%s' % (self.curBanRequestNum,
         dislid,
         comment,
         fullUrl))
        simbase.air.writeServerEvent('ban-request', avId=avatarId, dislid=dislid, comment=comment, fullUrl=fullUrl)
        if config.ConfigVariableBool('do-actual-ban', True).getValue():
            newTaskName = 'ban-task-%d' % self.curBanRequestNum
            newTask = taskMgr.add(self.doBanUrlTask, newTaskName)
            newTask.banRequestNum = self.curBanRequestNum
            http = HTTPClient.getGlobalPtr()
            channel = http.makeChannel(False)
            self.channels[self.curBanRequestNum] = channel
            rf = Ramfile()
            self.ramFiles[self.curBanRequestNum] = rf
            channel.beginGetDocument(fullUrl)
            channel.downloadToRam(rf)
        self.curBanRequestNum += 1

    def cleanupBanReq(self, banReq):
        channel = self.channels.get(banReq)
        if channel:
            del self.channels[banReq]
        ramfile = self.ramFiles.get(banReq)
        if ramfile:
            del self.ramFiles[banReq]

    def doBanUrlTask(self, task):
        banReq = task.banRequestNum
        channel = self.channels.get(banReq)
        if channel:
            if channel.run():
                return task.cont
        else:
            self.notify.warning('no channel for ban req %s' % banReq)
            self.cleanupBanReq(banReq)
            return task.done
        result = ''
        ramfile = self.ramFiles.get(banReq)
        if ramfile:
            result = ramfile.getData()
        self.notify.info('done processing ban request %s, ramFile=%s' % (banReq, result))
        self.cleanupBanReq(banReq)
        return task.done
