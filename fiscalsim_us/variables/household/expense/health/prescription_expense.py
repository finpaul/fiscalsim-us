from fiscalsim_us.model_api import *


class prescription_expense(Variable):
    value_type = float
    entity = Person
    label = "Prescription expenses"
    unit = USD
    definition_period = YEAR
