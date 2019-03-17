
#How does Rick tell if Morty is a simulation?

##Is it Morty though? Start with 1,
##Since Rick is curious enough to question it.
isItMorty = 1
##Filled with possibile answers of Morty, can be added to
normalResponses = ['Nothing, geez Rick','Okay, this is getting weird',
                   'If everyone is going to be crazy, then let me be crazy with Jessica']
rickdiculousQuestions = ['This is just sloppy craftsmanship','Whatever quote unquote, Morty?',
                         'Oh wow, responsive. You guys really went all out.']
counter = 0
##while these two are 
while isItMorty < 100 and isItMorty >0:
    askRickdiculousQuestion = input(rickdiculousQuestions[0+counter])
    counter+=1
    if askRickdiculousQuestion in normalResponses:
        isItMorty += 33
    else:
        isItMorty = 0
        
##Failed the Morty Test      
if isItMorty == 0:
    print('''Rick shows up as Morty is asleep''')
    print('burp, I knew you were a god---- simulation Morty.')
    print('Rick shoots Simulation Morty.')
elif isItMorty == 100:
##The ones that captured Morty and Rick are 
    print('''Take off your clothes Morty, they won't listen to us\n while we're naked''')