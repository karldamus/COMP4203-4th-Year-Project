import pprint

puz = [["D", "I", "R", "T", "Y", "D", "A", "N", "C", "I", "N", "G", "E", "R", "S"],
          ["A", "D", "I", "Q", "D", "E", "V", "I", "L", "S", "P", "O", "N", "D", "J"],
          ["D", "R", "D", "A", "R", "K", "S", "E", "C", "R", "E", "T", "S", "S", "O"],
          ["S", "A", "A", "D", "A", "Y", "A", "N", "D", "N", "I", "G", "H", "T", "G"],
          ["A", "H", "N", "I", "P", "A", "R", "T", "H", "T", "A", "E", "D", "G", "N"],
          ["R", "E", "I", "T", "O", "D", "E", "L", "I", "R", "I", "O", "U", "S", "A"],
          ["M", "I", "E", "D", "E", "A", "D", "O", "R", "A", "L", "I", "V", "E", "J"],
          ["Y", "D", "L", "G", "J", "S", "N", "O", "I", "L", "E", "D", "N", "A", "D"],
          ["U", "E", "C", "N", "E", "L", "I", "S", "D", "A", "E", "D", "T", "W", "A"],
          ["G", "N", "I", "K", "L", "A", "W", "N", "A", "M", "D", "A", "E", "D", "I"],
          ["A", "T", "O", "O", "B", "S", "A", "D", "F", "T", "M", "R", "P", "B", "S"],
          ["A", "I", "B", "R", "U", "T", "S", "I", "D", "E", "T", "O", "U", "R", "I"],
          ["E", "R", "U", "S", "O", "L", "C", "S", "I", "D", "R", "E", "O", "Q", "E"],
          ["T", "A", "E", "H", "D", "A", "E", "D", "R", "A", "G", "N", "E", "T", "S"],
          ["R", "I", "D", "I", "R", "E", "C", "T", "A", "C", "T", "I", "O", "N", "G"]]

puz2 = [["R", "V", "K", "M", "B", "P", "T", "K", "B", "R", "V", "T", "R", "R", "D"], 
        ["F", "R", "E", "K", "N", "U", "B", "E", "T", "U", "W", "O", "F", "Y", "N"], 
        ["R", "E", "N", "O", "I", "R", "E", "A", "N", "Z", "T", "U", "R", "F", "U"], 
        ["L", "C", "N", "T", "T", "N", "I", "M", "U", "A", "L", "L", "I", "U", "G"], 
        ["S", "A", "A", "D", "A", "M", "S", "D", "G", "Y", "M", "O", "E", "D", "A"], 
        ["B", "A", "Z", "I", "L", "L", "E", "P", "L", "E", "C", "U", "S", "R", "S"], 
        ["Q", "I", "E", "R", "L", "G", "D", "E", "I", "L", "A", "S", "E", "Y", "N"], 
        ["F", "S", "C", "E", "A", "L", "I", "A", "T", "S", "S", "E", "K", "E", "G"], 
        ["R", "E", "E", "S", "S", "A", "E", "O", "E", "I", "S", "L", "E", "L", "V"], 
        ["C", "G", "V", "R", "O", "S", "R", "B", "N", "S", "A", "A", "O", "N", "A"], 
        ["P", "U", "H", "T", "O", "S", "I", "R", "O", "M", "T", "U", "R", "I", "N"], 
        ["L", "U", "H", "R", "E", "V", "E", "T", "M", "T", "T", "T", "I", "R", "G"], 
        ["T", "V", "A", "E", "M", "A", "S", "S", "A", "H", "T", "R", "R", "B", "O"], 
        ["L", "M", "J", "Y", "F", "J", "L", "P", "V", "M", "U", "E", "A", "S", "G"], 
        ["T", "R", "A", "X", "I", "G", "L", "A", "A", "A", "J", "C", "T", "L", "H"]]

# Given a possible match for word, we trace along the puzzle in the direction given (supplied by k and l values)
# to confirm it is the word and we store the indicies along the way so it can be returned to the calling function
def confirmWord(puzzle, word, i, j, k, l, currIndex):
    rtrn = []
    scaleK = k
    scaleL = l
    limitRow = len(puzzle) - 1
    limitCol = len(puzzle[0]) - 1

    # Getting here means we have identified the first two letters of the word, so they can safely be added to rtrn
    rtrn.append((i, j))
    rtrn.append((i + k, j + l))

    k += k
    l += l

    for index in range(len(word) - 2):
        if i + k > limitRow or i + k < 0 or j + l > limitCol or j + l < 0:
            rtrn = False
            break

        if puzzle[i + k][j + l] == word[currIndex + 1]:
            rtrn.append((i+k, j+l))
            k = k + scaleK
            l = l + scaleL
            currIndex += 1

            if currIndex == len(word) - 1:
                return rtrn
        else:
            rtrn = False
            break

    return rtrn

# Input: Word Search puzzle and word bank associated with puzzle
# Output: Dictonary with words as keys and their solution as array of tuple values as values to dictonary 
def findWords(puzzle, words):    
    rtrn = dict(zip(words, [None]*len(words)))
    wordsNoSpaces = []
    limitRow = len(puzzle) - 1
    limitCol = len(puzzle[0]) - 1

    # Sanitize words
    for w in words:
        w = w.replace(" ", "")
        w = w.replace("'", "")
        w = w.replace("-", "")
        wordsNoSpaces.append(w)

    for index, w in enumerate(wordsNoSpaces):
        currIndex = 0
        wordFound = False
        
        # Loop through all elements of puzzle and look at neighbours for possible matches
        for i in range(len(puzzle)):
            for j in range(len(puzzle[0])): 

                if i > 0 and i < limitRow and j > 0 and j < limitCol and wordFound == False: # 0 < i < len, 0 < j < len (General Case )
                    if puzzle[i][j] == w[currIndex]:                                              
                        for k in range(-1, 2):
                            for l in range(-1, 2):
                                if puzzle[i + k][j + l] == w[currIndex+1]:
                                    currIndex += 1
                                    val = confirmWord(puzzle, w, i, j, k, l, currIndex) 

                                    if val == False:
                                        currIndex -= 1
                                        continue
                                    else:
                                        rtrn[words[index]] = val
                                        wordFound = True
                                        break

                elif i == 0 and j > 0 and j < limitCol and wordFound == False: # i == 0, 0 < j < len (top row, not a corner)
                    if puzzle[i][j] == w[currIndex]:                                              
                        for k in range(0, 2):
                            for l in range(-1, 2):
                                if puzzle[i + k][j + l] == w[currIndex+1]:
                                    currIndex += 1
                                    val = confirmWord(puzzle, w, i, j, k, l, currIndex) 

                                    if val == False:
                                        currIndex -= 1
                                        continue
                                    else:
                                        rtrn[words[index]] = val
                                        wordFound = True
                                        break

                elif i == limitRow and j > 0 and j < limitCol and wordFound == False: # i == len, 0 < j < len (bottom row, not a corner)
                    if puzzle[i][j] == w[currIndex]:                                              
                        for k in range(-1, 1):
                            for l in range(-1, 2):
                                if puzzle[i + k][j + l] == w[currIndex+1]:
                                    currIndex += 1
                                    val = confirmWord(puzzle, w, i, j, k, l, currIndex) 

                                    if val == False:
                                        currIndex -= 1
                                        continue
                                    else:
                                        rtrn[words[index]] = val
                                        wordFound = True
                                        break

                elif i > 0 and i < limitRow and j == 0 and wordFound == False: # 0 < i < len, j == 0 (first column, not a corner)
                    if puzzle[i][j] == w[currIndex]:                                              
                        for k in range(-1, 2):
                            for l in range(0, 2):
                                if puzzle[i + k][j + l] == w[currIndex+1]:
                                    currIndex += 1
                                    val = confirmWord(puzzle, w, i, j, k, l, currIndex) 

                                    if val == False:
                                        currIndex -= 1
                                        continue
                                    else:
                                        rtrn[words[index]] = val
                                        wordFound = True
                                        break

                elif i > 0 and i < limitRow and j == limitCol and wordFound == False: # 0 < i < len, j == len (rightmost column, not a corner)
                    if puzzle[i][j] == w[currIndex]:                                              
                        for k in range(-1, 2):
                            for l in range(-1, 1):
                                if puzzle[i + k][j + l] == w[currIndex+1]:
                                    currIndex += 1
                                    val = confirmWord(puzzle, w, i, j, k, l, currIndex) 

                                    if val == False:
                                        currIndex -= 1
                                        continue
                                    else:
                                        rtrn[words[index]] = val
                                        wordFound = True
                                        break

                elif i == 0 and j == 0: # topleft corner
                    if puzzle[i][j] == w[currIndex] and wordFound == False:                                              
                        for k in range(0, 2):
                            for l in range(0, 2):
                                if puzzle[i + k][j + l] == w[currIndex+1]:
                                    currIndex += 1
                                    val = confirmWord(puzzle, w, i, j, k, l, currIndex) 

                                    if val == False:
                                        currIndex -= 1
                                        continue
                                    else:
                                        rtrn[words[index]] = val
                                        wordFound = True
                                        break

                elif i == limitRow and j == 0 and wordFound == False: # bottomleft corner
                    if puzzle[i][j] == w[currIndex]:                                              
                        for k in range(-1, 1):
                            for l in range(0, 2):
                                if puzzle[i + k][j + l] == w[currIndex+1]:
                                    currIndex += 1
                                    val = confirmWord(puzzle, w, i, j, k, l, currIndex) 

                                    if val == False:
                                        currIndex -= 1
                                        continue
                                    else:
                                        rtrn[words[index]] = val
                                        wordFound = True
                                        break

                elif i == 0 and j == limitCol and wordFound == False: # topright corner
                    if puzzle[i][j] == w[currIndex]:                                              
                        for k in range(0, 2):
                            for l in range(-1, 1):
                                if puzzle[i + k][j + l] == w[currIndex+1]:
                                    currIndex += 1
                                    val = confirmWord(puzzle, w, i, j, k, l, currIndex) 

                                    if val == False:
                                        currIndex -= 1
                                        continue
                                    else:
                                        rtrn[words[index]] = val
                                        wordFound = True
                                        break

                elif i == limitRow and j == limitCol and wordFound == False: # bottomright corner
                    if puzzle[i][j] == w[currIndex]:                                              
                        for k in range(-1, 1):
                            for l in range(-1, 1):
                                if puzzle[i + k][j + l] == w[currIndex+1]:
                                    currIndex += 1
                                    val = confirmWord(puzzle, w, i, j, k, l, currIndex) 

                                    if val == False:
                                        currIndex -= 1
                                        continue
                                    else:
                                        rtrn[words[index]] = val
                                        wordFound = True
                                        break
                
                if wordFound:
                    break
                

    
    return rtrn

wordBank1 = ["DADS ARMY", "DAS BOOT", "DEATHTRAP", "DIRTY DANCING", "DAISIES", "DAY AND NIGHT", "DELIRIOUS", "DISCLOSURE", "DANDELION", "DEAD HEAT",
            "DETOUR", "DISTURBIA", "DANIEL", "DEAD MAN WALKING", "DEVILS POND", "DJANGO", "DANTE'S INFERNO", "DEAD OR ALIVE", "DIE HARD", "DOUBLE JEOPARDY",
            "DARK SECRETS", "DEAD SILENCE", "DIRECT ACTION", "DRAGNET"]

wordBank2 = ["ADAMS", "CASSATT", "HASSAM", "REID", "BAZILLE", "CEZANNE", "MANET", "RENOIR", "BRINLEY", "DEGAS", "MATISSE", "SEROV", "BUNKER", "DUFY", "MONET", 
             "SISLEY", "BUTLER", "FRIESEKE", "MORISOT", "TOULOUSE-LAUTREC", "CAILLEBOTTE", "GUILLAUMIN", "PISSARRO", "VAN GOGH"]

if __name__ == "__main__":
    testWords = ["DAISIES", "DANDELION", "DIRECT ACTION", "DJANGO"]
    pprint.pprint(findWords(puz2, wordBank2))