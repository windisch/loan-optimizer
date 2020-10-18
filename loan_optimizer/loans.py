import numpy as np


class Loan(object):

    def __init__(self, interest_rate, principal):
        """

        """

        self.interest_rate = interest_rate
        self.annuity_factor = 1 + self.interest_rate
        self.princial = principal

    def compute_period(self, annuity_monthly):

        R = annuity_monthly * 12
        return (
            - np.log(1-self.interest_rate*self.princial/R) / np.log(self.annuity_factor)
        )

    def calculate(self, annuity_monthly, period=None):

        clearence = self.compute_clearence(annuity_monthly, period=period)
        interest = self.compute_interest(annuity_monthly, period=period)

        return interest, clearence

    def compute_clearence(self, annuity_monthly, periods=None):

        if periods is None:
            period_max = int(np.ceil(self.compute_period(annuity_monthly)))
        else:
            period_max = periods

        clearence = np.array([self._compute_clearence_in_period(
            annuity_monthly=annuity_monthly,
            period=p) for p in range(1, period_max + 1)
        ])
        if clearence.sum() > self.princial:
            clearence[-1] = clearence[-1] - (clearence.sum() - self.princial)
        return clearence

    def compute_interest(self, annuity_monthly, periods=None):
        clearence = self.compute_clearence(annuity_monthly, periods=periods)

        annuity_yearly = 12*annuity_monthly
        interest = annuity_yearly - clearence

        if periods is None:

            n_months = np.ceil(clearence[-1] / annuity_monthly)
            annunity_last_year = n_months * annuity_monthly

            interest [-1] = annunity_last_year - clearence[-1]
        return interest


    def _compute_clearence_in_period(self, annuity_monthly, period):
        annuity_yearly = 12*annuity_monthly

        return (
            annuity_yearly-self.princial*self.interest_rate
        )*(
            self.annuity_factor**period
        )






