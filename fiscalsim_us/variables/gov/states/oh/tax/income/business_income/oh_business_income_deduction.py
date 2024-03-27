from fiscalsim_us.model_api import *

class oh_business_income_deduction(Variable):
    value_type = float
    entity = TaxUnit
    label = "Ohio business income deduction"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://tax.ohio.gov/static/forms/ohio_individual/individual/2023/it1040-sd100-instructionbooklet.pdf",
    )
    defined_for = StateCode.OH

    def formula(tax_unit, period, parameters):
        income = tax_unit("adjusted_gross_income", period)
        filing_status = tax_unit("filing_status", period)
        bus_income = tax_unit("oh_business_income", period)
        p = parameters(period).gov.states.oh.tax.income.deductions
        status = filing_status.possible_values
        line11min = min_(income,bus_income)
        line11nonneg = max_(line11min,0)
        filing_status == status.SINGLE
        filing_status == status.JOINT
        filing_status == status.SEPARATE
        line12 = p.bus_inc_ded_amount[filing_status]
        
        return min_(line11nonneg,line12)
        
    