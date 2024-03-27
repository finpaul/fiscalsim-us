from fiscalsim_us.model_api import *


class oh_tax_due(Variable):
    value_type = float
    entity = TaxUnit
    label = "OH tax due"
    defined_for = StateCode.OH
    unit = USD
    definition_period = YEAR
    reference = "https://tax.ohio.gov/static/forms/ohio_individual/individual/2023/it1040-sd100-instructionbooklet.pdf"

    def formula(tax_unit, period, parameters):
        after = tax_unit("oh_income_tax_after_credits", period)
        credits = tax_unit("oh_refundable_credits", period)

        return after + credits