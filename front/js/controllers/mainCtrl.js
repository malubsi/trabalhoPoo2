angular.module("maluReceitas").controller("mainCtrl", function($scope,receitas, categorias){
    $scope.receitas= receitas.data;
    $scope.categorias = categorias.data;
});
