#Prog counts number of each character in the paragraph
characterList = []
characterCounter = []
firstCharacterAppeneded = False
characterAlreadyInList = False



with open('test.txt', 'r') as f:
  for reader in f:              #reader is every line (yes its going over the first two lines
    for i in reader:            #i is every character in the line (yes its reading the characters

      #will attach the first character to the list
      if not firstCharacterAppeneded: 
        characterList.append(i)
        firstCharacterAppeneded = True 
      
      #j iterating through characterList
      for j in characterList:   
        
        #Checks if the character is already on the list
        if (i == j):
          characterAlreadyInList = True
      
      #if the character is not on the list, add it
      if (not characterAlreadyInList):
          characterList.append(i)
      
      characterAlreadyInList = False
print(characterList)