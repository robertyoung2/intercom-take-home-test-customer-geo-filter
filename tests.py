# Import modules and all functions from the main python script
import unittest
import filecmp
from take_home_test import load_customer_data, haversine, customer_distance, output_customer_list=

# Paths for opening and writing files for unit testing
test_file_path = 'test_text_files/'
output_path = 'test_text_files/test_output/'


class TestLoadCustomerData(unittest.TestCase):

    def test_correct_customer_format(self):
        """
        Test json objects in text file are converted to Python dict and added to a list
        """
        test_customers = test_file_path + 'test_customers.txt'
        customer_data = load_customer_data(test_customers)
        answer = [{'latitude': '52.986375', 'user_id': 12, 'name': 'Christina McArdle', 'longitude': '-6.043701'}]

        self.assertEqual(customer_data, answer)

    def test_handles_erroneous_file_text(self):
        """
        Tests the script to ensure the output is correct, even for JSON data objects which are poorly formed (code
        should skip these). At the end, the output
        will only be those that are valid customer objects.
        """

        customer_errors = test_file_path + 'customer_errors.txt'
        customer_data = load_customer_data(customer_errors)
        print(customer_data)
        answer = [{'latitude': '53.2451022', 'user_id': 4, 'name': 'Ian Kehoe', 'longitude': '-6.238335'},
                  {'latitude': '53.1302756', 'user_id': 5, 'name': 'Nora Dempsey', 'longitude': '-6.2397222'},
                  {'latitude': '53.008769', 'user_id': 11, 'name': 'Richard Finnegan', 'longitude': '-6.1056711'},
                  {'latitude': '53.74452', 'user_id': 29, 'name': 'Oliver Ahearn', 'longitude': '-7.11167'}]

        self.assertEqual(customer_data, answer)

    def test_empty_data(self):
        """
        Check the program exits if the provided data file is empty
        """
        with self.assertRaises(SystemExit) as cm:
            load_customer_data(test_file_path + 'empty_file.txt')

        self.assertEqual(cm.exception.code, 0)


class TestHaversine(unittest.TestCase):

    def test_correct_distance(self):
        """
        Test correct distance is calculated in haversine function between Enniskerry and Dun Laoghaire using
        Google Maps calculated distance as the reference value to be asserted against
        """
        coords_1 = (53.192807, -6.170260)
        coords_2 = (53.293867, -6.131701)
        google_maps_calc_distance = 11.53
        haversine_calc_distance = haversine(coords_1[0], coords_1[1], coords_2[0],coords_2[1])

        self.assertEqual(google_maps_calc_distance, haversine_calc_distance)


class TestCustomerDistance(unittest.TestCase):

    def test_customer_distance(self):
        """
        Test customers with a distance greater than 100km are excluded, and customers within 100km are included.
        Uses a new test set of customers from around Dublin and the United Kingdom
        """
        coords_1 = (53.192807, -6.170260)
        accepted_distance = 100
        customer_distance_test = load_customer_data(test_file_path + 'customer_distance.txt')
        customer_distance_solution = load_customer_data(test_file_path +
                                                        'test_solutions/customer_distance_solution.txt')
        customer_list = customer_distance(coords_1[0], coords_1[1], customer_distance_test, accepted_distance)

        self.assertEqual(customer_distance_solution, customer_list)

    def test_customer_distance_sorted(self):
        """
        Test that the returned customer list is in ascending order based on user_id
        Loops over the customer list and compares the current user_id value with the next user_id value
        """
        coords_1 = (53.192807, -6.170260)
        accepted_distance = 100
        customer_list = load_customer_data(test_file_path + 'customers.txt')
        customer_sorted_list = customer_distance(coords_1[0], coords_1[1], customer_list, accepted_distance)

        flag = False
        i = 0
        while i < len(customer_sorted_list) - 1:
            if customer_sorted_list[i]['user_id'] <= customer_sorted_list[i+1]['user_id']:
                flag = True
                i += 1
            else:
                flag = False
                break

        self.assertEqual(True, flag)

    def test_duplicate_entry(self):
        """
        Test that no duplicate entries are added to the list
        """
        coords_1 = (53.192807, -6.170260)
        accepted_distance = 100
        duplicate_list = [{"latitude": "54.0894797", "user_id": 8, "name": "Eoin Ahearn", "longitude": "-6.18671"},
                          {"latitude": "54.0894797", "user_id": 8, "name": "Eoin Ahearn", "longitude": "-6.18671"}]
        correct_output = [{"latitude": "54.0894797", "user_id": 8, "name": "Eoin Ahearn", "longitude": "-6.18671"}]
        generated_list = customer_distance(coords_1[0], coords_1[1], duplicate_list, accepted_distance)

        self.assertEqual(correct_output, generated_list)


class TestOutputCustomerList(unittest.TestCase):

    def test_text_correct(self):
        """
        Does a byte by byte comparison of a solution output and a produced output during testing and asserts if the two
        files are the same in terms of content
        """
        file_test_customers_sorted = [{'latitude': '53.2451022', 'user_id': 4, 'name':
            'Ian Kehoe', 'longitude': '-6.238335'}, {'latitude': '53.1302756', 'user_id': 5, 'name':
            'Nora Dempsey', 'longitude': '-6.2397222'}, {'latitude': '53.1229599', 'user_id': 6, 'name':
            'Theresa Enright', 'longitude': '-6.2705202'}]

        output_customer_list(file_test_customers_sorted, output_path)
        file_solution = test_file_path + 'test_solutions/output_solution.txt'
        file_output = test_file_path + 'test_output/output.txt'
        check = (filecmp.cmp(file_solution, file_output))

        self.assertEqual(True, check)

    def test_csv_correct(self):
        """
        Does a byte by byte comparison of a solution output and a produced output during testing and asserts if the two
        files are the same in terms of content
        """
        file_test_customers_sorted = [{'latitude': '53.2451022', 'user_id': 4, 'name':
            'Ian Kehoe', 'longitude': '-6.238335'}, {'latitude': '53.1302756', 'user_id': 5, 'name':
            'Nora Dempsey', 'longitude': '-6.2397222'}, {'latitude': '53.1229599', 'user_id': 6, 'name':
            'Theresa Enright', 'longitude': '-6.2705202'}]

        output_customer_list(file_test_customers_sorted, output_path)
        file_solution = test_file_path + 'test_solutions/output_solution.csv'
        file_output = test_file_path + 'test_output/output.csv'
        check = (filecmp.cmp(file_solution, file_output))

        self.assertEqual(True, check)


if __name__ == '__main__':
    unittest.main()
