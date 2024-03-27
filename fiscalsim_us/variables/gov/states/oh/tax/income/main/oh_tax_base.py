from fiscalsim_us.model_api import *


class oh_tax_base(Variable):
    value_type = float
    entity = TaxUnit
    label = "OH tax base"
    defined_for = StateCode.OH
    unit = USD
    definition_period = YEAR
    reference = "https://tax.ohio.gov/static/forms/ohio_individual/individual/2023/it1040-sd100-instructionbooklet.pdf"

    def formula(tax_unit, period, parameters):
        exp = tax_unit("oh_exemptions_amount", period)
        agi = tax_unit("oh_agi", period)
        exp_agi = agi - exp

        return max_(exp_agi,0)