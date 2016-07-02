angular.module("maluReceitas").controller("receitasCategoriasCtrl", function($scope, receitas, categorias){
    $scope.receitas= receitas.data;
    $scope.categorias = categorias.data;

    var listaCategorias = $scope.categorias;
    listaVazia = function(listaCategorias){
      if(listaCategorias.length == 0){
        return true;
      } else{
        return false;
      }
    }
    var verificaLista = listaVazia(listaCategorias);

    $scope.verificaCategoria = verificaLista;

    var listaReceitas = $scope.receitas;
    listaVazia = function(lista){
      if(lista.length == 0){
        return true;
      } else{
        return false;
      }
    }
    var verificaLista = listaVazia(listaReceitas);

    $scope.verificaReceita = verificaLista;
});
