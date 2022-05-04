import os

def main():

    directory = input("Enter the directory that you want to save the file : ")
    filename = input("Enter the filename : ")

    name = input("Enter your name : ")
    address = input("Enter your address : ")
    phone_number = input("Enter your phone number : ")


    if os.path.isdir(directory):


        writeFile = open(os.path.join(directory,filename),'w')


        writeFile.close()

        print("File contents:")

        
        readFile = open(os.path.join(directory,filename),'r')
        for line in readFile:

            print(line)

        readFile.close()

    else:

        print("Sorry that directory is not available...")

main()
