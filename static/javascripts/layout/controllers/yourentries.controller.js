(function () {
    'use strict';

    angular
        .module('thinkster.layout.controllers')
        .controller('YourentriesIndexController', YourentriesIndexController);

    YourentriesIndexController.$inject = ['$scope', 'Authentication', 'Yourentries', 'Snackbar', '$routeParams'];


    function YourentriesIndexController($scope, Authentication, Yourentries, Snackbar, $routeParams) {
        var vm = this;
        vm.isAuthenticated = Authentication.isAuthenticated();
        vm.yourentries = [];

        activate();

        function activate() {
            Yourentries.get($routeParams.username.substr(1)).then(entrySuccess, entryFailure);

            function entrySuccess(data, status, headers, config) {
                vm.yourentries = data.data;
                Snackbar.show("OWN ENTRIES / data count: " + data.length + " / " + vm.yourentries.length);
            }

            function entryFailure(data, status, headers, config) {
                Snackbar.error(data.error);
            }
        }


    }

})();