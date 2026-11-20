def shutdown(user_input):
    if user_input =="yes":
        print("shutting down")

    elif user_input == "no":
        print("abort shut down")

    else:
        print("sorry")

user_choice = input("do you want to shut down? (yes/no): ")
shutdown(user_choice)