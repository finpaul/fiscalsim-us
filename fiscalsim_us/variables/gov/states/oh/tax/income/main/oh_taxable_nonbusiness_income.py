from fiscalsim_us.model_api import *


class oh_taxable_nonbusiness_income(Variable):
    value_type = float
    entity = TaxUnit
    label = "OH taxable nonbusiness_income"
    defined_for = StateCode.OH
    unit = USD
    definition_period = YEAR
    reference = "https://tax.ohio.gov/static/forms/ohio_individual/individual/2023/it1040-sd100-instructionbooklet.pdf"

    def formula(tax_unit, period, parameters):
        income = tax_unit("oh_taxable_business_income", period)
        taxbase = tax_unit("oh_tax_base", period)
        line7 = taxbase - income
        
        return max_(line7,0)