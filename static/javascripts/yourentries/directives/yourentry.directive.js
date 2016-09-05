(function () {
    'use strict';

    angular
        .module('thinkster.yourentries.directives')
        .directive('yourentry', yourentry);

    function yourentry() {
        var directive = {
            restrict: 'E',
            scope: {
                yourentry: '='
            },
            templateUrl: '/static/templates/yourentries/yourentry.html'
        };
        return directive;
    }

})();