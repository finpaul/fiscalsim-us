from fiscalsim_us.model_api import *


class oh_529_plan_funds(Variable):
    """
    Line 4 on Ohio schedule of adjustments
    """

    value_type = float
    entity = TaxUnit
    label = "529 plan funds used for non-qualified expenses"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH