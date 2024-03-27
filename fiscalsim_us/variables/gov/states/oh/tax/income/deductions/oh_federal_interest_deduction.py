from fiscalsim_us.model_api import *


class oh_federal_interest_deduction(Variable):
    """
    Line 23 on Ohio schedule of adjustments
    """

    value_type = float
    entity = TaxUnit
    label = "Federal interest and dividends exempt from state taxation"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.OH

    def formula(tax_unit, period, parameters):
        deduction = (tax_unit, period, ["tax_exempt_interest_income"])

        return deduction