angular.module("maluReceitas").controller("receitasCtrl", function($scope, $routeParams, receitas){
    $scope.receitas = receitas.data;
});
