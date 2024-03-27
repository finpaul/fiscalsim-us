from fiscalsim_us.model_api import *


class oh_business_income_deduction(Variable):
    """
    Line 12 on Ohio schedule of adjustments
    Ohio Schedule of Business Income, line 13
    """

    value_type = float
    entity = TaxUnit
    label = "Business income deduction"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH
    #add after business income is done