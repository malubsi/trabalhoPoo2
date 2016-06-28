angular.module("maluReceitas").controller("receitasCategoriasCtrl", function($scope, receitas, categorias){
    $scope.receitas= receitas.data;
    $scope.categorias = categorias.data;
    console.log(receitas);
    console.log(categorias);
});
