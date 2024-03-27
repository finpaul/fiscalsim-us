from fiscalsim_us.model_api import *


class oh_uniformed_services_deduction(Variable):
    """
    Line 29-33 on Ohio schedule of adjustments
    """

    value_type = float
    entity = TaxUnit
    label = "All Uniformed Services Deductions"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH

    
    