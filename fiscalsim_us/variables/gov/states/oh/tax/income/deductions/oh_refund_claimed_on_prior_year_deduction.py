from fiscalsim_us.model_api import *


class oh_refund_claimed_on_prior_year_deduction(Variable):
    """
    Line 25 on Ohio schedule of adjustments
    """

    value_type = float
    entity = TaxUnit
    label = "Refund or reimbursements from federal 1040 itemized deductions from prior year"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH
