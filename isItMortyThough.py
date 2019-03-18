#How does Rick tell if Morty is a simulation?
##Rick will question if it's Morty 
isItMorty = 1
##Populate with responses from Morty
mortyResponses = ['Nothing, geez Rick','Okay, this is getting weird',
                   'If everyone is going to be crazy, then let me be crazy with Jessica']
##Populate with Rick Questions
rickdiculousQuestions = ['This is just sloppy craftsmanship','Whatever quote unquote, Morty?',
                         'Oh wow, responsive. You guys really went all out.']
##Counter to move through the rickdiculousQuestions.
counter = 0
##while these two are between 1 and 99 
while isItMorty < 100 and isItMorty >0:
##getting an if/elif/else statement
    askQuestion = input(rickdiculousQuestions[0+counter])
    counter+=1
    if askQuestion in mortyResponses:
        isItMorty += 33
    else:
        isItMorty = 0
        
##Failed the Morty Test      
if isItMorty == 0:
    print('''Rick shows up as Morty is asleep''')
    print('burp, I knew you were a god---- simulation Morty.')
    print('Rick shoots Simulation Morty.')
##Passed the Morty Test
elif isItMorty == 100:
##The ones that captured Morty and Rick are 
    print('''Take off your clothes Morty, they won't listen to us\n while we're naked''')