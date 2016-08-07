(function () {
    'use strict';

    angular
        .module('thinkster.entries.directives')
        .directive('entries', entries);

    function entries() {
        var directive = {
            controller: 'EntriesController',
            controllerAs: 'vm',
            restrict: 'E',
            scope: {
                entries: '='
            },
            templateUrl: '/static/templates/entries/entries.html'
        };

        return directive;
    }

})();