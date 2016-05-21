angular.module("maluReceitas").service("categoriasAPI",function($http, config){

   this.getCategorias = function(){
        return $http.get(config.baseUrl + "/categorias/?format=json");
    };

    this.getCategoria = function(id){
        return $http.get(config.baseUrl + "/categoria/"+id+"/?format=json");
    };

    this.getCategoriasInMacroCategoria = function(id){
      return $http.get(config.baseUrl + "/macro/categorias/"+id+"/?format=json");
    }
});
