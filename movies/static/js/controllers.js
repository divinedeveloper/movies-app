'use strict';

/* Controllers */

myApp.controller('AppCtrl', ['$scope', '$http', '$rootScope', '$location', 'toaster', function($scope, $http, $rootScope, $location, toaster) {
	$scope.init = function () {
        $location.path("/");
    }
    
    $scope.goToHomePage= function(){

        $location.path("/");
    }
    
    
}]);
    