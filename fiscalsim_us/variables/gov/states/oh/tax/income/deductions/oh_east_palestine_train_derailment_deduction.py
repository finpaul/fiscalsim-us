from fiscalsim_us.model_api import *


class oh_east_palestine_train_derailment_deduction(Variable):
    """
    Line 21 on Ohio schedule of adjustments
    """

    value_type = float
    entity = TaxUnit
    label = "Certain payments related to the East Palestine train derailment"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH