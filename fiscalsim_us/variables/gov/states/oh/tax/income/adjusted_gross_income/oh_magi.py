from fiscalsim_us.model_api import *

class oh_magi(Variable):
    value_type = float
    entity = TaxUnit
    label = "Ohio modified adjusted gross income"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://codes.ohio.gov/ohio-revised-code/section-5747.055",
        "https://tax.ohio.gov/static/forms/ohio_individual/individual/2023/it1040-sd100-instructionbooklet.pdf",
    )
    defined_for = StateCode.OH

    adds = ["adjusted_gross_income", "oh_business_income_deduction"]