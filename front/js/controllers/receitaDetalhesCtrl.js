angular.module("maluReceitas").controller("receitaDetalhesCtrl", function($scope, $routeParams, receita){
    $scope.receita = receita.data;
});
