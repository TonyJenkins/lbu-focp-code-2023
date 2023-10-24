if __name__ == '__main__':

    name = input("Hello. What is your name? ")
    if name == "" or str.isspace(name) == True:
        print("Well met, Mysterious Stranger! How shall we learn your name?")
    else:
        print(f"Well met, {name} It is good to meet you!")


#COMMENT
#this starts to consider further use cases where errors could be inputted (multiple spaces for the name)
# == , is (which to use?)