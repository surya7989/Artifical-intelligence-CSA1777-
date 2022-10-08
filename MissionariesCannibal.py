boat_side = "Right"
missionary_on_right = 3
cannibals_on_right = 3
missionary_on_left = 0
cannibals_on_left = 0

user_interface = ''
for i in range(0,missionary_on_left):
    user_interface += "\U0001f482"
for i in range(0,cannibals_on_left):
    user_interface += "\U0001f479"
user_interface += '|'
for i in range(0,5):
    user_interface += "\U0001f30a"
user_interface += "\U0001f6A2|"
for i in range(0,missionary_on_right):
    user_interface += "\U0001f482"
for i in range(0,cannibals_on_right):
    user_interface += "\U0001f479"
print(user_interface)

while True:
    missionary = int(input("Enter number of Missionary in boat on "+ boat_side + ":"))
    cannibals = int(input("Enter number of Cannibals in boat on " + boat_side + ":"))
    
    #Maximum number of people one the boat should be 1 or 2
    if (missionary+cannibals) != 1 and (missionary+cannibals) != 2:
        print("Invalid move")
        continue
    
    #Turn based decisions
    if boat_side == "Right":
        if missionary > missionary_on_right or cannibals > cannibals_on_right:
            print("Invalid move")
            continue
           
        missionary_on_right -= missionary
        cannibals_on_right -= cannibals
        missionary_on_left += missionary
        cannibals_on_left += cannibals
        
        boat_side = "Left"
        
        user_interface = ''
        for i in range(0,missionary_on_left):
            user_interface += "\U0001f482"
        for i in range(0,cannibals_on_left):
            user_interface += "\U0001f479"
        user_interface += '|\U0001f6A2'
        for i in range(0,5):
            user_interface += "\U0001f30a"
        user_interface += "|"
        for i in range(0,missionary_on_right):
            user_interface += "\U0001f482"
        for i in range(0,cannibals_on_right):
            user_interface += "\U0001f479"
        print(user_interface)
        
    else:
        if missionary > missionary_on_left or cannibals > cannibals_on_left:
            print("Invalid move")
            continue
            
        missionary_on_right += missionary
        cannibals_on_right += cannibals
        missionary_on_left -= missionary
        cannibals_on_left -= cannibals
        
        boat_side = "Right"
        
        user_interface = ''
        for i in range(0,missionary_on_left):
            user_interface += "\U0001f482"
        for i in range(0,cannibals_on_left):
            user_interface += "\U0001f479"
        user_interface += '|'
        for i in range(0,5):
            user_interface += "\U0001f30a"
        user_interface += "\U0001f6A2|"
        for i in range(0,missionary_on_right):
            user_interface += "\U0001f482"
        for i in range(0,cannibals_on_right):
            user_interface += "\U0001f479"
        print(user_interface)
     
    #condition for losing
    if (missionary_on_right != 0 and missionary_on_right < cannibals_on_right) or (missionary_on_left != 0 and missionary_on_left < cannibals_on_left):
        print("YOU LOSE")
        break
    
    #condition for winning
    if missionary_on_left == 3 and cannibals_on_left == 3:
        print("YOU WIN")
        break
print("GAME OVER")
