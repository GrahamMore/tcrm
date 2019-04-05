"""
Test random number generation extensions

FIXME: Test additional variates available through the Random module
"""

import unittest
import numpy as np

from numpy.testing import assert_almost_equal
from Utilities.tcrandom import Random as old_Random
from Utilities.tcrandom_randgen import Random as new_Random


class TestRandom(unittest.TestCase):

    def setUp(self):
        self.reference = old_Random(1)
        self.target = new_Random(1)


    def testcauchy(self):
        """Testing logistic variates"""
        bins = np.linspace(0,1,100)
        mu = 1
        sigma = 1
        result = [self.target.cauchyvariate(mu, sigma) for x in np.arange(1,1_000_000)]
        result_hist = np.histogram(result,bins)
        reference = [self.reference.cauchyvariate(mu, sigma) for x in np.arange(1,1_000_000)]
        ref_hist = np.histogram(reference,bins)
        np.testing.assert_almost_equal(np.zeros(99),1- result_hist[0]/ref_hist[0],decimal=1)

    # def testuniform(self):
    #     """Testing logistic variates"""
    #     bins = np.linspace(0,1,100)
    #     result = [self.prng.rand() for x in np.arange(1,100000)]
    #     result_hist = np.histogram(result,bins)
    #     reference = [Random for x in np.arange(1,100000)]
    #     ref_hist = np.histogram(reference,bins)
    #     np.testing.assert_almost_equal(np.zeros(99),(ref_hist[0]- result_hist[0])/1000,decimal=1)






if __name__ == '__main__':
    unittest.main()
