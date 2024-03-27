from fiscalsim_us.model_api import *


class oh_pass_though_entity(Variable):
    """
    Line 2 on Ohio schedule of adjustments
    """

    value_type = float
    entity = TaxUnit
    label = "Ohio pass-through entity taxes excluded from federal adjusted gross income"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH