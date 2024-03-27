from fiscalsim_us.model_api import *


class oh_nonmedical_withdrawals(Variable):
    """
    Line 6 on Ohio schedule of adjustments
    """

    value_type = float
    entity = TaxUnit
    label = "Nonmedical withdrawals from a medical savings account"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH