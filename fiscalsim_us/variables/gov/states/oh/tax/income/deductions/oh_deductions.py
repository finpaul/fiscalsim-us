from fiscalsim_us.model_api import *


class oh_deductions(Variable):
    """
    Line 2b of Ohio state individual tax return form 1040
    Adds all items found on schedule of adjustments under deductions
    """

    value_type = float
    entity = TaxUnit
    label = "Ohio deductions"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH

    adds = "gov.states.oh.tax.income.deductions.deductions"