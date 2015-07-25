'use strict';

/* Controllers */
var ruseappControllers = angular.module('ruseappControllers', []);

ruseappControllers.controller('HomeController', ['$scope', '$wamp', HomeController])
                  .controller('AppController', ['$scope', '$wamp', AppController]);


function AppController($scope, $wamp)
{
    $scope.query = "";
    $scope.search = function()
    {
        console.log("Searching for "+$scope.query);
        $scope.$broadcast(events.onSearching, $scope.query);
    };
}

function HomeController($scope, $wamp)
{
    $wamp.subscribe('com.ruse.now_playing', function(args)
    {
        $scope.$apply(function() {
            console.log(args);
            $scope.status = args[0];
        });
    });

    $scope.$on(events.onSearching, function(event, args) {
                   //show progress spinner
    });

    $scope.$on(events.onSearchResults, function (event, args) {
        //hide progress spinner
        //update search results here
    });
}

