no_of_playeres = 1
player_count=3
print(''''Rock'
'Paper'
'Scissors'
''')
player=input("Rock, Paper, Scissors?:  ").lower()

while  player == "rock" or "paper" or "scissors":
	
	import random
	
	game= ["rock", "paper", "scissors"]
	cpu= random.choice(game)
	print("you played: " + player , "...cpu playered: "+ cpu)
			
	no_of_playeres+=1
	if player == cpu:
		print("its a tie! ")
		break
	
	if player == "rock":
		if cpu== 'scissors':
			print("you win!")
			break
		
		elif cpu == 'paper':
		   	print("you lose! ")
		   	break
	    	
	if player == "paper":
		if cpu == "rock":
			print("you win! ")
			break
		
		elif cpu == "scissors":
			print("you lose! ")
			break
	
	if player == 'scissors':
		if cpu == 'rock':
			print("you lose! ")
			break
		
		elif cpu == 'paper':
			print("you win!")
			break
			
	else:
		print("wrong command! ")
		break