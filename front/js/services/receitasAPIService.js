angular.module("maluReceitas").service("receitasAPI",function($http, config){
   this.getReceitas = function(){
        return $http.get(config.baseUrl +"/receitas/?format=json");
    };

    this.getReceita = function(id){
        return $http.get(config.baseUrl +"/receita/"+id+"/?format=json");
    };

    this.getReceitasInCategoria = function(id){
        return $http.get(config.baseUrl + "/categoria/"+id+"/?format=json");
    };

    this.getReceitasInCategoriaMacro = function(id){
      return $http.get(config.baseUrl + "macro/receitas/"+id+"/?format=json");
  };
});
