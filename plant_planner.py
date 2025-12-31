tree = 3
sunflower = 3

def what_to_plant(x,y,plot_size):
	if (x<tree):
		plant_tree_grass()
	elif (x<plot_size-sunflower):
		plant_pumpkin_cactus(y,plot_size)
	else:
		plant_sunflower()	

def plant_grass():
	if get_ground_type() == Grounds.Soil:
		till()

def plant_tree_grass():
	if((get_pos_y()+get_pos_x())%2==0):
		plant_grass()
	else:
		plant(Entities.Tree)

def plant_pumpkin_cactus(y,plot_size):
	
	if (y < plot_size-sunflower-tree):
		plant(Entities.Pumpkin)
	else:
		plant(Entities.Cactus)

def plant_sunflower():
	if((get_pos_y()+get_pos_x())%2==0):
		plant(Entities.Sunflower)
	else:
		plant(Entities.Carrot)
	
def selective_harvest(type):
	if (type == Entities.Pumpkin):
		can_harvest_pumpkin()
	elif (type == Entities.sunflower):
		can_harvest_sunflower()
	else: 
		harvest()
		
def can_harvest_pumpkin():
	if (measure()>8000000):
		harvest()
	else:
		pass
		
def can_harvest_sunflower():
	if (measure()>=12):
		harvest()
	else:
		pass	