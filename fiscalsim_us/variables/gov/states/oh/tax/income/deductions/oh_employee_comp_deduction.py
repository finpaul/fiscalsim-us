from fiscalsim_us.model_api import *


class oh_employee_comp_deduction(Variable):
    """
    Line 13 on Ohio schedule of adjustments
    """

    value_type = float
    entity = TaxUnit
    label = "Employee compensation earned in Ohio by residents of neighboring states"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH
    