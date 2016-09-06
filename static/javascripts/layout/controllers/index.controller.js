(function () {
    'use strict';

    angular
        .module('thinkster.layout.controllers')
        .controller('IndexController', IndexController);

    IndexController.$inject = ['$scope', 'Authentication', 'Entries', 'Snackbar', '$routeParams'];


    function IndexController($scope, Authentication, Entries, Snackbar, $routeParams) {
        var vm = this;
        vm.isAuthenticated = Authentication.isAuthenticated();

        vm.entriesOriginal = [];
        vm.entries = [];

        activate();

        function activate() {
            if ($routeParams.username != null) {
                Entries.get($routeParams.username.substr(1)).then(entrySuccess, entryFailure);
            } else {
                Entries.all().then(entrySuccess, entryFailure);
            }


            $scope.$on('entry.created', function(event, entry) {
                vm.entries.unshift(entry);
            });

            $scope.$on('entry.created.error', function() {
                vm.entries.shift();
            });

            function entrySuccess(data, status, headers, config) {
                vm.entries = data.data;
                vm.entriesOriginal = vm.entries;
                Snackbar.show("success / data count: " + data.length + " / " + vm.entries.length);
            }

            function entryFailure(data, status, headers, config) {
                Snackbar.error(data.error);
            }
        }

        $scope.sortEntriesLikes = function() {
            vm.entries.sort(compareLikes);
        };

        $scope.sortEntriesDate = function () {
            vm.entries = vm.entriesOriginal;
        };

        function compareLikes(a,b) {
          if (a.likes < b.likes)
            return -1;
          if (a.likes > b.likes)
            return 1;
          return 0;
        }

        var SortingType = {
            CREATE_DATE : 0,
            UPDATE_DATE : 1,
            LIKES_COUNT : 2
        };

        var SortingOrder = {
            DESCENDING: 0,
            ASCENDING: 1
        };
    }

})();