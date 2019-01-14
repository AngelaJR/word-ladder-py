from collections import defaultdict
from collections import deque
import time


'''
Function build a graph of word in which each word is a node in the graph,
and a node may have two words that adjacent if they differ by one letter.
To build the graph a python dictionary is created in which words that rhyme and are off by just one letter
are group together.
This function receives one parameter which is an array of words and returns the
graph.
For example The Graph will look as: {'CARE': set(['CAFE', 'TARE'])}
'''
def getGraph(words):
    dictionary = {}  #initialize an object which will take the words
    dictGraph = defaultdict(set) #initialize the graph.

    '''
    Iterates through the words array and creates a list of objectsself.
    Each object has a key of one word with a letter ommited and the values are
    words that have the same letters as the key.
    For example: {"*ARS": ['MARS']}
    '''
    for word in words: #iterate through words array
        for i, j in enumerate(word): #get index as well as the word from word
            wordsRhyme = word[:i] + '*' + word[i+1:] #change one letter of the word with *. Ex:'*ARS'
            if wordsRhyme in dictionary: #if the word with a * is in dictionary
                dictionary[wordsRhyme].append(word) #add new word to dictionary as an object
            else:
                dictionary[wordsRhyme] = [word] #else add full word as value to key

    '''
    Create vertices and edges of words that rhyme
    '''
    for wordsRhyme in dictionary.keys(): #iterate through the keys in the dictionary object
        for startingWord in dictionary[wordsRhyme]: #get 1st values of key and make node of graph
            for endingWord in dictionary[wordsRhyme]: #get 2nd value of key
                if startingWord != endingWord: # if the two words are not the same
                    dictGraph[startingWord].add(endingWord) #Create edge - add the word that rhyme to one array.
                    dictGraph[endingWord].add(startingWord) #Create edge - add the word that rhyme to one array.

    return dictGraph

'''
Function trys to find a path in the graph based on the vertex and edge of each node.
In order to know in which node to start is take the Startig Node as a parameter it finds the word
in the grpah and then it takes that Node as the starting point.
To keep track of which node is being visited a set() is usedself.
To keep track of which edge to visit next a queue is used.
'''
def findPath(dictGraph, startingWord):
    queue = deque([[startingWord]]) #list container that appends adjacent edges
    nodesChecked = set() #stores which node have already been visited

    while queue: #continues through loop until ther eis no more edge to visit
        path = queue.popleft() #Remove and return an element from the left side of the deque.
        currentVertex = path[-1] #gets the current vertex that has been visited
        yield currentVertex, path # return the currentVertex, and the path
        for edge in dictGraph[currentVertex] - nodesChecked: #get the edges of the current set
            nodesChecked.add(edge) #once node is checked add to the set
            queue.append(path + [edge]) #add new edge to the queue and path

'''
Function loop through possible path graphs depending on two different words, the starting word
and the ending word.
If it finds a path then it transforms the set into a readable string.
'''
def displayPath(dictGraph, startingWord, endingWord):
    finalPath = ''
    for edge, path in findPath(dictionaryGraph, startingWord):
        if edge == endingWord: #if the edge is the same as the endingWord then a path is found
            finalPath = ' -> '.join(map(str, path)) #make path readable

    #check to see if a path was created.
    #if there was not path displays a message that there was no path else it display the path
    if path == '':
        print ('There is no path')
    else:
        print finalPath


'''
Ask the user for a new word to add to the dictionary
'''
def getUsrInput():
    startingWord = raw_input("Enter the starting 4 letter word: ")
    endingWord = raw_input("Enter the ending a 4 letter word: ")
    isReady = False

    while isReady == False:
        if len(startingWord) == 4 and len(endingWord) == 4:
            isReady = True
            isWordInDictionary(startingWord.upper(), endingWord.upper())
            return startingWord.upper(), endingWord.upper()
        else:
            print ("Words must be 4 letters")
            startingWord = raw_input("Enter the starting 4 letter word: ")
            endingWord = raw_input("Enter the ending a 4 letter word: ")

'''
Checks if a word is in and array that holds the dictionary words.
If the word is not in the array then it appends the word to the array
'''
def isWordInDictionary(startingWord, endingWord):
    dicArray = [
    'WARM',
    'COLD',
    'CARE',
    'TALL',
    'BOLD',
    'MARS',
    'TARS',
    'TOLD',
    'TOLL',
    'ABLE',
    'TARE',
    'CAFE',
    'DABS',
    'REST',
    'MORE',
    'LESS',
    'DOTS',
    'BURN',
    'CHEW',
    'ZAGS',
    'YALE',
    'WAFT',
    'WANY',
    'VAIN',
    'WHIP',
    'TREE',
    'RUDE',
    'DOOR',
    'CARS',
    ]

    for word in dicArray:
        if not startingWord in dicArray:
            dicArray.append(startingWord)
        if not endingWord in dicArray:
            dicArray.append(endingWord)

    return dicArray

if __name__ == '__main__':
    words = getUsrInput()
    time.sleep(1)
    print ('')
    print ('Starting word is: ' + words[0])
    print ('Ending word is: ' + words[1])
    dictionaryGraph = getGraph(isWordInDictionary(words[0], words[1]))
    displayPath(dictionaryGraph, words[0], words[1])
