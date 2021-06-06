#Packages
import random
import time
#For all the warnings you need the hp, dfn (defense) and dmg stats all setup.

yes_or_no = input("Do you want to use the sword, PISTOL, flail, watergun, ak-47 or a paper ak-47: ")
player = hp = 100 and dmg = yes_or_no
test_enemy = hp = 20 and dmg = 2
if_user_want_to_use_the_attachment = input("There's a attachment available. Would you like to use it?: ")

#The weapons
def sword():
	#The variables:
	dmg = 2
	used = False
	print("The sword deals 2 dmg")
	info_on_gun = input("Do you want info on the GUN?")

	#The main function:
	if info_on_gun == 'Yes' or 'yes':
		print("The GUN deals 3 dmg on the body but 5 dmg on the head ")
	elif yes_or_no == 'The sword' or 'the sword':
		used = True
	elif yes_or_no == 'The gun' or "the gun":
		used = True
		pistol()
	elif used == True:
		sword()
		hp = hp - dmg
	else:
		pass

def pistol():
	#The variables:
	dmg = 3

	used = False
	print("The Gun deals 3 dmg on the body but 5 dmg on the head ")
	info_on_sword = input("Do you want info on the sword?")
	if_user_want_to_use_the_attachment = input("There's a attachment available. Would you like to use it?")
	on_body_or_on_head = random.randchoice([])

	#The main function:
	if info_on_sword == 'Yes' or 'yes':
		print("The sword deals 2 dmg")
	elif yes_or_no == 'The sword' or "the sword":
		used = True
		sword()
	elif yes_or_no == 'The gun' or "the gun":
		used = True
	elif used == True:
		if on_body_or_on_head == body:
			dmg = 3
		elif on_body_or_on_head == head:
			dmg = 5
		else:
			pass
		hp = hp - dmg
	elif if_user_want_to_use_the_attachment == 'Yes' or 'yes':
		if used == True:
			attachment_on_pistol()
		else:
			pass
	else:
		pass

def attachment_on_pistol():
	def pistol():
		#The variables:
		dmg = 5
		used = False
		print("The Gun deals 5 dmg on the body but 9 dmg on the head ")
		info_on_sword = input("Do you want info on the sword?")
		on_body_or_on_head = random.randchoice([])

		#The main function:
		if info_on_sword == 'Yes' or 'yes':
			print("The sword deals 2 dmg")
		elif yes_or_no == 'The sword' or "the sword":
			sword()
		elif yes_or_no == 'The gun' or "the gun":
			used = True
		elif used == True:
			gun()
			hp = hp - dmg
		else:
			pass

def flail():
	#The variables:
	dmg = 9
	used = False
	print("The flail deals 9 dmg to the enemy and, sometimes, even the player!")
	info_on_sword = input("Do you want info on the sword?")
	info_on_gun = input("Do you want info on the GUN?")
	on_body_or_on_head = random.randchoice(body, head)
	on_player_or_on_enemy = random.randchoice(player, test_enemy)

	#The main function:
	if yes_or_no == 'The flail' or 'the flail':
		used = True
	elif yes_or_no == 'The gun' or 'the gun':
		used = True
		if if_user_want_to_use_the_attachment == 'Yes' or 'yes':
			attachment_on_pistol()
		else:
			pistol()
	elif yes_or_no == 'the sword' or 'The sword':
		used = True
		sword()
	if on_body_or_on_head == random.randchoice(body, head):
		if on_body_or_on_head == body:
			if on_player_or_on_enemy == player:
				test_enemy == time.sleep(5000)
			elif on_player_or_on_enemy == test_enemy:
				player == time.sleep(5000)
			else:
				pass
		elif on_body_or_on_head == head:
			if on_player_or_on_enemy == player:
				player == time.sleep(5000)
			elif on_player_or_on_enemy == test_enemy:
				test_enemy == time.sleep(5000)
			else:
				pass
		else:
			pass
	elif used == True:
		hp = hp - dmg
	elif used == False:
		pass
	else:
		pass

def watergun():
	#The variables:
	dmg = 1
	used = False
	print("The watergun deals 1 dmg to the enemy, but stuns BOTH the player AND the enemy")
	info_on_sword = input("Do you want info on the sword?")
	info_on_gun = input("Do you want info on the GUN?")
	info_on_flail = input("Do you want info on the flail?")
	on_test_enemy_head = random.randchoice(True, False)
	on_test_enemy_body = random.randchoice(True, False)
	test_enemy = hp = 10 and dmg = 2
	on_player_head = random.randchoice(True, False)
	on_player_body = random.randchoice(True, False)
	player = hp = 100 and dmg = watergun(dmg)

	#The main function:
	if yes_or_no == 'the sword' or 'The sword':
		used = True
		player = dmg = 2
		sword()
	elif yes_or_no == 'The pistol' or "the pistol":
		used = True
		player = dmg = 3
		pistol()
	elif yes_or_no == 'The flail' or 'the flail':
		used = True
		player = dmg = 9
		flail()
	elif yes_or_no == 'The watergun' or 'the watergun':
		used = True
		hp = hp - dmg
	elif on_player_head == True:
		time.sleep(5000)
	elif on_player_head == False:
		on_player_body = True
	elif on_player_body == True:
		on_test_enemy_head == True
	elif on_player_body == False:
		pass
	elif on_test_enemy_head == True:
		enemy = time.sleep(5000)
	elif on_test_enemy_body == True:
		on_player_head = True
	elif on_test_enemy_head == False:
		on_test_enemy_body = True
	elif on_test_enemy_body == False:
		pass
	elif used == False:
		yes_or_no
	else:
		pass

def ak47():
	#The variables:
	dmg = 15
	for_each_shot_dmg = 3
	on_enemy_head = hp = 29 and dmg = 2
	on_enemy_body = hp = 41 and dfn = 3
	on_player_head = hp = 50 and dfn = 3
	on_player_body = hp = 100 and dfn = 1
	if_user_want_to_use_the_attachment = input("There's a attachment available. Would you like to use it?")


	#The main function:
	if yes_or_no == 'The flail' or 'the flail':
		used = True
		flail()
	elif yes_or_no == 'The watergun' or 'the watergun':
		used = True
		watergun()
	elif yes_or_no == 'The gun' or "the gun":
		used = True
		if if_user_want_to_use_the_attachment == 'Yes' or 'yes':
			attachment_on_pistol()
		else:
			pistol()
	elif yes_or_no == 'The sword' or 'the sword':
		used = True
		sword()
	elif yes_or_no == 'The ak47' or "the ak47":
		used = True
		hp = hp + dfn - dmg
	elif on_player_head == True:
		time.sleep(5000)
	elif on_player_head == False:
		pass
	elif on_player_body == True:
		on_enemy_head == True
	elif on_player_body == False:
		pass
	elif on_enemy_head == True:
		enemy = time.sleep(5000)
	elif on_enemy_body == True:
		on_player_head = True
	elif on_enemy_head == False:
		pass
	elif on_enemy_body == False:
		pass
	elif used == False:
		pass
	else:
		pass

def paper_ak47():
	#The variables:
	dmg = 20
	for_each_shot_dmg = 6
	on_enemy_head = hp = 29 and dmg = 2
	on_enemy_body = hp = 41 and dfn = 3
	on_player_head = hp = 50 and dfn = 3
	on_player_body = hp = 100 and dfn = 1
	if_user_want_to_use_the_attachment = input("There's a attachment available. Would you like to use it?")

	#The main function:
	if yes_or_no == 'The flail' or 'the flail':
		used = True
		flail()
	elif yes_or_no == 'The watergun' or 'the watergun':
		used = True
		watergun()
	elif yes_or_no == 'The gun' or "the gun":
		used = True
		if if_user_want_to_use_the_attachment == 'Yes' or 'yes':
			attachment_on_pistol()
		else:
			pistol()
	elif yes_or_no == 'The sword' or 'the sword':
		used = True
		sword()
	elif yes_or_no == 'The ak47' or "the ak47":
		used = True
		hp = hp + dfn - dmg
	elif on_player_head == True:
		time.sleep(5000)
	elif on_player_head == False:
		pass
	elif on_player_body == True:
		on_enemy_head == True
	elif on_player_body == False:
		pass
	elif on_enemy_head == True:
		enemy = time.sleep(5000)
	elif on_enemy_body == True:
		on_player_head = True
	elif on_enemy_head == False:
		pass
	elif on_enemy_body == False:
		pass
	elif used == False:
		pass
	else:
		pass
