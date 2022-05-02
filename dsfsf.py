import random
	random_num = random.randint(1, 100)
	print("Добро пожаловать в числовую угадайку")  
	user_choice = int(input())
	

	

	def is_valid(user_choice):
	  if user_choice > 100 or user_choice < 1 :
	    print("А может быть все-таки введем целое число от 1 до 100?")
	    return False 
	  else:
	    return True
	    
	def random_game(random_num, user_choice ):
	    counter = 1
	    while user_choice != random_num:
	        Flag_Valid = is_valid(user_choice)
	        if Flag_Valid == True:
	          if  user_choice > random_num:
	            print("Слишком много, попробуйте еще раз")
	            user_choice = int(input())
	            counter += 1
	          else:
	            print("Слишком мало, попробуйте еще раз")
	            user_choice = int(input())
	            counter += 1
	        else :
	          user_choice = int(input())
	          counter += 1
	

	    print("Вы угадали, поздравляем!")
	    print("Вы угадали с", counter, "попытки!")
	        
	random_game(random_num, user_choice )
