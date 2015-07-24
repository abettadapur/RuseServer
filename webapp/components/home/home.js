angular.module("ruseapp.home", [])
    .controller("HomeController", ['$scope', '$wamp', HomeController]);

function HomeController($scope,$wamp)
{
    this.name = "Testtest";
    $wamp.subscribe('com.ruse.now_playing', function(args) {
        console.log(args);
        this.name = args[0]['current']['title'];
     });
}
