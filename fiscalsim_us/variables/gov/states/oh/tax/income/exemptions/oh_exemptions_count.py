from fiscalsim_us.model_api import *


class oh_exemptions_count(Variable):
    value_type = float
    entity = TaxUnit
    label = "Number of Ohio exemptions"
    definition_period = YEAR
    reference = "https://tax.ohio.gov/static/forms/ohio_individual/individual/2023/it1040-sd100-instructionbooklet.pdf"
    defined_for = StateCode.OH

    adds = [
        "head_spouse_count",
        "tax_unit_dependents",
    ]