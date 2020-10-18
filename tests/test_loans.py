import numpy as np
import unittest
from loan_optimizer.loans import Loan


class TestLoan(unittest.TestCase):

    def setUp(self):
        self.loan = Loan(0.01, 200000)

    def test_period(self):

        np.testing.assert_array_almost_equal(
            self.loan.compute_period(2000),
            8.744571)

    def test_clearence(self):
        clearence = self.loan.compute_clearence(2000)
        self.assertTupleEqual(clearence.shape, (9, ))
        self.assertEqual(clearence.sum(), self.loan.princial)

    def test_interest(self):
        interest = self.loan.compute_interest(2000)
        self.assertTupleEqual(interest.shape, (9, ))
