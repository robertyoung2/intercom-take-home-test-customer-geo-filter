# 1. Take Home Test - Brief

1. Technical problem

We have some customer records in a text file (customers.txt) -- one customer per line, JSON lines formatted. We want to 
invite any customer within 100km of our Dublin office for some food and drinks on us. Write a program that will read 
the full list of customers and output the names and user ids of matching customers (within 100km), sorted by User ID 
(ascending).

# 2. Solution

This code has been written using a functional/procedural approach to solving the problem rather than an object-orientated
approach. The reasons for this are as follows:

* It was a simple task with respect to input/output, OOP would have added a layer of complexity not required for such 
a task.
* We are dealing with JSON objects, which represented customers, there was no variation on this class, such as perhaps
'Intercom Employees'.
* No methods to interact with and change the provided customer data were required.
* Procedural code is more efficient, and if written correctly, easier to maintain.
* The code itself is static, and bar perhaps the distance range, or the intercom Dublin office geo-coordinates,
is not intended to change over time. 

The code itself will handle the major error cases that may occur when given an input file. If any one customer JSON object
in the file is incorrect, a console log will be printed stating the error and the offending object, and the script will continue
with processing any remaining valid objects in the file.

Should a JSON key or value be incorrect, such as a user_id not be a number, but instead characters such as 'aaa',
the code will again raise an error, and continue to process any valid objects.

Should a provided data file be empty, the user will be informed and the script will exit.


# 3. Project Structure Overview

In the root of the project folder there are the following files:

* take_home_test.py - this is the main python script containing all the functionality to solve the given problem.
* test.py - this is where all the unit tests for take_home_test.py are contained.
* requirements.txt - this is the requirements file to be installed for the Python virtual environment.
* customers.txt - this is the text file containing the customer JSON data to be processed.

### Output Files Directory

output_files - there are two files in here, one in csv format and the other in text containing JSON objects, similar 
to the customer text file provided for this problem. These two files are generated on execution of the code.
The files comprise the solution to the given problem. The csv is human/spreadsheet readable, giving only the customer name 
user_id. The JSON file contains all the customer information. This are only customers within 100km of Intercoms Dublin office,
sorted in ascending order of user id.

There is one other directory in the project root, test_text_files. This directory comprises of files and folders with solutions 
and text files I have manipulated,
such as empty files, or missing data, to use when running the unit tests to check robust performance.


# 4. Software and Requirements

This problem has been solved using the language Python. If you are using a Mac or Linux, it should already be 
pre-installed. You can check this by entering:

```
python --version
```

on the command line. This code was written using Python 3, so please make sure the version runnning on your computer is 
3 or above if you intend to test it. There is a good article [here](https://wsvincent.com/install-python3-mac/) on how
to do so. 

While no additional packages are required to run this script 
bar the core packages which come with Python, a requirements file has been provided to emulate the virtual environment 
used during development. This is the file requirements.txt.

To create a virtual environment, activate it and install the required packages run the following commands from the root of the 
directory (where requirements.txt is).

```
python3 -m venv venv_ryoung
source venv_ryoung/bin/activate
pip install -r requirements.txt
```

The virtual environment should now be created, activated, and the dependencies in the requirements.txt file installed.

You are now ready to run the Python code.

# 5. Entry Point - Python Function

Once the venv has been installed using requirements.txt, and the virtual environment activated, 
the python script, take_home_test.py may be run. To do this, first ensure you are in the same directory as where the script is
stored, and then, from the command line execute the following command.

```
python take_home_test.py
```

This will execute the script, and generate the results in output_files folder.


# 6. Entry Point - Unit Tests

The unit tests for all functions in the script are contained in the file, tests.py. As before, ensure your directory 
location is where tests.py is stored. To run the unit tests, from the command line, enter the following command:

```
python tests.py -b
```

For reference, the '-b' statement hides any messages sent to the console from the main function. If you would like to see 
these when running the unit tests, simply remove the '-b' from the command.