from fiscalsim_us.model_api import *


class oh_wage_expense_deduction(Variable):
    """
    Line 27 on Ohio schedule of adjustments
    """

    value_type = float
    entity = TaxUnit
    label = "Wage expense not deducted based on the federal work opportunity tax credit"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH
