myApp.controller('MoviesListCtrl', ['$scope', '$http', '$location', '$rootScope', '$routeParams', 'toaster', function($scope, $http, $location, $rootScope, $routeParams, toaster) {
        $scope.errorMessage;

        $scope.addNewMovie = function(){

        $location.path("/new-movie");
    }

        $scope.moviesList = function(){

                $http(
                {
                  method: 'GET', 
                  url: 'movie-app/api/v1/movies/', 
                  params: {"name": $scope.name}

                }).
                   success(function(data, status, headers, config) {
                    if(status == 200){
                        $scope.responseMovies = data
                           // toaster.pop('success', "", "Welcome to dashboard");
                   }
                       
                       
                     }).
                 error(function(data, status, headers, config) {
                   if(status == 500){
                        toaster.pop('error', "", data.message);
                    }
                     if(status == 502){
                        toaster.pop('error', "", "Server down");
                    }
                    if(status == 503){
                        toaster.pop('error', "", data.message);
                    }
                       if(status == 401){
                           toaster.pop('error', "", data.message);
                       }
                       if(status == 403){
                           toaster.pop('error', "", data.message);
                       }
                     if(status == 400){
                           toaster.pop('error', "", data.message);
                       }
                    if(status == 404){
                        toaster.pop('error', "", data.message);
//                      $location.path("/page-not-found");
                    }
                 }); 

        }

        $scope.addNewMovie = function(){
            $location.path("/new-movie");
        }

        $scope.viewMovie = function(movieId){
          $routeParams.movieId = movieId;
          $location.path("/movie-detail/" + $routeParams.movieId);
        }

        
        
}]);