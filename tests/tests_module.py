import unittest
from test_models.test_base_model import TestBaseModel


if __name__ == "__main__":
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestBaseModel)
    suite = unittest.TestSuite([suite1])
    unittest.TextTestRunner().run(suite)