from fiscalsim_us.model_api import *


class oh_taxable_refunds_deduction(Variable):
    """
    Line 14 on Ohio schedule of adjustments
    """

    value_type = float
    entity = TaxUnit
    label = "Taxable refunds, credits, or offsets of state and local income taxes"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH

    
    