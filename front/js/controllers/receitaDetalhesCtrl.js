angular.module("maluReceitas").controller("receitaDetalhesCtrl", function($scope, $routeParams, receita, categorias){
    $scope.receita = receita.data;
    $scope.categorias = categorias.data;
    console.log(categorias);
});
