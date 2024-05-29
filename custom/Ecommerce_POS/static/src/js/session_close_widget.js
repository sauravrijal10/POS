odoo.define('Ecommerce_POS.session_close_widget', function (require) {
    "use strict";

    var Widget = require('web.Widget');
    var sessionRedirect = require('Ecommerce_POS.session_redirect');

    var SessionCloseWidget = Widget.extend({
        start: function () {
            this._super.apply(this, arguments);

            var self = this;
            this.pos.bind('change:cashier', function () {
                if (!self.pos.get_cashier()) {
                    sessionRedirect.redirectToURL();
                }
            });
        },
    });

    return SessionCloseWidget;
});
