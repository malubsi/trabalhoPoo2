angular.module("maluReceitas").service("ingredientesAPI",function($http, config){

   this.getIngredientes = function(){
        return $http.get(config.baseUrl + "/ingredientes/?format=json");
    };
    
});
