odoo.define('Ecommerce_POS.session_redirect', function (require) {
    "use strict";

    var redirectToURL = function () {
        window.location.href = "http://localhost:8069/web#action=539&model=pos.config&view_type=kanban&cids=1&menu_id=284";
    };

    return {
        redirectToURL: redirectToURL,
    };
});
