# Import Libraries
from firebase import firebase
import datetime
import time

# Establish my connection to the Firebase Database
FBConn = firebase.FirebaseApplication(
    'https://fsmorder-46bdb.firebaseio.com/', None)


while True:
    myGetResults = FBConn.get('/users/1', None)

    # Check it's contents
    print(myGetResults)
    print(time)
    # Wait 5 seconds
    time.sleep(5)


# 2019-03-27 11: 13: 07.351247
    # var time = moment().format("h:mm:ss")
