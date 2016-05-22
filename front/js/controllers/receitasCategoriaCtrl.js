angular.module("maluReceitas").controller("receitasCategoriaCtrl", function($scope, $routeParams, categorias){
    $scope.categorias= categorias.data;
});
