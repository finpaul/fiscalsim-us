from fiscalsim_us.model_api import *


class oh_income_earned_out_of_state_disaster_deduction(Variable):
    """
    Line 20 on Ohio schedule of adjustments
    """

    value_type = float
    entity = TaxUnit
    label = "Income earned in Ohio by a qualifying out-of-state business during disaster"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH