angular.module("maluReceitas").controller("mainCtrl", function($scope,receitasAPI,receitas){
    $scope.receitas= receitas.data;
});
