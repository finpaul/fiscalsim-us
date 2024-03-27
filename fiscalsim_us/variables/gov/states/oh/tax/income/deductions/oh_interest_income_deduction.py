from fiscalsim_us.model_api import *


class oh_interest_income_deduction(Variable):
    """
    Line 17 on Ohio schedule of adjustments
    """

    value_type = float
    entity = TaxUnit
    label = "Interest income from Ohio public obligations"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH