import os
from datetime import datetime

folder = ""
J_folder = ""
count = 0
j = 0

parent_dir = "E:/opencvproject/"
directory = "workbook"
parent_dir0 = "".join([parent_dir, directory])

if os.path.exists(parent_dir0):

    print("file already existed")
    for i in range(0, 11, 1):

        x = datetime.now()
        directory_1 = x.strftime(f'{"%d-%m-%Y-"}{i}{".txt"}')  # "workbook"
        path = os.path.join(parent_dir0, directory_1)
        J_folder = path

        try:

            with open(path, 'x') as fp:
                pass
        except OSError as error:
            break
            # print("all files have been created", i)

else:

    # directory = ""
    path = os.path.join(parent_dir, directory)
    os.makedirs(path)
    print("Directory '% s' created" % directory)


for j in os.listdir(parent_dir0):
    if os.path.isfile(J_folder):
        count += 1
print(f"number of file in the directory:'{parent_dir0}' is ", count)

