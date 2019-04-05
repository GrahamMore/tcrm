"""
:mod:`tcrandom` -- extended version of Python's :class:`random` library
=======================================================================

.. module: tcrandom
    :synopsis: Provides additional random variates beyond those in the `random` libray.
               - logisticvariate
               - cauchyvariate

.. moduleauthor:: Craig Arthur <craig.arthur@ga.gov.au>
.. |mu| unicode:: U+003BC .. GREEK SMALL LETTER MU
.. |sigma|  unicode:: U+003C3 .. GREEK SMALL LETTER SIGMA
.. |gamma|  unicode:: U+003B3 .. GREEK SMALL LETTER GAMMA

"""
import random
import randomgen
from randomgen import RandomGenerator,PCG64,MT19937
import math
from scipy.special import nctdtrit, ndtri

#pylint: disable-msg=R0904

class Random(RandomGenerator):
    """
    An extension of the standard :mod:`random` library to
    allow sampling from additional distributions.

    """

    def __init__(self, value=None):
        RNG = PCG64(value)
        super().__init__(RNG)


    def cauchyvariate(self, mu, sigma):
        """
        Random variate from the Cauchy distribution.

        :param float mu: Location parameter.
        :param float sigma: Scale parameter (|sigma| > 0)

        :returns: A random variate from the Cauchy distribution.

        """
        u1 = self.rand()#provides the number from the random gen.
        if sigma <= 0.0:
            raise ValueError("Invalid input parameter: `sigma` must be positive")
        return mu + sigma * math.tan(math.pi * (u1 - 0.5))

    def nctvariate(self, df, nc, mu=0.0, sigma=1.0):
        """
        Random variate from the non-central T distribution.

        :param float df: degrees of freedom for the distribution.
        :param float nc: non-centrality parameter.
        :param float mu: Location parameter.
        :param float sigma: Scale parameter.

        :returns: A random variate from the non-central T distribution.
        """
        if df <= 0.0:
            raise ValueError("Invalid input parameter: `df` must be positive")
        if sigma <= 0.0:
            raise ValueError("Invalid input parameter: `sigma` must be positive")

        u1 = self.rand()
        return mu + sigma * nctdtrit(df, nc, u1)

    def lognormvariate(self, xi, mu=0.0, sigma=1.0):
        """
        Random variate from the lognormal distribution.
        
        :param float xi: Shape parameter
        :param float mu: Location parameter
        :param float sigma: Scale paramter (|sigma| > 0)
        
        :returns: A random variate from the lognormal distribution
        """
        if xi <= 0.0:
            raise ValueError("Invalid input parameter: `xi` must be positive")
        if sigma <= 0.0:
            raise ValueError("Invalid input parameter: `sigma` must be positive")

        u1 = self.rand()
        return mu + sigma * math.exp(xi * ndtri(u1))
