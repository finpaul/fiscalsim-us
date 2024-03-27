from fiscalsim_us.model_api import *


class oh_adoption_grant_deduction(Variable):
    """
    Line 22 on Ohio schedule of adjustments
    """

    value_type = float
    entity = TaxUnit
    label = "Ohio adoption grant program payments received from the Ohio Department of Job and Family Services"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH