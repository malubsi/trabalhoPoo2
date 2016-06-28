angular.module("maluReceitas").controller("receitaDetalhesCtrl", function($scope, receita, categorias){
    $scope.receita= receita.data;
    $scope.categorias = categorias.data;
});
