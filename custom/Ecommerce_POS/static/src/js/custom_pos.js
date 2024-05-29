odoo.define('Ecommerce_POS.custom_pos', function (require) {
    'use strict';

    const { posbus } = require('point_of_sale.utils');
    const { Gui } = require('point_of_sale.Gui');
    const { ClosePosPopup } = require('point_of_sale.ClosPosPopup');
    const { Registries } = require('point_of_sale.Registries');

    const CustomClosePosPopup = (ClosePosPopup) => class extends ClosePosPopup {
        async confirm() {
            // Call the original confirm method to handle the session closing
            await super.confirm();

            // Custom redirection after session is closed
            window.location.href = '/web#action=539&model=pos.config&view_type=kanban&cids=1&menu_id=284';
        }
    };

    Registries.Component.extend(ClosePosPopup, CustomClosePosPopup);

    return ClosePosPopup;
});
