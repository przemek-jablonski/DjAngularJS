(function () {
    'use strict';

    angular
        .module('thinkster.yourentries.services')
        .factory('Yourentries', Yourentries);

    Yourentries.$inject = ['$http'];

    function Yourentries($http) {
        var Yourentries = {
            create: create,
            get: get,
            destroy: destroy
        };
        return Yourentries;


        function create(content, title) {
            return $http.post('/api/v1/entries/', {
                content: content,
                title: title
            });
        }

        function get(username) {
            return $http.get('/api/v1/accounts/' + username + '/entries/');
        }

        function destroy(id) {
            return $http.delete('/api/v1/entries/' + id + "/");
        }

    }

})();