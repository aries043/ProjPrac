import returnAddress

def find():
    print("Please enter your current location.")
    curloc = input()
    return returnAddress.getloc(curloc)
