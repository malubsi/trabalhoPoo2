angular.module("maluReceitas",["ngMessages","ngRoute"]);
angular.module("maluReceitas").config(function($httpProvider){      
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
});
