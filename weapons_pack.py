#Packages
import random
import time
#For all the warnings you need the hp, dfn (defense) and dmg stats all setup.


def dmg(yes_or_no, sword, pistol, flail, watergun, ak47, paper_ak47):
	#a, b, c, d, e, f = sword, pistol, flail, watergun, ak47, paper_ak47
	if yes_or_no == 'a':
		return sword['dmg']
	elif yes_or_no == 'b':
		return pistol['dmg']
	elif yes_or_no == 'c':
		return flail['dmg']
	elif yes_or_no == 'd':
		return watergun['dmg']
	elif yes_or_no == 'e':
		return ak47['dmg']
	elif yes_or_no == 'f':
		return paper_ak47['dmg']

def attack(if_user_want_to_use_the_attachment, choice_head_or_body, choice_on_player_or_enemy, test_enemy, player_hp, player_dmg, sword, pistol, flail, watergun, ak47, paper_ak47):

	if player_dmg == sword['dmg']:
		test_enemy['hp'] -= sword['dmg']
	elif player_dmg == pistol['dmg']:
		if if_user_want_to_use_the_attachment == 'no':
			head_or_body = random.choice(choice_head_or_body)
			if head_or_body == 'body':
				test_enemy['hp'] -= pistol['dmg']
			else:
				test_enemy['hp'] -= pistol['dmg_head']
		else:
			head_or_body = random.choice(choice_head_or_body)
			if head_or_body == 'body':
				test_enemy['hp'] -= pistol['dmg_a']
			else:
				test_enemy['hp'] -= pistol['dmg_a_head']
	elif player_dmg == flail['dmg']:
		player_or_enemy = random.choice(choice_on_player_or_enemy)
		if player_or_enemy == 'player':
			player_hp -= flail['dmg']
			time.sleep(5)
		else:
			test_enemy['hp'] -= flail['dmg']
			test_enemy['stunned'] = True
	elif player_dmg == watergun['dmg']:
		test_enemy['hp'] -= watergun['dmg']
		time.sleep(5)
	elif player_dmg == ak47['dmg']:
		head_or_body = random.choice(choice_head_or_body)
		if head_or_body == 'body':
			test_enemy['hp'] = test_enemy['hp'] + test_enemy['enemy_body_dfn'] - ak47['dmg']
		else:
			test_enemy['hp'] = test_enemy['hp'] + test_enemy['enemy_head_dfn'] - ak47['dmg']
	elif player_dmg == paper_ak47['dmg']:
		head_or_body = random.choice(choice_head_or_body)
		if head_or_body == 'body':
			test_enemy['hp'] = test_enemy['hp'] + test_enemy['enemy_body_dfn'] - paper_ak47['dmg']
		else:
			test_enemy['hp'] = test_enemy['hp'] + test_enemy['enemy_head_dfn'] - paper_ak47['dmg']
	
	print('Your HP: ' + str(player_hp) + '\nEnemy HP: '+ str(test_enemy['hp']))

#all needed variables stored in dictionaries
test_enemy = {
	'dmg': 2,
	'hp': 20,
	'stunned': False,
	'enemy_head_dfn': 2,
	'enemy_body_dfn': 3,
}
sword = {
	'dmg': 2,
} 
pistol = {
	'dmg': 3,
	'dmg_head': 5,
	#pistol dmg with attachment
	'dmg_a': 5,
	'dmg_a_head': 9,
}
flail = {
	'dmg': 9,
}
watergun = {
	'dmg': 1,
	'stun_enemy': True,
	'stun_player': True,
}
ak47 = {
	'dmg': 15,
}
paper_ak47 = {
	'dmg': 20,
}
if_user_want_to_use_the_attachment = "no"
i = 0
#main part of the program
while True:
	if i == 0:
		info = input("Do you want to see the info of the guns?:").lower()
		i += 1
	
		if info == 'yes':
			print('SWORD\n damage: 2\n PISTOL\n damage: body = 3, head = 5, with attachment: body = 5, head = 9\n FLAIL\n damage: 9\n WATERGUN\n damage: 1 AND stuns player and enemy\nAK47\n damage: 15\nPAPER AK47\n damage: 20')
			time.sleep(5)
		else:
			pass

	while True:
		yes_or_no = input("Which weapon do you want to use? (type 'a' or 'b' or 'c' or....)\na) sword\nb) pistol\nc) flail\nd) watergun\ne) ak47\nf) paper ak47 ").lower()
		if yes_or_no == "a" or "b" or "c" or "d" or "e" or "f":
			break
		else: 
			print('Invalid Input. Try Again.')
	print(yes_or_no)
	if yes_or_no == "b":
		while True:
			if_user_want_to_use_the_attachment = input("There's an attachment available. Would you like to use it?:\n ").lower()
			if if_user_want_to_use_the_attachment == "yes" or "no":
				break
			else:
				print('Invalid Input. Try Again.')
	choice_head_or_body = ['head', 'body']
	choice_on_player_or_enemy = ['player', 'enemy']
	player_hp, player_dmg = 100, dmg(yes_or_no, sword, pistol, flail, watergun, ak47, paper_ak47)
	attack(if_user_want_to_use_the_attachment, choice_head_or_body, choice_on_player_or_enemy, test_enemy, player_hp, player_dmg, sword, pistol, flail, watergun, ak47, paper_ak47)



