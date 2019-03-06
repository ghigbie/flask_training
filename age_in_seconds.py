def age_in_seconds():
    user_age = input("Please enter your age: ")
    age_seconds = int(user_age) *365 *24 *60 *60
    print(f"Your age in seconds is {age_seconds}.")


age_in_seconds()

