from fiscalsim_us.model_api import *


class mt_dependent_exemption_count(Variable):
    value_type = float
    entity = TaxUnit
    label = "Total Ohio exemption amount"
    unit = USD
    definition_period = YEAR
    reference = "https://tax.ohio.gov/static/forms/ohio_individual/individual/2023/it1040-sd100-instructionbooklet.pdf"
    defined_for = StateCode.OH

    def formula(tax_unit, period, parameters):
        p = parameters(period).gov.states.oh.tax.income.exemptions
        count = tax_unit("oh_exemption_count", period)

        return count * p.exemption_amount
