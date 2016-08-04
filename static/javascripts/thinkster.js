(function() {
    'use strict';

    angular
        // .module('thinkster', [
        //     'thinkster.config',
        //     'thinkster.routes',
        //     'thinkster.authentication'
        // ]);
        .module('thinkster', []);

    angular
        .module('thinkster.routes', ['ngRoute']);

    // angular
    //     .module('thinkster.config', []);

    // handling CSRF protection
    angular
        .module('thinkster')
        .run(run);

    run.$inject = ['$http'];

    function run($http) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
    }

})
