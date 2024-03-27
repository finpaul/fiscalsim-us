from fiscalsim_us.model_api import *


class oh_federal_conformity(Variable):
    """
    Line 10 on Ohio schedule of adjustments
    """

    value_type = float
    entity = TaxUnit
    label = "Federal conformity additions"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH
