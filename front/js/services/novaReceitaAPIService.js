angular.module("maluReceitas").service("novaReceitaAPI",function($http, config){

    this.postReceita = function(nome,categorias,data_de_criacao,
                              ingredientes, modo_de_preparo, tempo_de_preparo,
                              rendimento, grau_de_dificuldade, imagem){
        return $http.post(config.baseUrl +"/website/receitas/add/?next=/trabalhoPOO/receitas/",{nome:nome,categorias:categorias,data_de_criacao:data_de_criacao,
                                  ingredientes:ingredientes, modo_de_preparo:modo_de_preparo, tempo_de_preparo:tempo_de_preparo,
                                  rendimento:rendimento, grau_de_dificuldade:grau_de_dificuldade, imagem:imagem});
    };

});
