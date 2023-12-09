"""Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the mod

    Args:
        SimpleTestCase (_type_): _description_
    """

    def test_add_number(self):
        """Test adding numbers tog"""

        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    def test_subtract(self):
        res = calc.subtract(20, 15)

        self.assertEqual(res, 5)
