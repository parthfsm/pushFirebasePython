from firebase import firebase

FBConn = firebase.FirebaseApplication(
    'https://python-54b97.firebaseio.com/', None)


while True:

    # Ask the user to input a temperature
    temperature = 22

    # Create a dictionary to store the data before sending to the database
    data_to_upload = {
        'Temp': temperature
    }

    # Post the data to the appropriate folder/branch within your database
    result = FBConn.post('/MyTestData/', data_to_upload)

    # Print the returned unique identifier
    print(result)

# Close the serial connection
# ser.close()
