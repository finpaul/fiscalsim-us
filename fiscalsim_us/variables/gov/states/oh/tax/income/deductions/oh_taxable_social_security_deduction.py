from fiscalsim_us.model_api import *


class oh_taxable_social_security_deduction(Variable):
    """
    Line 15 on Ohio schedule of adjustments
    Federal 1040 schedule 1, line 6b
    """

    value_type = float
    entity = TaxUnit
    label = "Taxable Social Security benefits"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH