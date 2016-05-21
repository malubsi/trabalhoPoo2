angular.module("maluReceitas").controller("categoriasReceitasCtrl", function($scope, $routeParams, categorias, receitas){
    $scope.categorias= categorias.data;
    $scope.receitas= receitas.data;
});
