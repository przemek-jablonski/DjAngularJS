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

            Entries.create(vm.content, vm.title).then(newEntrySuccess, newEntryFailure);

            function newEntrySuccess(data, status, headers, config) {
                Snackbar.show('Entry succesfully created!');
            }

            function newEntryFailure(data, status, headers, config) {
                $rootScope.$broadcast('error' + 'entry.created.error');
                Snackbar.error(data.error);
            }
        }
    }


})();