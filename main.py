import os
from datetime import datetime

folder = ""
J_folder = ""
file_count = 0
j = 0
exist = bool
count_start_file = 0
count_total_file = 331


parent_dir = "E:/opencvproject/"
directory = "workbook"
parent_dir0 = "".join([parent_dir, directory])

if os.path.exists(parent_dir0):

    print("file already existed")
    for i in range(count_start_file, count_total_file, 1):

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


for path_dir, folder_dir, total_file in os.walk(parent_dir0):
    file_count += len(total_file)
print(f"number of file in the directory:'{parent_dir0}' is ", file_count)



