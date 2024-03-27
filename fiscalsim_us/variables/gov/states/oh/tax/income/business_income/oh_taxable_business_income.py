from fiscalsim_us.model_api import *


class oh_taxable_business_income(Variable):
    value_type = float
    entity = TaxUnit
    label = "OH taxable business income"
    defined_for = StateCode.OH
    unit = USD
    definition_period = YEAR
    reference = "https://tax.ohio.gov/static/forms/ohio_individual/individual/2023/it1040-sd100-instructionbooklet.pdf"

    def formula(tax_unit, period, parameters):
        income = tax_unit("adjusted_gross_income", period)
        bus_income = tax_unit("oh_business_income", period)
        ded = tax_unit("oh_business_income_deduction", period)
        taxbase = tax_unit("oh_tax_base", period)
        line11min = min_(income,bus_income)
        line11nonneg = max_(line11min,0)
        line14 = line11nonneg - ded

        return min_(line14, taxbase)
