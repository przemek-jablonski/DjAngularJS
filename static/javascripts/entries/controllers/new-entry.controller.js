(function () {
    'use strict';

    angular
        .module('thinkster.entries.controllers')
        .controller('NewEntryController', NewEntryController);

    NewEntryController.$inject = ['$rootScope', '$scope', 'Authentication', 'Snackbar', 'Entries'];


    function NewEntryController($rootScope, $scope, Authentication, Snackbar, Entries) {
        var vm = this;

        vm.submit = submit;

        function submit() {
            $rootScope.$broadcast('entry.created', {
                content: vm.content,
                author: { username: Authentication.getAuthenticatedAccount().username}
            });

            $scope.closeThisDialog();

            Entries.create(vm.content).then(newEntrySuccess, newEntryFailure);

            function newEntrySuccess(data, status, headers, config) {
                Snackbar.show('Entry created!');
            }

            function newEntryFailure(data, status, headers, config) {
                $rootScope.$broadcast('entry.created.error');
                Snackbar.error(data.error);
            }
        }
    }


})();