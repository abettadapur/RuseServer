# ##############################################################################
##
##  Copyright (C) 2014 Tavendo GmbH
##
##  Licensed under the Apache License, Version 2.0 (the "License");
##  you may not use this file except in compliance with the License.
##  You may obtain a copy of the License at
##
##      http://www.apache.org/licenses/LICENSE-2.0
##
##  Unless required by applicable law or agreed to in writing, software
##  distributed under the License is distributed on an "AS IS" BASIS,
##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##  See the License for the specific language governing permissions and
##  limitations under the License.
##
###############################################################################

import sys

from twisted.python import log
from twisted.internet import reactor
from twisted.internet.endpoints import serverFromString
from autobahn.wamp import router
from autobahn.twisted import wamp, websocket

from ruse.transport.autobahn.protocol import RuseProtocol




if __name__ == '__main__':
    ## 0) start logging to console
    log.startLogging(sys.stdout)

    ## 1) create a WAMP router factory
    router_factory = router.RouterFactory()

    ## 2) create a WAMP router session factory
    session_factory = wamp.RouterSessionFactory(router_factory)

    ## 3) Optionally, add embedded WAMP application sessions to the router
    component_session = RuseProtocol()
    session_factory.add(component_session)

    ## 4) create a WAMP-over-WebSocket transport server factory
    transport_factory = websocket.WampWebSocketServerFactory(session_factory, \
                                                             debug=True, \
                                                             debug_wamp=False)

    ## 5) start the server from a Twisted endpoint
    server = serverFromString(reactor, "tcp:3000")
    server.listen(transport_factory)

    ## 6) now enter the Twisted reactor loop
    reactor.run()