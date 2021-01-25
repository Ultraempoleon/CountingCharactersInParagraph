#Reads through the text file, every different character is appended to a list
#There are two lists, CharacterList adds every new character read from the file / the second list CharacterCounterList will count every time a character is read from the file that already exists in the list
#Example file abcc
#                              a  b  c
#List1 = [a, b, c, c] List2 = [1, 1, 2]
#As it goes through the list of characters appended to the list, will count the amount of times it reads that characteter from the file
#


#Declarations
characterList = []
characterCounterList = []
firstCharacterAppeneded = False
characterAlreadyInList = False
characterCount = 0
characterCountIndex = 0



#Main
with open('test.txt', 'r') as f:
  for reader in f:              #reader is every line (yes its going over the first two lines
    for i in reader:            #i is every character in the line (yes its reading the characters
      
      #print(f'now checking on the character {i}')

      #will attach the first character to the list
      if not firstCharacterAppeneded: 
        characterList.append(i)
        characterCounterList.append(0)
        firstCharacterAppeneded = True 
      
      #j iterating through characterList
      for j in characterList:   
        
        #print(f'checking: {i} : {j}')
        #Checks if the character is already on the list
        if (i == j):
          characterCounterList[characterList.index(j)] += 1
          #print(f'{i} matched with {j} so the list for {j} was increased')
          characterAlreadyInList = True
      #end of J loop

      #if the character is not on the list, add it
      if (not characterAlreadyInList):
          characterList.append(i)
          characterCounterList.append(1)
      
      characterAlreadyInList = False

      #print(f'done checking {i}')
print(characterList)
print(characterCounterList)