import os

folders = input("please provide list of folder names with spaces in between").split()

for folder in folders:

    try:
        files=os.listdir(folder)        #searching for folder in the directories given in the input
    except FileNotFoundError:
        print("Please provide a valid folder name")
        continue
    except PermissionError:
        break


    print("listing files for the folder" + folder)

    # print(files)

    for file in files:
        print(file)

# exception hnadling 
