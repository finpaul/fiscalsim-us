from fiscalsim_us.model_api import *


class oh_medical_deduction(Variable):
    """
    Line 39-43 on Ohio schedule of adjustments
    """

    value_type = float
    entity = TaxUnit
    label = "All Medical Deductions"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH

    
    