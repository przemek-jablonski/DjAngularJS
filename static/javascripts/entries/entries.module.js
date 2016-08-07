(function () {
    'use strict'

    angular
        .module('thinkster.entries', [
            'thinkster.entries.controllers',
            'thinkster.entries.directives',
            'thinkster.entries.services'
        ]);

    angular
        .module('thinkster.entries.controllers', []);

    //ngDialog as dependency (MODALS - modal dialogs and popups)
    angular
        .module('thinkster.entries.directives', ['ngDialog']);

    angular
        .module('thinkster.entries.services', []);

})();