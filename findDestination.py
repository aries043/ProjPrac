import returnAddress

def find():
    print("Please enter your destination.")
    dstloc = input()
    return returnAddress.getloc(dstloc)
