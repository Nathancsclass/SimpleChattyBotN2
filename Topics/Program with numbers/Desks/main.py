# put your python code here
group_1 = abs(int(input()))
group_2 = abs(int(input()))
group_3 = abs(int(input()))
room_1 = (group_1 // 2) + (group_1 % 2)
room_2 = (group_2 // 2) + (group_2 % 2)
room_3 = (group_3 // 2) + (group_3 % 2)
desks = room_1 + room_2 + room_3
print(desks)
