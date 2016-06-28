angular.module("maluReceitas").controller("novaReceitaCtrl", function($scope, $location, categorias, ingredientes, novaReceitaAPI){
        $scope.categorias = categorias.data;
        $scope.ingredientes = ingredientes.data;
        $scope.receita = [];

        $scope.cadastrar = function(receita){
                console.log({username: $scope.receita.username,password:$scope.receita.password});
                novaReceitaAPI.postReceita($scope.receita.nome,$scope.receita.categorias,$scope.receita.data_de_criacao,
                                          $scope.receita.ingredientes, $scope.receita.modo_de_preparo, $scope.receita.tempo_de_preparo,
                                          $scope.receita.rendimento, $scope.receita.grau_de_dificuldade, $scope.receita.imagem).success(function(data){
                    console.log(data);
                });
        };

});
