from fiscalsim_us.model_api import *


class oh_exempt_interest(Variable):
    """
    Line 9 on Ohio schedule of adjustments
    """

    value_type = float
    entity = TaxUnit
    label = "Exempt federal interest and dividends subject to state taxation"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH
