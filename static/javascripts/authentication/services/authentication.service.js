/**
* Authentication
* @namespace thinkster.authentication.services
*/
(function () {
  'use strict';

    angular
      .module('thinkster.authentication.services')
      .factory('Authentication', Authentication);

    Authentication.$inject = ['$cookies', '$http'];

    /**
    * @namespace Authentication
    * @returns {Factory}
    */
    function Authentication($cookies, $http) {
    /**
    * @name Authentication
    * @desc The Factory to be returned
    */
        var Authentication = {
            login: login,
            register: register,
            getAuthenticatedAccount: getAuthenticatedAccount,
            isAuthenticated: isAuthenticated,
            setAuthenticatedAccount: setAuthenticatedAccount,
            unauthenticate: unauthenticate
        };
            return Authentication;


        function register(email, password, username) {
            return $http.post('/api/v1/accounts/', {
                username: username,
                password: password,
                email: email
            });
        }

        function login(email, password) {
            return $http.post('/api/v1/auth/login', {
                email: email,
                password: password
            }).then(loginSuccess, loginFailure);

            function loginSuccess(data, status, headers, config) {
                Authentication.setAuthenticatedAccount(data.data);
                window.location = '/';
            }

            function loginFailure(data, status, headers, config) {
                console.error("login failure");
            }
        }

        function getAuthenticatedAccount() {
            if (!$cookies.authenticatedAccount) {
                return;
            }

            return JSON.parse($cookies.authenticatedAccount);
        }

        function isAuthenticated() {
            return !!$cookies.authenticatedAccount;
        }

        function setAuthenticatedAccount(account) {
            $cookies.authenticatedAccount = JSON.stringify(account);
        }

        function unauthenticate() {
            delete $cookies.authenticatedAccount;
        }

    }
})();
