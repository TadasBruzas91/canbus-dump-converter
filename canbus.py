from functions import rejoined


class CanBus:
    def __init__(self, file_path):
        self.file_path = file_path
        self.can_ids = []
        self.can_messages = []

    def find_all_ids_candump(self):
        try:
            self.can_ids = []
            with open(self.file_path, "r") as f:
                for line in f:
                    if len(line) > 0:
                        can_id = line.split(" ")[2].split("#")[0]
                        if can_id not in self.can_ids and can_id:
                            self.can_ids.append(can_id)
        except:
            print("ERROR: File emty or bad path!")

    def find_all_ids_canhacker(self):
        try:
            self.can_ids = []
            with open(self.file_path, "r") as f:
                for line in f:
                    if len(line):
                        can_id = line.split(" ")[1]
                        if can_id not in self.can_ids and can_id:
                            self.can_ids.append((can_id))

        except:
            print("ERROR: File emty or bad path!")

    def find_all_messages_candump(self, can_id_req):
        try:
            self.can_messages = []
            with open(self.file_path, "r") as f:
                for line in f:
                    can_id = line.split(" ")[2].split("#")[0]
                    can_message = line.split(" ")[2].split("#")[1].replace("\n","")
                    if can_id_req == can_id:
                        self.can_messages.append(rejoined(can_message, " ").strip())
        except:
            print("ERROR: No messages found!")

    def find_all_messages_canhacker(self, can_id_req):
        try:
            self.can_messages = []
            with open(self.file_path, "r") as f:
                for line in f:
                    can_id = line.split(" ")[1]
                    can_message = line.split(" ")[8:16]
                    if can_id_req == can_id:
                        self.can_messages.append(" ".join(can_message).strip())
        except:
            print("ERROR: No messages found!")


    def show_can_ids(self):
        if(self.can_ids):
            print(f"Success found {len(self.can_ids)} CAN ID's.")
            print(self.can_ids)
        else:
            print("CAN ID's not found.")





#############      Testing !!!     ################
if __name__ == "__main__":
    can = CanBus("/home/tadas/Documents/EDC15 test drive canbus/edc15 speed.trc")
    can.find_all_ids_canhacker()
    can.find_all_messages_canhacker("588")
    for msg in can.can_messages:
        print(msg)