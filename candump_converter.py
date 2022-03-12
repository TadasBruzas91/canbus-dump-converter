import sys
from canbus import CanBus

args = sys.argv[1:]

help_message = """
************ CAN BUS DUMP CONVERTER ************
            -h, --help    print available commands
            -p, --path    file path
            -t, --type    file type (from CANDUMP or from CANHACKER)
        """

try:
    if args[0].lower() == "-h" or args[0].lower() == "--help":
        print(help_message)
except:
    pass


try:
    file_path = [args[index + 1] for index, item in enumerate(args) if item.lower() == "-p" or item.lower() == "--path"][0]
except:
    print("ERROR: File path not found!")
    print(help_message)
    sys.exit(1)
    

try:
    file_type = [args[index + 1] for index, item in enumerate(args) if item.lower() == "-t" or item.lower() == "--type"][0]
except:
    print("ERROR: File type not found!")
    print(help_message)
    sys.exit(1)
    

can = CanBus(file_path)

if file_type == "CANDUMP":
    can.find_all_ids_candump()

if file_type == "CANHACKER":
    can.find_all_ids_canhacker()

can_data_formated = []

for col_index, can_id in enumerate(can.can_ids):

    if len(can_data_formated) <= col_index:
        can_data_formated.append([])
    can_data_formated[col_index].append(can_id)

    if file_type == "CANDUMP":
        can.find_all_messages_candump(can_id)

    if file_type == "CANHACKER":
        can.find_all_messages_canhacker(can_id)

    for row_index, can_message in enumerate(can.can_messages):
        can_data_formated[col_index].append(can_message)
    

with open("output/formatted_canbus_messages_for_excel.txt", "w") as f:
    biggest_list = 0
    for indx,item in enumerate(can_data_formated):
        if len(item) > biggest_list:
            biggest_list = len(item)
    
    biggest_list -= 1

    for i in range(0,biggest_list):
        for j in range(0, len(can_data_formated)-1):
            try:
                f.write(can_data_formated[j][i]+",")
            except:
                f.write(",")
        f.write("\n")