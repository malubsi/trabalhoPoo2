angular.module("maluReceitas").service("macroCategoriasAPI",function($http, config){

   this.getMacroCategorias = function(){
        return $http.get(config.baseUrl + "/macro/?format=json");
    };

    this.getMacroCategoria = function(id){
        return $http.get(config.baseUrl + "/macro/categorias/"+id+"/?format=json");
    };
});
