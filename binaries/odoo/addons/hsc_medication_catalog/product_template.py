from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    x_concept_source = fields.Selection(
        selection=[
            ("https://cielterminology.org", "CIEL"),
            ("http://snomed.info/sct/", "SNOMED CT"),
            ("http://loinc.org", "LOINC"),
        ],
        string="Concept Source",
    )
    x_concept_code = fields.Char(string="Concept Code")
    x_drug_strength = fields.Char(string="Drug Strength")
