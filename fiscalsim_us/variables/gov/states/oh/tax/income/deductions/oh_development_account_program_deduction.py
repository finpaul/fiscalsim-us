from fiscalsim_us.model_api import *


class oh_development_account_program_deduction(Variable):
    """
    Line 18 on Ohio schedule of adjustments
    """

    value_type = float
    entity = TaxUnit
    label = "Amounts contributed to an Ohio county's individual development account program"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH