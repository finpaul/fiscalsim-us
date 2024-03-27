from fiscalsim_us.model_api import *


class oh_tax_after_nonrefundable_credits(Variable):
    value_type = float
    entity = TaxUnit
    label = "OH income tax after credits"
    defined_for = StateCode.OH
    unit = USD
    definition_period = YEAR
    reference = "https://tax.ohio.gov/static/forms/ohio_individual/individual/2023/it1040-sd100-instructionbooklet.pdf"

    def formula(tax_unit, period, parameters):
        line8c = tax_unit("oh_income_tax_before_credits", period)
        line9 = tax_unit("oh_nonrefundable_credits", period)
        line10 = line8c - line9 

        return max_(line10, 0)