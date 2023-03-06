import os
from datetime import datetime

folder = ""
J_folder = ""
count = 0

for i in range(0, 11, 1):
    # get the current date and time
    x = datetime.now()
    # let's create our path where we want it to be located
    parent_dir = "E:/opencvproject/workbook/"
    folder = parent_dir
    # let's create our directory/folder
    directory = x.strftime(f'{"%d-%m-%Y-"}{i}{".txt"}')  # "workbook"
    # path
    path = os.path.join(parent_dir, directory)
    J_folder = path

    try:
        # let's create it
        # os.makedirs(path)
        print("Directory '% s' created" % directory)
    except OSError as error:
        print("file already existed")

    with open(path, 'x') as fp:
        pass

print("all files have been created", i)

for j in os.listdir(folder):
    if os.path.isfile(J_folder):
        count += 1
print('number of file', count)

