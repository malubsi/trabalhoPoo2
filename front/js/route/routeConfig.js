angular.module("maluReceitas").config(function($routeProvider){
        $routeProvider.when("/home",{
            templateUrl:"view/home.html" ,
            controller: "mainCtrl" ,
            resolve:{
                    receitas: function(receitasAPI){
                            return receitasAPI.getReceitas();
                    },
                    categorias: function(macroCategoriasAPI,$route){
                      return macroCategoriasAPI.getMacroCategorias();
                    }
            }
        });

         $routeProvider.when("/cadastro",{
            templateUrl:"view/cadastro.html" ,
            controller: "loginCtrl"
        });

         $routeProvider.when("/login",{
            templateUrl:"view/login.html" ,
            controller: "loginCtrl"
        });

       $routeProvider.when("/macroCategorias",{
          templateUrl:"view/macroCategorias.html" ,
          controller: "macroCategoriasCtrl",
          resolve:{
                    macroCategorias: function(macroCategoriasAPI,$route){
                        return macroCategoriasAPI.getMacroCategorias();
                    }
                  }
        });

         $routeProvider.when("/receitasInCategoria/:id",{
            templateUrl:"view/receitasInCategoria.html" ,
            controller: "receitasInCategoriaCtrl",
            resolve:{
                    receitas: function(receitasAPI,$route){
                            return receitasAPI.getReceitasInCategoria($route.current.params.id);
                    },
                     categoria: function(macroCategoriasAPI,$route){
                            return macroCategoriasAPI.getMacroCategoria($route.current.params.id);
                    }
            }
        });

        $routeProvider.when("/macro/receitas/:id",{
           templateUrl:"view/algumacoisa.html" ,
           controller: "categoriasReceitasCtrl",
           resolve:{
                   categorias: function(categoriasAPI,$route){
                           return categoriasAPI.getCategoriasInMacroCategoria($route.current.params.id);
                   },
                   receitas: function(receitasAPI,$route){
                           return receitasAPI.getReceitasInCategoriaMacro($route.current.params.id);
                   }
           }
       });

            $routeProvider.when("/receita/:id",{
            templateUrl:"view/receitaDetalhes.html" ,
            controller: "receitaDetalhesCtrl" ,
            resolve:{
                    receita: function(receitasAPI, $route){
                            return receitasAPI.getReceita($route.current.params.id);
                    }
            }
        });


        $routeProvider.otherwise({redirectTo: "/home"});
});
