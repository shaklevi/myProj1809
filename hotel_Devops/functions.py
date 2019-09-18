from hotel_Devops.hotel_funcs import *


def menu(self):
    boolean = 0
    choice = input("1.Search for available rooms\n2.Search for specific date\n3.Make Invitation\n4.Cancel Invitation\n5.Add days \ rooms\n6.Search invitation")
    if choice == "1":
        hotel.find_free_rooms()
        boolean = 1
    elif choice =="2":
        requiredDate = input("Enter required date:")
        number_of_people = input("Enter number of people:")



        boolean = 1
    elif choice == "3":
        boolean = 1
    elif choice == 4:
        boolean =1
    elif choice == 5:
        boolean =1
    elif choice == 6:
        boolean =1
    elif:
        print("Enter a number between 1 and 6")