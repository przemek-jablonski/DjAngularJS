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
                title: vm.title,
                author: { username: Authentication.getAuthenticatedAccount().username}
            });

            $scope.closeThisDialog();

            function newEntrySuccess(data, status, headers, config) {
                Snackbar.show('Entry succesfully created!');
            }

            function newEntryFailure(data, status, headers, config) {
                $rootScope.$broadcast('entry.created.error');
                Snackbar.error(data.error);
            }
        }
    }


})();