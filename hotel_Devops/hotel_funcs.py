import datetime

class hotel:
    roomfiles  = [
        "C:\\Users\\ShaharL\Desktop\\room1.txt",
        "C:\\Users\\ShaharL\Desktop\\room2.txt",
        "C:\\Users\\ShaharL\Desktop\\room3.txt",
        "C:\\Users\\ShaharL\Desktop\\room4.txt"
    ]
    def find_free_rooms(self):
        print("Finding free rooms")
        room1 = open(roomfiles[0],"r")
        room2 = open(roomfiles[1], "r")
        room3 = open(roomfiles[2], "r")
        room4 = open(roomfiles[3], "r")
        print("Available dates for a room for 2 adults:", str(room1.read()))
        print("Available dates for a room for 2 adults:", str(room2.read()))
        print("Available dates for a room for 3 adults:", str(room3.read()))
        print("Available dates for a room for 3 adults:", str(room4.read()))
        room1.close()
        room2.close()
        room3.close()
        room4.close()
        def checkIfRoomIsAvailable(room_index,requiredDate):
            with open(roomfile[room_index-1], "r") as openfileRoom1:
                for line in openfileRoom1:
                    if datetime(line) == datetime(requiredDate):
                       return True
                return False


        def invitation(self, requiredDate, numberOfPeople):
            if numberOfPeople == 2:
                index=1
                if checkIfRoomIsAvailable(index,requiredDate) == True:
                    print(f"room {0} is available in date: {1}",index, requiredDate)
                index=2
                elif checkIfRoomIsAvailable(index,requiredDate) == True:
                    print(f"room {0} is available in date: {1}",index, requiredDate)
            elif numberOfPeople == 3:
                index=3
                if checkIfRoomIsAvailable(index,requiredDate) == True:
                    print(f"room {0} is available in date: {1}",index, requiredDate)
                index=4
                elif checkIfRoomIsAvailable(index,requiredDate) == True:
                    print(f"room {0} is available in date: {1}",index, requiredDate)
