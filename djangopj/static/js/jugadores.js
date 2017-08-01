var app = angular.module('futbol', ['ngRoute']);
app.controller('jugadoresController', function($scope){
    $scope.nombre = 'asdasdasd';
    $scope.save = function(){
    };
        alert('ASDAS');
    $scope.formVisibility = false;
    $scope.ShowForm=function(){
        alert('aasdsd');
        $scope.formVisibility = true;
        console.log($scope.formVisibility);
        }
    })
