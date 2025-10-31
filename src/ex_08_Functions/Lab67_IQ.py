def f1():
    print("Welcome")

    def f2():
        print("Hi")

    f2()
f1()

     #greet Saurav()

#def greet_Saurav():
 #   print("Hi, Saurav")


def validate_status_code(response_code):
    if response_code == 200:
        print("Request is success")
    else:
        print("Error is the request")

validate_status_code(400)
validate_status_code(300)
validate_status_code(response_code=200)
validate_status_code(input("Enter your status code"))