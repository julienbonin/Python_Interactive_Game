from random import randint
### Get User Name ###############################################################
def getName(userInput):
    if userInput.lower() == "q":
        endGame()
    while not((userInput.isalpha()) and (len(userInput) <=10)):
        print("Username can only be 10 or fewer alphabetical characters.") 
        userInput = input("What name would you like to use? ")
    return userInput
### Get User Type ###############################################################
def getType(userInput):
    while not((userInput.lower() == "elf") or (userInput.lower() == "nord") or (userInput.lower() == "q")):
        print("You must choose one. (ELF or NORD)")
        userInput = input("What are you? ")
    if userInput.lower() == "q":
        endGame()
    return userInput
### Main Character Class #############################################################
class Character:
    def __init__(self, characterName, characterType):
        self.__name = characterName
        self.__type = characterType
        self.__health = randint(0,100)
        self.__defense = randint(0,100)
        self.__attack = randint(0,100)
        self.__gold = randint(0,100)
        self.__location_X = 0
        self.__location_Y = 0
    ## Set Attribues
    def SetHealth(self, newHealth):
        self.__health = newHealth
    def SetDefense(self, newDefense):
        self.__defense = newDefense
    def SetAttack(self, newAttack):
        self.__attack = newAttack
    def SetGold(self, newGold):
        self.__gold = newGold           
    ## Coordinate Change
    def Y_Up(self):
        self.__location_Y += 1
    def Y_Down(self):
        self.__location_Y -= 1
    def X_Right(self):
        self.__location_X += 1
    def X_Left(self):
        self.__location_X -= 1
    # Get Info
    def GetName(self):
        return self.__name
    def GetType(self):
        return self.__type
    def GetHealth(self):
        return int(self.__health)
    def GetDefense(self):
        return int(self.__defense)
    def GetAttack(self):
        return int(self.__attack)
    def GetGold(self):
        return int(self.__gold)
    def GetLocation(self):
        return (self.__location_X, self.__location_Y)
### Print Character Attributes ##################################################
def characterInfo(mainCharacter):
    print("{:^30}".format("_" * 28))
    print("{:<5}{:^20}{:>5}".format("|", "Character Attributes", "|"))
    print("{:<1}{:28}{:>1}".format("|", "-" * 28, "|"))
    print("{:<1}{:>10}{:>14}{:>5}".format("|", "Health:", mainCharacter.GetHealth(), "|"))
    print("{:<1}{:28}{:>1}".format("|", "-" * 28, "|"))
    print("{:<1}{:>10}{:>14}{:>5}".format("|", "Defense:", mainCharacter.GetDefense(), "|"))
    print("{:<1}{:28}{:>1}".format("|", "-" * 28, "|"))
    print("{:<1}{:>10}{:>14}{:>5}".format("|", "Attack:", mainCharacter.GetAttack(), "|"))
    print("{:<1}{:28}{:>1}".format("|", "-" * 28, "|"))
    print("{:<1}{:>10}{:>14}{:>5}".format("|", "Gold:", mainCharacter.GetGold(), "|"))
    print("{}{:28}{}".format("|", "-" * 28, "|"))
    print("{:<1}{:>10}{:>14}{:>5}".format("|", mainCharacter.GetName().title(), mainCharacter.GetType().title(), "|"))

    print("{:1}{:28}{:1}".format("|", "_" * 28, "|"))
### Print Character and Enemy Attributes ########################################
def characterEnemyInfo(mainCharacter, enemy):
    print("{:^30}".format("_" * 28), end="")
    print("{:^20}".format("_" * 18))   
    print("{:<5}{:^20}{:>5}".format("|", "Character Attributes", "|"), end="")
    print("{:1}{:^18}{:1}".format("|", "Enemy Attributes", "|"))   
    print("{:<1}{:28}{:>1}".format("|", "-" * 28, "|"), end="")
    print("{}{}{}".format("|", "-" * 18, "|")) 
    print("{:<1}{:>10}{:>14}{:>5}".format("|", "Health:", mainCharacter.GetHealth(), "|"), end="")
    print("{:<1}{:^18}{:>1}".format("|", enemy.GetHealth(), "|"))
    print("{:<1}{:28}{:>1}".format("|", "-" * 28, "|"),end="")
    print("{}{}{}".format("|", "-" * 18, "|"))
    print("{:<1}{:>10}{:>14}{:>5}".format("|", "Defense:", mainCharacter.GetDefense(), "|"), end="")
    print("{:<1}{:^18}{:>1}".format("|", enemy.GetDefense(), "|"))
    print("{:<1}{:28}{:>1}".format("|", "-" * 28, "|"),end="")
    print("{}{}{}".format("|", "-" * 18, "|"))
    print("{:<1}{:>10}{:>14}{:>5}".format("|", "Attack:", mainCharacter.GetAttack(), "|"), end="")
    print("{:<1}{:^18}{:>1}".format("|", enemy.GetAttack(), "|"))
    print("{:<1}{:28}{:>1}".format("|", "-" * 28, "|"),end="")    
    print("{}{}{}".format("|", "-" * 18, "|"))
    print("{:<1}{:>10}{:>14}{:>5}".format("|", "Gold:", mainCharacter.GetGold(), "|"),end="")
    print("{:<1}{:^18}{:>1}".format("|", enemy.GetGold(), "|"))
    print("{:1}{:28}{:1}".format("|", "_" * 28, "|"), end="")    
    print("{}{}{}".format("|", "-" * 18, "|"))
### End Game #########################################################
def endGame():
    userInput = input("Would you like to create a save point? (y/n): ")
    while not((userInput.lower() == "y") or (userInput.lower() == "n")):
        userInput = input("Would you like to create a save point? (y/n): ")
    if userInput.lower() == "y":
         # saveGame()
        print("This feature is only available with the full version of this game.")
        exit()
    elif userInput.lower() == "n":
        exit()
### Print Directions to Move ###################################################
def getHelp():
    print("{:^30}".format("_" * 28))
    print("{}{:^28}{}".format("|", "MOVEMENT", "|"))
    print("{}{:28}{}".format("|", "-" * 28, "|"))
    print("{}{:28}{}".format("|", "Type 'n'  to move NORTH", "|"))
    print("{}{:28}{}".format("|", "-" * 28, "|"))
    print("{}{:28}{}".format("|", "Type 's'  to move SOUTH", "|"))
    print("{}{:28}{}".format("|", "-" * 28, "|"))
    print("{}{:28}{}".format("|", "Type 'e'  to move EAST", "|"))
    print("{}{:28}{}".format("|", "-" * 28, "|"))
    print("{}{:28}{}".format("|", "Type 'w'  to move WEST", "|"))
    print("{}{:28}{}".format("|", "-" * 28, "|"))
    print("{}{:28}{}".format("|", "Type 'ne' to move NORTH-EAST", "|"))
    print("{}{:28}{}".format("|", "-" * 28, "|"))
    print("{}{:28}{}".format("|", "Type 'nw' to move NORTH-WEST", "|"))
    print("{}{:28}{}".format("|", "-" * 28, "|"))
    print("{}{:28}{}".format("|", "Type 'se' to move SOUTH-EAST", "|"))
    print("{}{:28}{}".format("|", "-" * 28, "|"))
    print("{}{:28}{}".format("|", "Type 'sw' to move SOUTH-WEST", "|"))
    print("{}{:28}{}".format("|", "_" * 28, "|"))
### New Location CLASS #########################################################
class NewLocation:
    def __init__(self, location):  # location is Tuple (X,Y)
        self.__location_X = location[0]
        self.__location_Y = location[1]
        self.__number = randint(0,101)
        self.__hasEnemy = False
        self.__hasChess = False
        if (self.__number % 2) == 0 and (self.__number >= 51):
            self.__hasEnemy = True
        elif ((self.__number % 2) != 0) and (self.__number <= 50):
            self.__hasChess = True
    def GetHasEnemy(self):
        return self.__hasEnemy
    def GetHasChess(self):
        return self.__hasChess
    def GetLocation(self):
        return (self.__location_X, self.__location_Y)
### Enemy Class ################################################################
class Enemy:
    def __init__(self, characterLocation):
        self.__location_X = characterLocation[0]
        self.__location_Y = characterLocation[1]
        self.__health = randint(1,100)
        self.__defense = randint(0,100)
        self.__attack = randint(0,100)
        self.__gold = randint(0,100)
        self.__alive = None
        self.__bribeAmount = randint(0,101) # Amount the enemy would be willing accept for a bribe
    def GetHealth(self):
        return int(self.__health)
    def GetDefense(self):
        return int(self.__defense)
    def GetAttack(self):
        return int(self.__attack)
    def GetGold(self):
        return int(self.__gold)
    def GetAlive(self):
        return self.__alive
    def GetLocation(self):
        location = (self.__location_X, self.__location_Y)
        return location # returns tuple
    def GetBribe(self):
        return self.__bribeAmount
    def SetHealth(self, newHealth):
        self.__health = newHealth
    def SetDefense(self, newDefense):
        self.__defense = newDefense
    def SetAttack(self, newAttack):
        self.__attack = newAttack
    def SetGold(self, newGold):
        if (newGold + self.__gold) >= 100:
            self.__gold = 100
        else:
            self.__gold += newGold
    def SetAlive(self, bool):
        self.__alive = bool 
    ## Coordinate Change
    def Y_Up(self):
        self.__location_Y += 1
    def Y_Down(self):
        self.__location_Y -= 1
    def X_Right(self):
        self.__location_X += 1
    def X_Left(self):
        self.__location_X -= 1
#### Chess Interaction #########################################################
def chessInteraction(chess, mainCharacter):
    print()
    print("There's a CHESS at this location!")
    print()
    if chess.GetIsEmpty() != True:
        userInput = input("Whould you like to open it? (y/n): ")
        print()
        while not((userInput.lower() == "y") or (userInput.lower() == "n") or (userInput.lower() =="q")):
            userInput = input("'y' = YES, 'n' = NO, 'q' = QUIT")
        if userInput.lower() == "q":
            return True
        if userInput.lower() == "y":
            if chess.GetArmor() > 0: # CHESS HAS ARMOR
                print("This Chess contains", " +", chess.GetArmor(), " ARMOR!")
                print()
                armorInput = input("Would you like to take it? (y/n): ")
                print()
                if armorInput.lower() == "y":   # CHARACTER TAKES ARMOR
                    addArmor = chess.GetArmor()
                    characterDefense = mainCharacter.GetDefense()
                    newDefense = addArmor + characterDefense
                    if newDefense >= 100:   # DON'T ALLOW DEFENSE TO BE OVER 100
                        newDefense = 100
                        mainCharacter.SetDefense(newDefense)
                    else:
                        mainCharacter.SetDefense(newDefense)
                    chess.SetArmor(0)
                    chess.IsEmpty() # Sets chess to empty
                    print("Your DEFENSE is now ", mainCharacter.GetDefense())
                    print()
            elif chess.GetWeapon() > 0: # CHESS HAS WEAPON
                print("This Chess contains a", " +", chess.GetWeapon(), " WEAPON!")
                print()
                weaponInput = input("Would you like to take it? (y/n): ")
                print()
                if weaponInput.lower() == "y":  # CHARACTER TAKES WEAPON
                    addWeapon = chess.GetWeapon()
                    characterAttack = mainCharacter.GetAttack()
                    newAttack = addWeapon + characterAttack
                    if newAttack >= 100:
                        newAttack = 100
                        mainCharacter.SetAttack(newAttack)
                    else:
                        mainCharacter.SetAttack(newAttack)
                    chess.SetWeapon(0)
                    chess.IsEmpty()
                    print("Your ATTACK is now ", mainCharacter.GetAttack())
                    print()
            elif chess.GetGold() > 0:   # CHESS HAS GOLD
                print("This Chess contains", " +", chess.GetGold(), " GOLD!")
                print()
                goldInput = input("Would you like to take it? (y/n): ")
                print()
                if goldInput.lower() == "y":    # CHARACTER TAKES GOLD
                    addGold = chess.GetGold()
                    characterGold = mainCharacter.GetGold()
                    newGold = addGold + characterGold
                    if newGold >= 100:
                        newGold = 100
                        mainCharacter.SetGold(newGold)
                    else:
                        mainCharacter.SetGold(newGold)
                    chess.SetGold(0)
                    chess.IsEmpty()
                    print("Your GOLD is now ", mainCharacter.GetGold())
                    print()
            elif chess.GetHealth() > 0: # CHESS HAS HEALTH
                print("This Chess contains a", " +", chess.GetHealth(), " HEALTH BOOST!")
                print()
                healthInput = input("Would you like to take it? (y/n): ")
                print()
                if healthInput.lower() == "y":  # CHARACTER TAKES HEALTH
                    addHealth = chess.GetHealth()
                    characterHealth = mainCharacter.GetHealth()
                    newHealth = addHealth + characterHealth
                    if newHealth >= 100:
                        newHealth = 100
                        mainCharacter.SetHealth(newHealth)
                    else:
                        mainCharacter.SetHealth(newHealth)
                    chess.SetHealth(0)
                    chess.IsEmpty()
                    print("Your HEALTH is now ", mainCharacter.GetHealth())
                    print()
    else:
        print("This chess is empty...")
    print()
### Chess Class ################################################################
class Chess:
    def __init__(self, characterLocation):
        self.__location = characterLocation
        self.__number = randint(0,100)
        self.__armor = 0
        self.__weapon = 0
        self.__gold = 0
        self.__health = 0
        self.__isEmpty = False
        # Decide which item the chess contains
        
        if self.__number <= 35:
            if (self.__number % 2) == 0:
                self.__armor = randint(0, 100)
            else:
                self.__weapon = randint(0, 100)
        elif (self.__number > 35) and (self.__number < 70):
            if (self.__number % 2) == 0:
                self.__gold = randint(0, 100)
            else:
                self.__health = randint(0, 100)
        else: self.__isEmpty = True
    def GetArmor(self):
        return self.__armor
    def GetWeapon(self):
        return self.__weapon
    def GetGold(self):
        return self.__gold
    def GetHealth(self):
        return self.__health
    def GetIsEmpty(self):
        return self.__isEmpty
    def GetLocation(self):
        return self.__location
    def SetArmor(self, newArmor):
        self.__armor = newArmor
    def SetWeapon(self, newWeapon):
        self.__weapon = newWeapon
    def SetGold(self, newGold):
        self.__gold = newGold
    def SetHealth(self, newHealth):
        self.__health = newHealth
    def IsEmpty(self):
        self.__isEmpty = True
### Function to move mainCharacter ###################################################
def moveCharacter(actualInput, mainCharacter):
        if actualInput.lower() == "n": 
            mainCharacter.Y_Up()
        elif actualInput.lower() == "s":
            mainCharacter.Y_Down()
        elif actualInput.lower() == "e":
            mainCharacter.X_Right()
        elif actualInput.lower() == "w":
            mainCharacter.X_Left()
        elif actualInput.lower() == "ne":
            mainCharacter.X_Right()
            mainCharacter.Y_Up()
        elif actualInput.lower() == "se":
            mainCharacter.X_Right()
            mainCharacter.Y_Down()
        elif actualInput.lower() == "nw":
            mainCharacter.X_Left()
            mainCharacter.Y_Up()
        elif actualInput.lower() == "sw":
            mainCharacter.X_Left()
            mainCharacter.Y_Down()
### runFromEnemy - FUNCTION FOR ememyInteraction() ##############################
def runFromEnemy(mainCharacter):
    randomNumber1 = randint(0,10)
    number = randint(0,10)
    Success = True
    if randomNumber1 >= number:
        number = randint(1,8)
        if number == 1:
            mainCharacter.Y_Up()
        elif number == 2:
            mainCharacter.Y_Down()
        elif number == 3:
            mainCharacter.X_Right()
        elif number == 4:
            mainCharacter.X_Left()
        elif number == 5:
            mainCharacter.Y_Up()
            mainCharacter.X_Right()
        elif number == 6:
            mainCharacter.Y_Up()
            mainCharacter.X_Left()
        elif number == 7:
            mainCharacter.Y_Down()
            mainCharacter.X_Right()
        elif number == 8:
            mainCharacter.Y_Down()
            mainCharacter.X_Left()
    else:
        Success = False
    return Success, number
### Enemy Interaction ##########################################################
def enemyInteraction(enemy, mainCharacter):
    entered_q = None
    restart = None
    if enemy.GetAlive() == False:
        print("There's a dead enemy here.")
        print()
    else:
        print("Theres an enemy at this location!")
        characterEnemyInfo(mainCharacter, enemy)
        runSuccess = None
        bribeSuccess = None
        userInput = input("Do you want to Run [r], Bribe [b], or Fight [f]? ")
        print()
        while (runSuccess == None) or (bribeSuccess == None) or (enemy.GetAlive() == None):
            while userInput.lower() not in ("q","x","r","b","f"):
                    print("type 'x' for user/enemy attributes, type 'q' to Quit")
                    print()
                    userInput = input("You must Run[r], Bribe[b], or Fight[f]: ")
                    print()
            if userInput.lower() == "q":
                    entered_q = True
                    break
            elif userInput.lower() == "x":
                    characterEnemyInfo(mainCharacter, enemy)
            elif userInput.lower() == "r":
                if runSuccess == False:
                    print("You can't run!")
                    print()
                elif runSuccess == None:
                    runSuccess, runNumber = runFromEnemy(mainCharacter)
                    if runSuccess == True:
                        runFromEnemyPrint(runNumber)
                        break
                    else:
                        print("YOU RAN INTO THE ENEMY!")
                        print()
                        runSuccess = False
                        if bribeSuccess == False:
                            print("You can only Fight[f]")
                            print()
                        else:
                            print("Do you want to Bribe[b] or Fight[f]? ")
                            print()
            elif userInput.lower() == "b":
                if (bribeSuccess == False) or (mainCharacter.GetGold() <= 0):
                    print("You can't bribe!")
                    print()
                elif bribeSuccess == None:
                    bribeSuccess, bribeNumber = bribeEnemy(enemy, mainCharacter)
                    if bribeSuccess == True:
                        print("Your bribe worked!")
                        print()
                        break
                    else:
                        print("Your bribe didn't work!")
                        print()
                        bribeSuccess = False
                        if runSuccess == False:
                            print("You can only Fight[f]")
                            print()
                        else:
                            print("Do you want to Run[r] or Fight[f]? ")
                            print()
            elif userInput.lower() == "f":
                fightEnemy(enemy, mainCharacter) # Fight is to death. If you die, game over. If enemy dies, ('there is a dead enemy at this location')                
                if enemy.GetAlive() == True:
                    print("You lost the battle...")
                    print()
                    userInput = input("Would you like to play again? (y/n): ")
                    print()
                    while not((userInput.lower() == "y") or (userInput.lower() == "n")):
                        userInput = input("'y' to play again, 'n' to end game. ")
                        print()
                    if userInput.lower() == "y":
                        restart = True
                        break
                    elif userInput.lower() == "n":
                        quit()
                    else:
                        userInput = input("'y' to play again, 'n' to end game. ")
                        print()
                elif enemy.GetAlive() == False:
                    print("You killed the enemy! ")
                    print()
                    enemyGold = enemy.GetGold()
                    characterGold = mainCharacter.GetGold()
                    newCharacterGold = enemyGold + characterGold
                    mainCharacter.SetGold(newCharacterGold)
                    enemy.SetGold(0)
                    break
            if restart == True:
                break
            if entered_q == True:
                break
            if runSuccess == True:
                break
            if bribeSuccess == True:
                break
            if enemy.GetAlive() == False:
                break
            userInput = input("What will you do? ")
            print()
    return entered_q, restart
### Fight Enemy for Enemy Interaction ##########################################
def fightEnemy(enemy, mainCharacter):
    attackFirst = randint(0,1)
    if attackFirst == 0: # mainCharacter Attacks First
        print()
        print("You attack first!")
        print()
        while (mainCharacter.GetHealth() > 0) and (enemy.GetHealth() > 0):
            print(mainCharacter.GetName().title(), ": ", end="")
            CharacterAttackEnemy(enemy, mainCharacter)
            if enemy.GetAlive() == False:
                break
            print("Enemy: ", end="")
            EnemyAttackCharacter(enemy, mainCharacter)
            print()
    elif attackFirst == 1: # Enemy attacks first
        print()
        print("The enemy attacked you first!")
        print()
        while (mainCharacter.GetHealth() > 0) and (enemy.GetHealth() > 0):
            print("Enemy: ", end="")
            EnemyAttackCharacter(enemy, mainCharacter)
            if mainCharacter.GetHealth() <= 0:
                break
            print(mainCharacter.GetName().title(), ": ", end="")
            CharacterAttackEnemy(enemy, mainCharacter)
            print()
    if enemy.GetHealth() > 0:
        enemy.SetAlive(True)
    elif enemy.GetHealth() <= 0:
        enemy.SetAlive(False)
### Enemy Attacks Main Character ###############################################
def EnemyAttackCharacter(enemy, mainCharacter):
    attackOffset = enemy.GetAttack() * randomOffset()
    defendOffset = mainCharacter.GetDefense() * randomOffset()
    attackSuccess = int(attackOffset) - int(defendOffset)
    if attackSuccess > 0:
        characterDamage = mainCharacter.GetHealth() - attackSuccess
        mainCharacter.SetHealth(characterDamage)
        if mainCharacter.GetHealth() > 0:
            print("Your health is now ", mainCharacter.GetHealth())
            print()
        elif mainCharacter.GetHealth() <= 0:
            enemy.SetAlive(True)
    else:
        print("The enemy's attack had no effect!")
        print()
### Main Character Attacks Enemy ###############################################
def CharacterAttackEnemy(enemy, mainCharacter):
        attackOffset = mainCharacter.GetAttack() * randomOffset()
        defendOffset = enemy.GetDefense() * randomOffset()
        attackSuccess = int(attackOffset) - int(defendOffset)
        if attackSuccess > 0:
            enemyDamage = enemy.GetHealth() - attackSuccess
            enemy.SetHealth(enemyDamage)
            if enemy.GetHealth() > 0:
                print("The enemy's health is now ", enemy.GetHealth())
                print()
            elif enemy.GetHealth() <= 0:
                enemy.SetAlive(False)               
        else:
            print("Your attack had no effect!")
            print()
### Random Offset For Fight With Enemy #########################################
def randomOffset():
    number = (randint(0,100)) / 100
    return number
### Bribe Enemy for Enemy Interaction ##########################################
def bribeEnemy(enemy, mainCharacter):
    bribeAmount = enemy.GetBribe()
    characterGold = mainCharacter.GetGold()
    print("You have ", characterGold, " GOLD.")
    print()
    userInput = input("How much would you like to BRIBE with? ")
    print()
    while not(userInput.isdigit()):
        userInput = input("Please enter an integer value: ")
        print()
    while not(int(userInput) <= characterGold):
        print("You don't have that much GOLD!")
        print()
        userInput = int(input("Please enter another amount: "))
        print()
    if int(userInput) > bribeAmount:
        number = randint(1,8)
        if number == 1:
            enemy.Y_Up()
        elif number == 2:
            enemy.Y_Down()
        elif number == 3:
            enemy.X_Right()
        elif number == 4:
            enemy.X_Left()
        elif number == 5:
            enemy.Y_Up()
            enemy.X_Right()
        elif number == 6:
            enemy.Y_Up()
            enemy.X_Left()
        elif number == 7:
            enemy.Y_Down()
            enemy.X_Right()
        elif number == 8:
            enemy.Y_Down()
            enemy.X_Left()
        bribeSuccess = True
        userGoldAfterBribe = (characterGold - int(userInput))
        enemy.SetGold(int(userInput))
        mainCharacter.SetGold(userGoldAfterBribe)
    else:
        bribeSuccess = False
    return bribeSuccess, bribeAmount
### Print for Run From Enemy Direction #########################################
def runFromEnemyPrint(number):
    if number == 1:
        print("You ran NORTH! You're safe, for now.")
        print()
    elif number == 2:
        print("You ran SOUTH! You're safe, for now.")
        print()
    elif number == 3:
        print("You ran EAST! You're safe, for now.")
        print()
    elif number == 4:
        print("You ran WEST! You're safe, for now.")
        print()
    elif number == 5:
        print("You ran NORTH-EAST! You're safe, for now.")
        print()
    elif number == 6:
        print("You ran NORTH-WEST! You're safe, for now.")
        print()
    elif number == 7:
        print("You ran SOUTH-EAST! You're safe, for now.")
        print()
    elif number == 8:
        print("You ran SOUTH-WEST! You're safe, for now.")
        print()
        
#### M A I N ###################################################################
def main():
    entered_q = None
    restart = None
    locationDictionary = {}
    userInput = input("What is your name? ")
    print()
    characterName = getName(userInput)
    userInput = input("Are you Elf of Nord? ")
    print()
    characterType = getType(userInput)
    mainCharacter = Character(characterName, characterType)
    characterInfo(mainCharacter)
    print("type 'x' for character attributes, 'help' for HELP, 'q' to QUIT")
    print()
    while True:
        userInput = input("What direction would you like to move? ")
        print()
        directions = ("n","s","e","w","ne","nw","se","sw")
        if userInput.lower() == "q":
            break
        elif userInput.lower() == "x":
            characterInfo(mainCharacter)
        elif userInput.lower() == "help":
            getHelp()
        elif userInput in directions:
            moveCharacter(userInput, mainCharacter)
            location = mainCharacter.GetLocation()
            # Check if location already exists or add it to dictionary if not
            if location not in locationDictionary:
                new_location = NewLocation(location)
                if (new_location.GetHasEnemy() == True):
                    new_enemy = Enemy(location)
                    locationDictionary.update({location:(new_location,new_enemy)})
                elif (new_location.GetHasChess() == True):
                    new_chess = Chess(location)
                    locationDictionary.update({location:(new_location,new_chess)})
                else: locationDictionary.update({location:(new_location, "There's nothing here.")})
            # Current Location interaction
            currentLocation = locationDictionary[location]
            if currentLocation[0].GetHasEnemy() == True:
                enemy = currentLocation[1]
                entered_q, restart = enemyInteraction(enemy, mainCharacter)
                if entered_q == True: break
                if restart == True: break
            elif currentLocation[0].GetHasChess() == True:
                chess = currentLocation[1]
                entered_q = chessInteraction(chess, mainCharacter)
                if entered_q == True: break
            else:
                print(currentLocation[1])
                print(mainCharacter.GetLocation())
    return entered_q, restart

### Run Main Function ##########################################################
restart = None
while restart != False:
    entered_q, restart = main()
    if entered_q == True:
        restart = False
    print("*" * 100)
endGame()
