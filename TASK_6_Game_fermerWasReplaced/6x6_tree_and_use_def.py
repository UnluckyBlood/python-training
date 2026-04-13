# clear()

# def go_start():
# 	dx = 0 - get_pos_x()
# 	dy = 0 - get_pos_y()
# 	if dx != 0:
# 		move_raz("x", dx)
# 	if dy != 0:
# 		move_raz("y", dy)

# def proverka_na_till():
# 	if get_ground_type() == Grounds.Soil and get_entity_type() == None:
# 		till()
	
# def plant_strok(len_vert, len_horiz, who_plant, count_tiil):
# 	for i in range(len_vert):
# 		for j in range(len_horiz):
# 			for t in range(count_tiil):
# 				till()
# 			plant(who_plant)
# 			move(East)
# 		move(North)
		
# def sbor_all():
# 	for i in range(get_world_size()):
# 		for j in range(get_world_size()):
# 			while can_harvest() != True:
# 				pass
# 			harvest()
# 			move(East)
# 		move(North)
# 	go_start()
		
# def move_raz(kuda,skolko):
# 	if skolko > 0:
# 		if kuda == "x":
# 			for i in range(skolko):
# 				move(East)
# 		else:
# 			for i in range(skolko):
# 				move(North)
# 	elif skolko < 0:
# 		if kuda == "x":
# 			for i in range(-skolko):
# 				move(West)
# 		else:
# 			for i in range(-skolko):
# 				move(South)
				
# def sbor_all_random_tree():
# 	go_start()
# 	unreaped = []
# 	for i in range(get_world_size()):
# 		for j in range(get_world_size()):
# 			if can_harvest() != True:
# 				unreaped.append((get_pos_x(), get_pos_y()))
# 			else:
# 				harvest()
# 			move(East)
# 		move(North)
# 	for (target_x, target_y) in unreaped:
# 		dx = target_x - get_pos_x()
# 		dy = target_y - get_pos_y()
# 		if dx != 0:
# 			move_raz("x", dx)
# 		if dy != 0:
# 			move_raz("y", dy)
# 		while not can_harvest():
# 			proverka_na_till()
# 	go_start()
			
# plant_strok(get_world_size(),get_world_size(),Entities.Bush,1)
# sbor_all()		

# plant_strok(6,3,Entities.Carrot,1)
# sbor_all_random_tree()	