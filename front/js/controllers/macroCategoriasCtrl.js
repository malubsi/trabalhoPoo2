angular.module("maluReceitas").controller("macroCategoriasCtrl", function($scope, macroCategorias){
    $scope.macroCategorias = macroCategorias.data;
});
