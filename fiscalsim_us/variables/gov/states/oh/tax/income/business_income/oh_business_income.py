from fiscalsim_us.model_api import *

class oh_business_income(Variable):
    value_type = float
    entity = TaxUnit
    label = "Ohio business income"
    unit = USD
    definition_period = YEAR
    reference = (
        "https://tax.ohio.gov/static/forms/ohio_individual/individual/2023/it1040-sd100-instructionbooklet.pdf",
    )
    defined_for = StateCode.OH

    adds = ["interest_income","dividend_income","capital_gains","capital_losses","farm_rent_income"]
    