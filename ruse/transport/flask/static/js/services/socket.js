angular.module('ruseWeb').factory('socket', function(socketFactory) {
	var socket = socketFactory({
		ioSocket: io.connect('/ruse')
	});
	return socket;
});
