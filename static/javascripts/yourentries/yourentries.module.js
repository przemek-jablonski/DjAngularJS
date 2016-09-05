(function () {
    'use strict';

    angular
        .module('thinkster.yourentries', [
            'thinkster.yourentries.controllers',
            'thinkster.yourentries.directives',
            'thinkster.yourentries.services'
        ]);

    angular
        .module('thinkster.yourentries.controllers', []);

    //ngDialog as dependency (MODALS - modal dialogs and popups)
    angular
        .module('thinkster.yourentries.directives', ['ngDialog']);

    angular
        .module('thinkster.yourentries.services', []);

})();