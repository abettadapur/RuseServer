from autobahn.twisted.util import sleep
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
from twisted.internet.defer import inlineCallbacks


class MyComponent(ApplicationSession):
    @inlineCallbacks
    def onJoin(self, details):
        print("session ready")

        def onStatus(status):
            print("status: "+status)

        def onQueue(queue):
            print("queue: "+queue)

        try:
            yield self.subscribe(onStatus, u'com.ruse.now_playing')
            yield self.subscribe(onQueue, u'com.ruse.queue')

            yield sleep(10)

            res = yield self.call(u'com.ruse.play_song', 'Tmc4p2uxfiqksaeobcg64roduny')
        except Exception as e:
            print("call error: {0}".format(e))


runner = ApplicationRunner(url=u"ws://localhost:5000/ws", realm=u"realm1")
runner.run(MyComponent)