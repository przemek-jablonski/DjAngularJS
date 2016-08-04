(function(){
    'use strict';

    // syntax: .module(MODULE_NAME, [DEPENDENCIES])
    angular
        .module('thinkster.authentication', [
            'thinkster.authentication.controllers',
            'thinkster.authentication.services'
        ]);

    angular
        .module('thinkster.authentication.controllers', []);

    angular
        .module('thinkster.authentication.services', ['ngCookies']);

})();
