from fiscalsim_us.model_api import *


class oh_additions(Variable):
    """
    Line 2a of Ohio state individual tax return form 1040
    Adds all items found on schedule of adjustments under additions
    """

    value_type = float
    entity = TaxUnit
    label = "Ohio additions"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH

    adds = "gov.states.oh.tax.income.additions.additions"