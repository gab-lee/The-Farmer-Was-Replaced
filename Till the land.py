#Till the land

exception = 0

clear()
for i in range (exception):
		move(East)
for i in range (get_world_size()-exception):
	for i in range(get_world_size()):
		till()
		move(North)
	move(East)
	
		