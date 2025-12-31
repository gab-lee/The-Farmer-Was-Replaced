import plant_planner

plot_size = get_world_size()

while True:
	move(North)
	plant_planner.selective_harvest(get_entity_type())
	plant_planner.what_to_plant(get_pos_x(),get_pos_y(),plot_size)
	if get_pos_y() == plot_size-1:
		move(East)
	else: 
		continue
		