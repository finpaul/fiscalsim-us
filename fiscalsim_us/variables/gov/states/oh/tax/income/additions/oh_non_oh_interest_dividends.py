from fiscalsim_us.model_api import *


class oh_non_oh_interest_dividends(Variable):
    """
    Line 1 on Ohio schedule of adjustments
    """

    value_type = float
    entity = TaxUnit
    label = "Non-Ohio state and local government interst and dividends"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH
