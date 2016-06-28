angular.module("maluReceitas").controller("loginCtrl", function($scope, loginAPI,$location){
        $scope.usuarios = [];

        $scope.cadastrarUsuario = function(usuario){
            usuarioAPI.postCadastrarUsuario(usuario).success(function(data){
               delete $scope.usuario;
                $scope.formCadastro.$setPristine();
                $location.path("/home");
            });
        };

        $scope.login = function(usuario){
                console.log({username: $scope.usuario.username,password:$scope.usuario.password});
                usuarioAPI.postLogin($scope.usuario.username,$scope.usuario.password).success(function(data){
                    console.log(data);
                });
        };


});
