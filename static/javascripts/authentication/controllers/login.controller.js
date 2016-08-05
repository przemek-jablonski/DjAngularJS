(function() {
    'use strict';

    angular
        .module('thinkster.authentication.controllers')
        .controller('LoginController', LoginController);

    LoginController.$inject = ['$location', '$scope', 'Authentication'];

    function LoginController($location, $scope, Authentication) {
        // vm -> viewmodel
        var vm = this;

        vm.login = login;
        activate();

        function activate() {
            // if user is authenticated, redirect to '/' should be made
            if (Authentication.isAuthenticated()) {
                $location.url('/');
            }
        }

        function login() {
            Authentication.login(vm.email, vm.password);
        }
    }

})();