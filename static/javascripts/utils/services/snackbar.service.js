(function () {
    'use strict';

    angular
        .module('thinkster.utils.services')
        .factory('Snackbar', Snackbar);

    function Snackbar() {
        var Snackbar = {
            error: error,
            show: show
        };
        return Snackbar;

        function _snackbar(content, options) {
            options = _.extend({timeout: 6000}, options);
            options.content = content;
            $.snackbar(options);
        }

        function error(content, options) {
            _snackbar('ERROR: ' + content, options);
        }

        function show(content, options) {
            _snackbar(content, options);
        }

    }

})($, _);