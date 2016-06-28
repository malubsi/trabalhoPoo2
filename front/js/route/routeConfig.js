angular.module("maluReceitas").config(function($routeProvider){
        $routeProvider.when("/home",{
            templateUrl:"view/home.html" ,
            controller: "mainCtrl" ,
            resolve:{
                    receitas: function(receitasAPI){
                            return receitasAPI.getReceitas();
                    },
                    categorias: function(categoriasAPI,$route){
                      return categoriasAPI.getMacroCategorias();
                    }
            }
        });

        $routeProvider.when("/novaReceita/",{
        templateUrl:"view/novaReceita.html" ,
        controller: "novaReceitaCtrl",
        resolve:{
                categorias: function(categoriasAPI, $route){
                        return categoriasAPI.getCategorias();
                },
                ingredientes: function(ingredientesAPI, $route){
                        return ingredientesAPI.getIngredientes();
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

          $routeProvider.when("/receita/:id",{
          templateUrl:"view/receitaDetalhes.html" ,
          controller: "receitaDetalhesCtrl",
          resolve:{
                  categorias: function(categoriasAPI, $route){
                          return categoriasAPI.getCategorias();
                  },
                  receita: function(receitasAPI, $route){
                          return receitasAPI.getReceita($route.current.params.id);
                  }
          }
      });

        $routeProvider.when("/receitasInCategoria/:id",{
        templateUrl:"view/receitasCategoria.html" ,
        controller: "receitasCategoriaCtrl",
        resolve:{
                  categorias: function(categoriasAPI,$route){
                    return categoriasAPI.getCategoriasInMacroCategoria($route.current.params.id);
                },

        }
    });

        $routeProvider.when("/categorias/",{
        templateUrl:"view/categorias.html" ,
        controller: "categoriasCtrl",
        resolve:{
                  categoriasMacro: function(categoriasAPI,$route){
                    return categoriasAPI.getMacroCategorias();
                }
        }
    });

        $routeProvider.otherwise({redirectTo: "/home"});
});
