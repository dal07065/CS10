# Lina Kang
# 1072568
# This program reads in "textabbv.txt" file and display it in a formatted manner

def createDict()->dict:
    '''Creates a dictionary based on the input from "textabbv.txt"'''
    infile = open('textabbv.txt', 'r')
    abbv = {}
    
    for line in infile:
        
        index = line.find(':')
        abbv[line[:index]] = line[index+1:]
        
    return abbv


def translate(word:str, abbv:dict)->str:
    '''Translates a given word based on the given dictionary'''
    
    for key in abbv:
        
        if word == key:
            return abbv[key]
        
    return word


def main():
    abbv = createDict()
    newString = "";
    
    print("Enter a message to be translated:")
    string = input("")
    list = string.split()
    
    for word in list:
        translatedWord = translate(word,abbv)
        translatedWord = translatedWord.rstrip('\n')
        
        newString = newString + translatedWord+ " "

    print("The translated text is: ")
    print(newString)


if __name__ == "__main__":
    main()

##Output with 5 Test Cases
##
##Test Case 1
##
##Enter a message to be translated:
##r u , lol ?
##The translated text is: 
##are you , laughing out loud ? 
##
##Test Case 2
##
##Enter a message to be translated:
##I have to go . ttyl !
##The translated text is: 
##I have to go . talk to you later ! 
##
##Test Case 3
##
##Enter a message to be translated:
##I know you are upset . But tldr . gtg :(
##The translated text is: 
##I know you are upset . But too long; didn't read . got to go :(
##
##Test Case 4
##
##Enter a message to be translated:
##I bet it hurt when you fell from heaven cuzz you are an angel
##The translated text is: 
##I bet it hurt when you fell from heaven because you are an angel 
##
##Test Case 5
##
##Enter a message to be translated:
##
##The translated text is:
##
