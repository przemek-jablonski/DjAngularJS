(function () {
    'use strict';

    angular
        .module('thinkster.entries.services')
        .factory('Entries', Entries);

    Entries.$inject = ['$http'];

    function Entries($http) {
        var Entries = {
            all: all,
            create: create,
            get: get,
            getSingle: getSingle
        };
        return Entries;


        function all() {
            return $http.get('/api/v1/entries/');
        }

        function create(content, title) {
            return $http.post('/api/v1/entries/', {
                content: content,
                title: title
            });
        }

        function get(username) {
            return $http.get('/api/v1/accounts/' + username + '/entries/');
        }

        function getSingle(entryId) {
            return $http.get('/api/v1/detail/' + entryId + '/');
        }

    }

})();