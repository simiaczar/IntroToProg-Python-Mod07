# ------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# Carl Caba,<08.17.2020>,Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
objFile = None
strFileName = 'AppData.dat'
lstCustomer = []

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    with open(file_name, 'wb') as file:
        pickle.dump(list_of_data, file)
        file.close()

def read_data_from_file(file_name):
    with open(file_name, 'rb') as file:
        list_of_data = pickle.load(file)
        file.close()
        return list_of_data

# Presentation ------------------------------------ #
def new_data_to_list():
    CustomerID = int(input('Enter the customer ID: '))
    strName = str(input('Enter the name: '))
    lstCustomer = [CustomerID, strName]
    return lstCustomer

try:
    fileData = read_data_from_file(strFileName)
except FileNotFoundError as e:
    print("File not found, please try again")
    fileData = lstCustomer
except pickle.UnpicklingError as e:
    print("The file you selected is corrupt")

try:
    lstCustomer.append(new_data_to_list())
    save_data_to_file(strFileName, lstCustomer)
except ValueError as e:
    print(e)

    input("Press Enter to Exit")