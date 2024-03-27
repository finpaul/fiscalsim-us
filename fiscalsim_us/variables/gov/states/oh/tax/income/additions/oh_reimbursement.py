from fiscalsim_us.model_api import *


class oh_reimbursement(Variable):
    """
    Line 7 on Ohio schedule of adjustments
    """

    value_type = float
    entity = TaxUnit
    label = "Reimbursement of expenses previously deducted on an Ohio income tax return"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH