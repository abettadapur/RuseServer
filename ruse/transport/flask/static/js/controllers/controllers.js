angular.module('ruseWeb').controller('player', function($scope, socket) 
{
	socket.on('status', function(status) {
		console.log(status);
	})
});
