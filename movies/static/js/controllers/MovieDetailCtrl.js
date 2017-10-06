myApp.controller('MovieDetailCtrl', ['$scope', '$http', '$location', '$rootScope', '$routeParams', 'toaster', function($scope, $http, $location, $rootScope, $routeParams, toaster) {
        $scope.errorMessage;

        $scope.getDetails = function(){

        	if ($routeParams.movieId) {
        		var movieId = $routeParams.movieId;

        		$http(
                {
                  method: 'GET', 
                  url: 'movie-app/api/v1/view-movie/' + parseInt(movieId) +'/'

                }).
                   success(function(data, status, headers, config) {
                    if(status == 200){
                        $scope.responseMovie = data
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

        	}else {
                toaster.pop('error', "", "Movie not found");
            }

                

        }

        $scope.editMovie = function(movieId){
          $routeParams.movieId = movieId;
          $location.path("/edit-movie/" + $routeParams.movieId);
        }

        $scope.deleteMovie = function(movieId){
          $http(
                {
                  method: 'DELETE', 
                  url: 'movie-app/api/v1/delete-movie/' + parseInt(movieId) +'/'

                }).
                   success(function(data, status, headers, config) {
                    if(status == 200){
                      toaster.pop('success', "", data.message);
                      $location.path("/");
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

        $scope.createMovieData = {
        "name": "",
        "locations": [
          {
            "name": "",
            "timings": [
              {
                "time": ""
              }
            ]
          }
        ]
      }


        $scope.removeLocation = function(index) {
          $scope.createMovieData.locations.splice(index, 1);
        };
        $scope.removeTiming = function(parentIndex, childIndex) {
          $scope.createMovieData.locations[parentIndex].timings.splice(childIndex, 1);
        };
        
        $scope.addLocation = function() {
          console.log($scope.createMovieData);
          $scope.createMovieData.locations.push({ name: '', timings: [{ time: ''}]});
        };

        $scope.addTiming = function(index) {
          $scope.createMovieData.locations[index].timings.push({ time: ''});
        };


        //create new movie
        $scope.createMovie = function(){
        
        
            
                // var movieData = {}
                // movieData.name = $scope.movieName;
                // movieData.locations = []

                // var locationData = {}
                // locationData.name = $scope.locationName;
                // locationData.timings = []

                // var timingData = {}
                // timingData.time = $scope.time;

                // createIECData.code = createIECData.code.toString()
                $http({method: 'POST', url: 'iec/api/v1/lookup/', data: movieData}).
                   success(function(data, status, headers, config) {
                    if(status == 200){
                        $scope.responseIecData = data
                           toaster.pop('success', "", "IEC data available");
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



        
        
}]);