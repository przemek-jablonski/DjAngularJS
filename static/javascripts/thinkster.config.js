(function() {
    'use strict';

    angular
        .module('thinkster.config')
        .config(config);

    config.$inject=['$locationProvider'];

    // enabling HTML5 routing (instead of hashrouting)
    // getting rid of '# prefix in websites
    function config($locationProvider) {
        $locationProvider.html5Mode(true);
        $locationProvider.hashPrefix('!');
    }

})();
