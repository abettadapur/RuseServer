'use strict';

/* Controllers */
var ruseappControllers = angular.module('ruseappControllers', []);

ruseappControllers.controller('HomeController', ['$scope', '$wamp', HomeController])
                  .controller('AppController', ['$scope', '$wamp', AppController]);


function AppController($scope, $wamp)
{
    $scope.search = function(query)
    {
        $scope.$emit("onSearching", query);
    };
}

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

    $scope.$on("onSearching", function(event, args)
    {
        console.log("OnSearching");
    });
}

