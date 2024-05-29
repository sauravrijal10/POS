from odoo import models


class ProductLabelLayout(models.TransientModel):
    _inherit = "product.label.layout"

    def _prepare_report_data(self):
        xml_id, data = super()._prepare_report_data()
        if self.env.context.get("force_label_qty_by_product"):
            data["quantity_by_product"] = self.env.context["force_label_qty_by_product"]
        return xml_id, data