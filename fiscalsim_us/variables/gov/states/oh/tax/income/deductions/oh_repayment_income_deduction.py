from fiscalsim_us.model_api import *


class oh_repayment_income_deduction(Variable):
    """
    Line 26 on Ohio schedule of adjustments
    """

    value_type = float
    entity = TaxUnit
    label = "Repayment of income reported in a prior year"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH
