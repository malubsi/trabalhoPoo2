angular.module("maluReceitas").controller("categoriasInMacroCategoriaCtrl", function($scope,$routeParams,macroCategoria,categorias){
    $scope.macroCategoria = macroCategoria.data;
    $scope.categorias= categorias.data;
});
