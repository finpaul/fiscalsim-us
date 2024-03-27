from fiscalsim_us.model_api import *


class oh_certian_railroad_deduction(Variable):
    """
    Line 16 on Ohio schedule of adjustments
    """

    value_type = float
    entity = TaxUnit
    label = "Certain railroad benefits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH