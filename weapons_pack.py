#Packages
import random
import time
#For all the warnings you need the hp, dfn (defense) and dmg stats all setup.


def dmg(yes_or_no, sword, pistol, flail, watergun, ak47, paper_ak47, scar_l, ak_37, ak_sh47):
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
	elif yes_or_no == 'g':
		return knife['dmg']
	elif yes_or_no == 'h':
		return minigun['dmg']
	elif yes_or_no == 'i':
		return portable_flamethrower['dmg']
	elif yes_or_no == 'j':
		return flamethrower['dmg']
	elif yes_or_no == 'k':
		return hammer['dmg']
	elif yes_or_no == 'l':
		return shotgun['dmg_close']
	elif yes_or_no == 'm':
		return scar_l['dmg']
	elif yes_or_no == 'n':
		return ak_sh47['dmg_close']
	elif yes_or_no == 'o':
		return ak_37['dmg_close']
	

def attack(if_user_want_to_use_the_attachment, choice_head_or_body, choice_on_player_or_enemy, test_enemy, player_hp, player_dmg, sword, pistol, flail, watergun, ak47, paper_ak47, player, scar_l, ak_37, ak_sh47):
	if test_enemy['stunned_turns'] > 0:
		test_enemy['hp'] -= test_enemy['stunned_dmg']
		test_enemy['stunned turns'] -= 1
	if test_enemy['stunned_turns'] == 0:
		test_enemy['stunned_dmg'] == 0
	
	if player_dmg == sword['dmg']:
		test_enemy['hp'] -= sword['dmg'] * (1 - (test_enemy['dfn'] / 10))
	elif player_dmg == pistol['dmg']:
		if if_user_want_to_use_the_attachment == 'no':
			head_or_body = random.choice(choice_head_or_body)
			if head_or_body == 'body':
				test_enemy['hp'] -= pistol['dmg'] * (1 - (test_enemy['dfn'] / 10))
			else:
				test_enemy['hp'] -= pistol['dmg_head'] * (1 - (test_enemy['dfn'] / 10))
		else:
			head_or_body = random.choice(choice_head_or_body)
			if head_or_body == 'body':
				test_enemy['hp'] -= pistol['dmg_a'] * (1 - (test_enemy['dfn'] / 10))
			else:
				test_enemy['hp'] -= pistol['dmg_a_head'] * (1 - (test_enemy['dfn'] / 10))
	elif player_dmg == flail['dmg']:
		player_or_enemy = random.choice(choice_on_player_or_enemy)
		if player_or_enemy == 'player':
			player_hp -= flail['dmg'] * (1 - (test_enemy['dfn'] / 10))
			player['stunned'] = True
		else:
			test_enemy['hp'] -= flail['dmg'] * (1 - (test_enemy['dfn'] / 10))
			test_enemy['stunned'] = True
	elif player_dmg == watergun['dmg']:
		test_enemy['hp'] -= watergun['dmg'] * (1 - (test_enemy['dfn'] / 10))
	elif player_dmg == ak47['dmg']:
		head_or_body = random.choice(choice_head_or_body)
		if head_or_body == 'body':
			test_enemy['hp'] = test_enemy['hp'] + test_enemy['enemy_body_dfn'] - (ak47['dmg'] * (1 - (test_enemy['dfn'] / 10)))
		else:
			test_enemy['hp'] = test_enemy['hp'] + test_enemy['enemy_head_dfn'] - (ak47['dmg'] * (1 - (test_enemy['dfn'] / 10)))
	elif player_dmg == paper_ak47['dmg']:
		head_or_body = random.choice(choice_head_or_body)
		if head_or_body == 'body':
			test_enemy['hp'] = test_enemy['hp'] + test_enemy['enemy_body_dfn'] - (paper_ak47['dmg'] * (1 - (test_enemy['dfn'] / 10)))
		else:
			test_enemy['hp'] = test_enemy['hp'] + test_enemy['enemy_head_dfn'] - (paper_ak47['dmg'] * (1 - (test_enemy['dfn'] / 10)))
	elif player_dmg == knife['dmg']:
		test_enemy['hp'] -= knife['dmg'] * (1 - (test_enemy['dfn'] / 10))
		test_enemy['stunned_turns'] = knife['stunned_turns']
		test_enemy['stunned_dmg'] = knife['stunned_dmg']
	elif player_dmg == minigun['dmg']:
		test_enemy['hp'] -= minigun['dmg'] * (1 - (test_enemy['dfn'] / 10))
		minigun['usable'] = False
	elif player_dmg == portable_flamethrower['dmg']:
		test_enemy['hp'] -= portable_flamethrower['dmg'] * (1 - (test_enemy['dfn'] / 10))
	elif player_dmg == flamethrower['dmg']:
		test_enemy['hp'] -= flamethrower['dmg'] * (1 - (test_enemy['dfn'] / 10))
	elif player_dmg == hammer['dmg']:
		test_enemy['stunned_turns'] = hammer['stunned_turns']
		test_enemy['hp'] -= hammer['dmg'] * (1 - (test_enemy['dfn'] / 10))
	elif player_dmg == shotgun['dmg_close']:
		close_or_far == random.choice(choice_close_or_far)
		if close_or_far == 'close':
			test_enemy['hp'] -= shotgun['dmg_close'] * (1 - (test_enemy['dfn'] / 10))
		else:
			test_enemy['hp'] -= shotgun['dmg_far'] * (1 - (test_enemy['dfn'] / 10))
	elif player_dmg == scar_l['dmg']:
		if test_enemy['dfn'] > 0:
			test_enemy['hp'] -= scar_l['dmg'] * (1 - (test_enemy['dfn'] / 10))
			test_enemy['dfn'] -= 1
		else:
			test_enemy['hp'] -= scar_l['dmg'] * (1 - (test_enemy['dfn'] / 10))
	elif player_dmg == ak_sh47['dmg_close']:
		close_or_far = random.choice(choice_close_or_far)
		if close_or_far == 'close':
			test_enemy['hp'] -= ak_sh47['dmg_close'] * (1 - (test_enemy['dfn'] / 10))
		else:
			tets_enemy['hp'] -= ak_sh47['dmg_far'] * (1 - (test_enemy['dfn'] / 10))
	elif player_dmg == ak_37['dmg_close']:
		close_or_far = random.choice(choice_close_or_far)
		if close_or_far == 'close':
			test_enemy['hp'] -= ak_37['dmg_close'] * (1 - (test_enemy['dfn'] / 10))
		else:
			test_enemy['hp'] -= ak_37['dmg_far'] * (1 - (test_enemy['dfn'] / 10))

	print('Your HP: ' + str(player_hp) + '\nEnemy HP: '+ str(int(test_enemy['hp'])) + '\nEnemy Dfn: '+ str(test_enemy['dfn']))

#all needed variables stored in dictionaries
test_enemy = {
	'dmg': 2,
	'dfn': 3,
	'hp': 20,
	'stunned_turns': 0,
	'stunned_dmg': 0,
	'enemy_head_dfn': 2,
	'enemy_body_dfn': 3,
}
knife = {
	'dmg': 1,
	'stunned_dmg': 5,
	'stunned_turns': 5,
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
}
ak47 = {
	'dmg': 15,
}
paper_ak47 = {
	'dmg': 20,
}
minigun = {
	'dmg': 30,
	#you can only use minigun once
	'usable': True,
}
portable_flamethrower = {
	'dmg': 10,
}
flamethrower = {
	'dmg': 20,
}
hammer = {
	'dmg': 15,
	'stunned_turns': 3,
}
shotgun = {
	'dmg_close': 7,
	'dmg_far': 2,
}
player = {
	'stunned': False,
}
scar_l = {
	'dmg': 12,
	'min_dfn': 1,
}
ak_sh47 = {
	'dmg_close': 25,
	'dmg_far': 17,
}
ak_37 = {
	'dmg_close': 15,
	'dmg_far': 13,
}

if_user_want_to_use_the_attachment = "no"
i = 0
#main part of the program
while True:
	if test_enemy['hp'] <= 0:
		print("You WON!")
		break
	if minigun['usable'] == False:
		minigun['dmg'] = 0
	if i == 0:
		info = input("Do you want to see the info of the guns?:").lower()
		i += 1
	
		if info == 'yes':
			print('SWORD\n damage: 2\nPISTOL\n damage: body = 3, head = 5, with attachment: body = 5, head = 9\nFLAIL\n damage: 9\nWATERGUN\n damage: 1 AND stuns player and enemy\nAK47\n damage: 15\nPAPER AK47\n damage: 20\nKNIFE\n damage: 1, bleeding: 1 (5 turns), stuns enemy for 5 turns\nMINIGUN\n damage: 30, breaks after 1 turn\nPORTABLE FLAMETHROWER\n damage: 10\nFLAMETHROWER\n damage: 20\nHAMMER\n damage: 15, stuns enemy for 3 turns\nSHOTGUN\n damage: close = 7, far = 2\nSCAR L\n damage: 12, takes 1 point from enemy defense\nAK-SH47\n damage: close = 25, far = 17\nAK-37\n damage: close = 15, far = 13\n')
			time.sleep(5)
		else:
			pass

	while True:
		yes_or_no = input("Which weapon do you want to use? (type 'a' or 'b' or 'c' or....)\na) sword\nb) pistol\nc) flail\nd) watergun\ne) ak47\nf) paper ak47\ng) knife\nh) minigun\ni) portable flamethrower\nj) flamethrower\nk) hammer\nl) shotgun\nm) scar l\nn) ak-sh47\no) ak-37\n").lower()
		if yes_or_no == "a" or "b" or "c" or "d" or "e" or "f" or "g" or "h" or "i" or "j" or "k" or "l" or "m" or "n" or "o":
			if minigun['usable'] == False and yes_or_no == "h":
				print("Oh no! Minigun malfunctioned!")
				break
			break
		else: 
			print('Invalid Input. Try Again.')

	if yes_or_no == "b":
		while True:
			if_user_want_to_use_the_attachment = input("There's an attachment available. Would you like to use it?:\n ").lower()
			if if_user_want_to_use_the_attachment == "yes" or "no":
				break
			else:
				print('Invalid Input. Try Again.')
	choice_head_or_body = ['head', 'body']
	choice_on_player_or_enemy = ['player', 'enemy']
	choice_close_or_far = ['close', 'far']
	player_hp, player_dmg = 100, dmg(yes_or_no, sword, pistol, flail, watergun, ak47, paper_ak47, scar_l, ak_37, ak_sh47)
	attack(if_user_want_to_use_the_attachment, choice_head_or_body, choice_on_player_or_enemy, test_enemy, player_hp, player_dmg, sword, pistol, flail, watergun, ak47, paper_ak47, player, scar_l, ak_37, ak_sh47)






