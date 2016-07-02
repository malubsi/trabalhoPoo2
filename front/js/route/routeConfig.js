angular.module("maluReceitas").config(function($routeProvider){
        $routeProvider.when("/home",{
            templateUrl:"view/home.html" ,
            controller: "receitasCategoriasCtrl" ,
            resolve:{
                    receitas: function(receitasAPI){
                            return receitasAPI.getReceitas();
                    },
                    categorias: function(categoriasAPI){
                      return categoriasAPI.getMacroCategorias();
                    }
            }
        });

        $routeProvider.when("/novaReceita",{
        templateUrl:"view/novaReceita.html" ,
        controller: "novaReceitaCtrl",
        resolve:{
                categorias: function(categoriasAPI){
                        return categoriasAPI.getCategorias();
                },
                ingredientes: function(ingredientesAPI){
                        return ingredientesAPI.getIngredientes();
                }
        }
    });

          $routeProvider.when("/receita/:id",{
          templateUrl:"view/receitaDetalhes.html" ,
          controller: "receitaDetalhesCtrl",
          resolve:{
                  categorias: function(categoriasAPI){
                          return categoriasAPI.getCategorias();
                  },
                  receita: function(receitasAPI, $route){
                          return receitasAPI.getReceita($route.current.params.id);
                  }
          }
      });

        $routeProvider.when("/receitasInCategoria/:id",{
        templateUrl:"view/receitasInCategorias.html" ,
        controller: "receitasCtrl",
        resolve:{
                  receitas: function(receitasAPI,$route){
                    return receitasAPI.getReceitasInCategoria($route.current.params.id);
                },

        }
    });

        $routeProvider.when("/categorias/:id",{
        templateUrl:"view/categoriasDetalhes.html" ,
        controller: "categoriasCtrl",
        resolve:{
                  categorias: function(categoriasAPI,$route){
                    return categoriasAPI.getCategoriasInMacroCategoria($route.current.params.id);
                  }
        }
    });

        $routeProvider.when("/categorias",{
        templateUrl:"view/categorias.html" ,
        controller: "categoriasCtrl",
        resolve:{
                  categorias: function(categoriasAPI){
                    return categoriasAPI.getCategorias();
                  }
        }
    });

        $routeProvider.otherwise({redirectTo: "/home"});
});
