angular.module("maluReceitas").controller("receitasInCategoriaCtrl", function($scope,$routeParams,receitas,categoria){
    $scope.categoria = categoria.data;
    $scope.receitas= receitas.data;
});
