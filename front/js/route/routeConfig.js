angular.module("maluReceitas").config(function($routeProvider){
        $routeProvider.when("/home",{
            templateUrl:"view/home.html" ,
            controller: "mainCtrl" ,
            resolve:{
                    receitas: function(receitasAPI){
                            return receitasAPI.getReceitas();
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

        $routeProvider.when("/categorias",{
           templateUrl:"view/categorias.html" ,
           controller: "categoriasCtrl",
           resolve:{
                      categorias: function(categoriasAPI,$route){
                        return categoriasAPI.getCategoria();
                      }
                    }
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

        $routeProvider.when("/categoriasInMacroCategoria/:id",{
           templateUrl:"view/categorias.html" ,
           controller: "categoriasInMacroCategoriaCtrl",
           resolve:{
                   categorias: function(receitasAPI,$route){
                           return categoriasAPI.getCategoriasInMacroCategoria($route.current.params.id);
                   },
                    macroCategoria: function(macroCategoriasAPI,$route){
                           return macroCategoriasAPI.getMacroCategoria($route.current.params.id);
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
