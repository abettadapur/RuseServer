'use strict';

var app = angular.module('ruseapp', ['ruseappControllers','ngMaterial', 'ngRoute', 'vxWamp']);

app.config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/', {templateUrl: 'partials/home.html', controller: 'HomeController'});
}]);

app.config(
    function($wampProvider) {
        $wampProvider.init({
            url: 'ws:///abettadapurlin2.cloudapp.net:5000/ws',
            realm: 'realm1'
        });
    }
);

app.config(
    function($mdThemingProvider){
        $mdThemingProvider.theme('default')
        .primaryPalette('light-blue')
        .accentPalette('orange');
    }
);

app.run(function($wamp)
{
    $wamp.open();
});
