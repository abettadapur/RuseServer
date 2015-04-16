from ruse.etc.config import config
from ruse.transport.autobahn.app import AppComponent
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner

if __name__ == "__main__":
    runner = ApplicationRunner(url=u"ws://{url}:{port}/ws".format(url=config.BIND, port=config.PORT), realm=u"realm1")
    runner.run(AppComponent)


