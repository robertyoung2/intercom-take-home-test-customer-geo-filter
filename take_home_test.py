import json
import os
from math import sin, cos, asin, sqrt, radians

# Set values for the purpose of this script
intercom_office_lat = 53.339428
intercom_office_lng = -6.257664
accepted_distance = 100
file_name = "test_text_files/customer_errors.txt"
output_path = "output_files/"


def load_customer_data(data_file):
    """
    Function to load the provided text file (json), and return a list of python dicts in the correct format
    If data file is empty, the program will exit as there is nothing to process. Console message will be printed.
    :param data_file: filename/path pointing to the customer-data text file to be loaded
    :return: returns a list of python dictionaries, one for each valid customer json object
    """
    if (os.stat(data_file).st_size == 0):
        print("The provided data file is empty, program will now exit.")
        exit(0)

    customer_data = []
    with open(data_file) as file:
        for line in file:
            try:
                customer_data.append(json.loads(line))
            except ValueError:
                print("Decoding JSON has failed, incorrect JSON format:")
                print(line)

    return customer_data


def haversine(intercom_lat, intercom_lng, customer_lat, customer_lng):
    """
    Takes in two coordinates and calculate the greater circle distance between these two points in kilometers
    Uses the greater circle distance formula from: https://en.wikipedia.org/wiki/Great-circle_distance,
    haversine formula. This is broken into three steps for readability, a,c and the return statement.

    :param intercom_lat: Latitude of Intercoms Dublin Office
    :param intercom_lng: Longitude of Intercoms Dublin Office
    :param customer_lat: Latitude of the given customer coordinate
    :param customer_lng: Longitude of the given customer coordinate
    :return: returns the greater circle distance between two coordinates in kilometers, rounded to two decimal places
    """

    radius_earth_km = 6371
    lat_1_rads, lng_1_rads = radians(intercom_lat), radians(intercom_lng)
    lat_2_rads, lng_2_rads = radians(customer_lat), radians(customer_lng)

    diff_lat_rads = lat_1_rads - lat_2_rads
    diff_lng_rads = lng_1_rads - lng_2_rads

    a = sin(diff_lat_rads / 2) ** 2 + (cos(lat_1_rads) * cos(lat_2_rads) * sin(diff_lng_rads / 2) ** 2)
    c = 2 * asin(sqrt(a))
    answer = round(c * radius_earth_km, 2)

    return answer


def customer_distance(intercom_lat, intercom_lng, customer_data_list, distance_within):
    """
    Generates a list of customers within the accepted range, sorted by user id
    :param intercom_lat: Latitude of Intercoms Dublin Office
    :param intercom_lng: Longitude of Intercoms Dublin Office
    :param customer_data_list: List of all customers as Python dictionary objects
    :param distance_within: Accepted distance customers must be within to be invited to Intercom party
    :return: returns list of customers as dictionary objects within the accepted_distance, sorted by user_id ascending
    """
    nearby_customers = []

    for customer in customer_data_list:
        try:
            customer_lat = float(customer['latitude'])
            customer_lng = float(customer['longitude'])
            distance = (haversine(intercom_lat, intercom_lng, customer_lat, customer_lng))

            if distance < distance_within and customer not in nearby_customers:
                nearby_customers.append(customer)

        except KeyError:
            print("Empty entry detected or incorrect Key value detected:")
            print(customer)

        except ValueError:
            print("Value error, please make sure value is required format (user_id should be an int, for example)")
            print(customer, '\n')

    return sorted(nearby_customers, key=lambda item: item['user_id'])


def output_customer_list(sorted_cus, output_path_write):
    """
    :param sorted_cus: takes as input the screened and sorted customer list from function customer_distance
    :param output_path_write: define path to write output file to
    :return: generates two output files of customers, one as .txt and one as .csv, listing customers within in the
    accepted pre-set range, and sorted by ascending user_id
    """
    output_file_text = open(output_path_write + "output.txt", 'w')
    output_file_csv = open(output_path_write + "output.csv", 'w')
    output_file_csv.write('{} {} {} {}'.format("User ID", ",", "Name", "\n"))

    for customer in sorted_cus:
        output_file_text.write(str(customer) + "\n")
        output_file_csv.write('{} {} {} {}'.format(str(customer['user_id']), ',', customer['name'], '\n'))

    output_file_text.close()
    output_file_csv.close()


def execute_functions():
    """
    Executes all required functions. For a given JSON text file will create two output files, one csv and one
    JSON text containing all customers within 100km of the set coordinate, sorted in ascending order based on user_id
    """
    customer_data_list = (load_customer_data(file_name))
    sorted_cus = customer_distance(intercom_office_lat, intercom_office_lng, customer_data_list, accepted_distance)
    output_customer_list(sorted_cus, output_path)


if __name__ == '__main__':
    execute_functions()
