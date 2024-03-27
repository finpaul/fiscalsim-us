from fiscalsim_us.model_api import *


class oh_section_179_expense_add_back(Variable):
    """
    Line 24 on Ohio schedule of adjustments
    """

    value_type = float
    entity = TaxUnit
    label = "Deduction of prior year 168k and 179 depreciation add-backs"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH
