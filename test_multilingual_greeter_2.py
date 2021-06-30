from unittest import TestCase, mock
import multilingual_greeter_v2

class Multi_Greeter_2(unittest.TestCase):

    @mock.patch(multilingual_greeter_v2.admin_or_user, return_value = 1)
    def test_admin_or_user(self):
        result = multilingual_greeter_v2.admin_or_user()
        expected = 
        self.assertEqual(result, 1)

    def test_admin_mode(self):
        result = multilingual_greeter_v2
