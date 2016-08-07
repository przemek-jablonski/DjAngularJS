(function () {
    'use strict';

    angular
        .module('thinkster.entries.directives')
        .directive('entry', entry);

    function entry() {
        var directive = {
            restrict: 'E',
            scope: {
                entry: '='
            },
            templateUrl: '/static/templates/entries/entry.html'
        };
        return directive;
    }

})();