#number of columns dedicated to the polyculture (grass,bush,tree,carrot)
polyculture_col = 3
#number of collumns dedicated to sunflowers
sunflower = 3 

def what_to_plant(x,y,plot_size,season,companion):
	if season == 1:
		if ((x,y) not in companion):
			plant_tree_grass_bush_carrot(x,y)
		else:
			plant(companion[(x,y)])
		plant_type, xy = get_companion()   # a = first element, b = second element
		companion[xy] = plant_type                 # key is second, value is first
	else: 
		plant_sunflower()	

def plant_grass():
	plant(Entities.grass)

def plant_tree_grass_bush_carrot(x,y):
	if((x+y)%3==0):
		plant_grass()
	elif ((x+y+1)%3==0):
		plant_carrot()
	else:
		plant(Entities.Tree)

def plant_carrot():
	plant(Entities.Carrot)

def plant_pumpkin_cactus(y,plot_size):
	
	if (y < plot_size-sunflower-polyculture_col):
		plant(Entities.Pumpkin)
	else:
		plant(Entities.Cactus)

def plant_sunflower():
	plant(Entities.Sunflower)

#Functions below help to selectively harvest crops

def selective_harvest(type,about_plot,season):
	if (type == Entities.Pumpkin):
		can_harvest_pumpkin()
	elif (type == Entities.sunflower):
		can_harvest_sunflower(about_plot)
	else: 
		harvest()
		
def can_harvest_pumpkin():
	if (measure()>8000000):
		harvest()
	else:
		pass
		
def can_harvest_sunflower(about_plot):
	#8x bonus if the sunflower harvested is the biggest sunflower && there are at least 10 sunflowers
	if (measure()==15): 
		#The max number of petals a sunflower can have is 15
		harvest()
	else:
		quick_print(about_plot)