from datetime import datetime
import pywhatkit

def parse_time():
    time = input("Enter when to send (hh:mm): ")

    try:
        # Parse the input time string into a datetime object
        time_object = datetime.strptime(time, '%H:%M')

        # Extract hour and minute components
        hour = time_object.hour
        minute = time_object.minute

        # Return the hour and minute values
        return True, hour, minute
    
    except ValueError:
        print("Please input the right time format!")
        parse_time()

who = input("Send text to number or group (N/g): ")

if who.upper() == "N": 
    # Send message to a contact
    # Parse the input time string
    valid, hour, minute = parse_time()
    number = input("Enter phone number (+62): ")
    message = input("Enter your message: ")
    
    try:
        pywhatkit.sendwhatmsg(number, message, hour, minute, 30, True, 5)
        print("Send message success!")
    except:
        print("Send message fail!")

elif who.lower()== "g":
    # Send message to a group
    # Parse the input time string
    valid, hour, minute = parse_time()
    group_id = input("Enter group id: ")
    message = input("Enter your message: ")

    try:
        pywhatkit.sendwhatmsg_to_group(group_id, message, hour, minute, 30, True, 5)
        print("Send message success!")
    except:
        print("Send message fail!")