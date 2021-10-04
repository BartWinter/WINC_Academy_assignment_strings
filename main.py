# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#Part 1
scorer_1 = 'Ruud Gullit'
scorer_2 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = scorer_1 + ' ' + str(goal_0) + ',' + ' ' + scorer_2 + ' ' + str(goal_1)
print(scorers)

report = f'{scorer_1} scored in the {goal_0}nd minute' '\n' f'{scorer_2} scored in the {goal_1}th minute'
print(report) 


#Part 2
player = 'Frank Rijkaard'
space_position = player.find(' ')
first_name = player[0:space_position]
print(first_name)

last_name = player[space_position+1:]
last_name_len = len(last_name)
print(last_name_len)

name_short = player[0] + '.' + ' ' + last_name 
print(name_short)

x = len(first_name)-1 
chant = (x * (first_name + '!' + ' ') + (first_name + '!'))  
print(chant)

#print(good_chant)
good_chant = chant[-1] != ' ' 
print(good_chant)
