angular.module("maluReceitas").controller("categoriasCtrl", function($scope, $routeParams, categorias){
    $scope.categorias= categorias.data;
});
