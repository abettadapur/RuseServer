from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from twisted.internet.defer import inlineCallbacks


class MyComponent(ApplicationSession):

   @inlineCallbacks
   def onJoin(self, details):
      print("session ready")

      try:
         res = yield self.call(u'com.ruse.search', '1901')
         print("call result: {}".format(res))
      except Exception as e:
         print("call error: {0}".format(e))




runner = ApplicationRunner(url = u"ws://localhost:5000/ws", realm = u"realm1")
runner.run(MyComponent)