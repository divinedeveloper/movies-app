'use strict';
// Declare app level module which depends on filters, and services
var myApp = angular.module('myApp', ['myApp.filters', 'myApp.services', 'myApp.directives','ngRoute', 'ng-environments', 'ngAnimate', 'toaster']).
 	config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider, $rootScope) {
        $routeProvider.when('/', {
            templateUrl: '/static/pages/list.html', 
            controller: 'MoviesListCtrl',
        });

        $routeProvider.when('/movie-detail/:movieId', {
            templateUrl: '/static/pages/movieDetail.html', 
            controller: 'MovieDetailCtrl',
        });

        $routeProvider.when('/new-movie', {
            templateUrl: '/static/pages/newMovie.html', 
            controller: 'MovieDetailCtrl',
        });
        
        $routeProvider.when('/edit-movie/:movieId', {
            templateUrl: '/static/pages/editMovie.html', 
            controller: 'MovieDetailCtrl',
        });
        
        $routeProvider.when('/page-not-found', {
            templateUrl: '/static/pages/page-not-found.html'
                       
        });
	    $routeProvider.otherwise({redirectTo: '/'});
	    $locationProvider.html5Mode(true);
  }]);

