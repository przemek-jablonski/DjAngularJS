(function () {
    'use strict';

    angular
        .module('thinkster.layout.controllers')
        .controller('NavbarController', NavbarController);

    NavbarController.$inject = ['$scope', 'Authentication', 'Entries'];

    function NavbarController($scope, Authentication) {
        var vm = this;

        vm.logout = logout;
        vm.ownEntries = ownEntries;

        function logout() {
            Authentication.logout();
        }
    }

})();