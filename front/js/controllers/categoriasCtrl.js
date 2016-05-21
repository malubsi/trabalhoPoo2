angular.module("maluReceitas").controller("categoriasCtrl", function($scope, categorias){
    $scope.categorias = categorias.data;
});
