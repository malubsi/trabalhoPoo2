angular.module("maluReceitas").controller("receitasCtrl", function($scope, $routeParams, receitas){
    $scope.receitas = receitas.data;

    var listaReceitas = $scope.receitas;
    listaVazia = function(lista){
      if(lista.length == 0){
        return true;
      } else{
        return false;
      }
    }
    var verificaLista = listaVazia(listaReceitas);

    $scope.verifica = verificaLista;
});
