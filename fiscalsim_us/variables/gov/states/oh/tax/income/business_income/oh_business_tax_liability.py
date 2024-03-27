from fiscalsim_us.model_api import *


class oh_business_tax_liability(Variable):
    value_type = float
    entity = TaxUnit
    label = "OH business tax liability"
    defined_for = StateCode.OH
    unit = USD
    definition_period = YEAR
    reference = "https://tax.ohio.gov/static/forms/ohio_individual/individual/2023/it1040-sd100-instructionbooklet.pdf"

    def formula(tax_unit, period, parameters):
        income = tax_unit("oh_taxable_business_income", period)
        p = parameters(period).gov.states.oh.tax.income.business_income

        return p.business_income_rate * income


