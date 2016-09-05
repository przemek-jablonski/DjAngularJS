(function () {
    'use strict';

    angular
        .module('thinkster.yourentries.directives')
        .directive('yourentries', yourentries);

    function yourentries() {
        var directive = {
            controller: 'YourentriesController',
            controllerAs: 'vm',
            restrict: 'E',
            scope: {
                yourentries: '='
            },
            templateUrl: '/static/templates/yourentries/yourentries.html'
        };

        return directive;
    }

})();