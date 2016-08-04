(function() {
    'use strict';

    angular
        .module('thinkster.authentication.services')
        .factory('Authentication', Authentication);

    // injecting Angular services (cookies, http) to service as a dependency
    Authentication.$inject = ['$cookies', '$http'];

    // defining (and returning) factory that was just created ('Authentication')
    /**
    * @namespace Authentication
    * @returns {Factory}
    */
    function Authentication($cookies, $http) {
        var Authentication = { // factory to be returned
            register: register
        };
        return Authentication;

        // registering a new user with data provided
        function register(email, username, password) {
            return $http.post('/api/v1/accounts', {
                email: email,
                username: username,
                password: password
            });
        }
    }
})();
