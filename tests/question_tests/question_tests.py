#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config, get_bonus_pay_amount
from src.question_b.question_b import get_random_number
from src.question_c.question_c import get_fahrenheit
from src.question_d.question_d import get_miles_per_hour

class Test_Config(unittest.TestCase):


    def test_question_a_config(self):
        self.assertEqual(True, test_config())
        self.assertEqual('Invalid Arguments', get_bonus_pay_amount(-1))
        self.assertEqual(36, get_bonus_pay_amount(600))
        self.assertEqual(10, get_bonus_pay_amount(200))
        self.assertEqual(70, get_bonus_pay_amount(1000))
        self.assertEqual(120, get_bonus_pay_amount(1500))
        self.assertEqual('Invalid Arguments', get_bonus_pay_amount(2000))

    def test_question_b_config(self):
        self.assertEqual(get_random_number())

    def test_question_c_config(self):
        self.assertEqual(32, get_fahrenheit(0))

    def test_question_d_config(self):
        self.assertEqual(19.883872, get_miles_per_hour(32, 60))
        

    



