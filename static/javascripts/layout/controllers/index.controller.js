(function () {
    'use strict';

    angular
        .module('thinkster.layout.controllers')
        .controller('IndexController', IndexController);

    IndexController.$inject = ['$scope', 'Authentication', 'Entries', 'Snackbar'];


    function IndexController($scope, Authentication, Entries, Snackbar) {
        var vm = this;
        vm.isAuthenticated = Authentication.isAuthenticated();
        vm.entries = [];

        activate();

        function activate() {
            Entries.all().then(entrySuccess, entryFailure);

            $scope.$on('entry.created', function(event, entry) {
                vm.entries.unshift(entry);
            });

            $scope.$on('entry.created.error', function() {
                vm.entries.shift();
            });

            function entrySuccess(data, status, headers, config) {
                vm.entries = data.data;
                Snackbar.show("success / data count: " + data.length + " / " + vm.entries.length);
            }

            function entryFailure(data, status, headers, config) {
                Snackbar.error(data.error);
            }
        }
    }

})();