import plant_planner

plot_size = get_world_size()
companion = {} #which is the best companion  
about_plot = []
season = 1

while True:
	move(North)
	plant_planner.selective_harvest(get_entity_type(),season,about_plot)
	plant_planner.what_to_plant(get_pos_x(),get_pos_y(),plot_size,season,companion)
	if get_pos_y() == plot_size-1:
		move(East)
	else: 
		continue
		