from fiscalsim_us.model_api import *


class oh_stable_account_deduction(Variable):
    """
    Line 19 on Ohio schedule of adjustments
    """

    value_type = float
    entity = TaxUnit
    label = "amounts contributed to a STABLE account"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH