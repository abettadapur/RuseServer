'use strict';

/* Controllers */
var ruseappControllers = angular.module('ruseappControllers', []);

ruseappControllers.controller('HomeController', ['$scope', '$wamp', HomeController]);

function HomeController($scope, $wamp)
{
    $scope.message = "because fuck this";
    $wamp.subscribe('com.ruse.now_playing', function(args)
    {
        $scope.$apply(function() {
            console.log(args);
            $scope.status = args[0];
        });
    });
}

