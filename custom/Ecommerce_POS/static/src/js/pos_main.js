odoo.define('Ecommerce_POS.pos_main', function (require) {
    "use strict";

    var models = require('point_of_sale.models');
    var SessionCloseWidget = require('Ecommerce_POS.session_close_widget');

    // Initialize POS models and other configurations here

    // Initialize the session close widget
    var sessionCloseWidget = new SessionCloseWidget();
    sessionCloseWidget.appendTo($('.pos'));
});
