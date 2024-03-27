from fiscalsim_us.model_api import *


class oh_taxes_paid_other_state(Variable):
    """
    Line 3 on Ohio schedule of adjustments
    """

    value_type = float
    entity = TaxUnit
    label = "Taxes paid to another state or District of Columbia"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH