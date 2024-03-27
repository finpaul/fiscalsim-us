from fiscalsim_us.model_api import *


class oh_bonus_depreciation_add_back(Variable):
    """
    Line 8 on Ohio schedule of adjustments
    """

    value_type = float
    entity = TaxUnit
    label = "Internal Revenue Code 168(k) and 179 depreciation expense add-back"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH
