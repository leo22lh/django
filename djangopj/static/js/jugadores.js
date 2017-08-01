var app = angular.module('app', []);
app.controller('JugadoresController', function($scope) {
    $scope.nombre = 'asdasdasd'
    $scope.save = function(){
        }
        alert('ASDAS')
    $scope.formVisibility = false;
    $scope.ShowForm=function(){
        alert('aasdsd');
        $scope.formVisibility = true;
        console.log($scope.formVisibility);
        }
    }
