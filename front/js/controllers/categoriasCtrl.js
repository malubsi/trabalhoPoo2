angular.module("maluReceitas").controller("categoriasCtrl", function($scope, $routeParams, categorias){
    $scope.categorias= categorias.data;

    var listaCategorias = $scope.categorias;
    listaVazia = function(lista){
      if(lista.length == 0){
        return true;
      } else{
        return false;
      }
    }
    var verificaLista = listaVazia(listaCategorias);

    $scope.verifica = verificaLista;
});
