from fiscalsim_us.model_api import *


class salt_deduction(Variable):
    value_type = float
    entity = TaxUnit
    label = "SALT deduction"
    unit = USD
    documentation = "State and local taxes paid plus real estate tax deduction from taxable income."
    definition_period = YEAR
    reference = "https://www.law.cornell.edu/uscode/text/26/164"

    def formula(tax_unit, period, parameters):
        salt_amount = add(
            tax_unit,
            period,
            ["sales_or_prior_year_state_and_local_income_tax_paid", "real_estate_taxes"],
        )
        salt = parameters(
            period
        ).gov.irs.deductions.itemized.salt_and_real_estate
        cap = salt.cap[tax_unit("filing_status", period)]
        return min_(cap, salt_amount)
