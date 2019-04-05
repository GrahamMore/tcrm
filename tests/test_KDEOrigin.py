"""
 Title: KDEOriginTestCase.py
 Author: Nariman Habili, nariman.habili@ga.gov.au
 CreationDate: 2006-12-13
 Description: Unit testing module for KDEOrigin.py

 Version: $Rev: 563 $

 $Id: TestKDEOrigin.py 563 2007-10-24 02:52:40Z carthur $
"""
import os, sys
import pickle
import unittest
import numpy as np
from tests import NumpyTestCase, pathLocate

try:
    pass
except:
    from unittests import pathLocate

# Add parent folder to python path
unittest_dir = pathLocate.getUnitTestDirectory()
sys.path.append(pathLocate.getRootDirectory())
from StatInterface import KDEOrigin
from Utilities.files import flStartLog
from Utilities.singleton import forgetAllSingletons

class TestKDEOrigin(NumpyTestCase.NumpyTestCase):

    def setUp(self):
        kdeType = 'Epanechnikov'
        gridLimit={'xMin':70, 'xMax':180, 'yMin':-36, 'yMax':0}
        kdeStep = 0.1
        pkl_file = open(os.path.join(unittest_dir, 'test_data', 'kde_origin_lonLat.pck'),'rb')
        lonLat = pickle.load(pkl_file,encoding='latin')
        self.kdeOrigin = KDEOrigin.KDEOrigin(None, gridLimit, kdeStep, lonLat)
        pkl_file.close()

    def tearDown(self):
        forgetAllSingletons()

    def test_GenerateKDE(self):
        """Testing GenerateKDE for 2D data"""
        pkl_file = open(os.path.join(unittest_dir, 'test_data', 'kdeOrigin_xyz.pck'), 'rb')
        xp = pickle.load(pkl_file,encoding='Latin').astype(np.float)
        yp = pickle.load(pkl_file,encoding='Latin').astype(np.float)
        zp = pickle.load(pkl_file,encoding='Latin').astype(np.float)

        x, y, z = self.kdeOrigin.generateKDE()
        self.numpyAssertAlmostEqual(xp, x)
        self.numpyAssertAlmostEqual(yp, y)
        self.numpyAssertAlmostEqual(zp, z)

if __name__ == "__main__":
    flStartLog('', 'CRITICAL', False)
    testSuite = unittest.makeSuite(TestKDEOrigin,'test')
    unittest.TextTestRunner(verbosity=2).run(testSuite)
