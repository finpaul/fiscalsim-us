from fiscalsim_us.model_api import *


class oh_losses_from_sale(Variable):
    """
    Line 5 on Ohio schedule of adjustments
    """

    value_type = float
    entity = TaxUnit
    label = "Losses from sale or disposition of Ohio public obligations"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH