from random import choice
from random import randrange
tenper = randrange(1,11)
fifiy = randrange(1,3)
quote = ''

PreWrittenQuotes = ["One, two, three, four, let me hear you scream if you want some more! Like uhh, push it, push it, watch me work it, I'm perfect!", 
                    'Has anyone really been so far as to go look as decided for?',
                    'Do you even lift?',
                    "They don't think it be like it is, but it do",
                    "Deal with it"]

EvolveVerb = ['evolved', 'come']
Sciencething = ['grains of sand', 'atoms', 'brains', 'bodies', 'stars', 'electrons', 'molecules', 'software', 'music', 'songs', 'programs']
Species = ['dogs', 'cats', 'whales', 'chickens', 'dolphins']
EvSpecies = ['humans', 'monkeys', choice(Species)]
CharactersOnly = ['Spock', 'Harry', 'Neo', 'Luke', 'Gandalf', 'Darth Vader']
Person = [choice(CharactersOnly), 'Carl Sagan', 'Albert Einstein', 'Oprah', 'Steve Jobs', 'Obama', 'Bill Cosby', 'Richard Stallman', 'Linus Torvalds']
Namecall = ['asshole', 'retard', 'faggot']
Entire = ['an entire inch', 'the entire world', 'the entire universe', 'the whole galaxy', 'an entire building', 'a whole continent']
Teleken = ['force', 'death grip', 'mind meld']
EndSentence = ['!', '?', '?!', '.', '!1!1!!!11!!', '!!111!!11!', '???', '!!!']
ListRand = [choice(Sciencething), choice(EvSpecies)]

def quote1():
    #rand1 = randrange (1,11)
    result = 'If ' + choice(EvSpecies) + ' ' + choice(EvolveVerb) + ' from ' + choice(EvSpecies)
    result +=' then ' + choice(EvSpecies) + ' must have ' + choice(EvolveVerb) + ' from ' +  choice(EvSpecies)
    return result

def quote2():
    #rand1 = randrange(1,11)
    Lrand2 = [choice(Entire), choice(ListRand)]
    morl = ['more ', 'less ']
    result = 'There are ' + choice(morl) + choice(Sciencething) + ' in ' + choice(Lrand2)
    result +=' than there are ' + choice(ListRand) + ' in ' + choice(Lrand2)
    return result

def quote3():
    result = 'Did you know that if you take ' + str(randrange(1,1000)) + ' ' + choice(ListRand) + ", and put them together, they'd fill up all the space in " + choice(Entire) + '?'
    return result
def quote4():
    result = 'Use the ' + choice(Teleken) + ' ' + choice(CharactersOnly) + choice(EndSentence)
    return result

ChooseQ = [quote1(), quote2(), quote3(), quote4()]

print '"' + choice([choice(PreWrittenQuotes)] + [choice(ChooseQ)] * 10 ) + '" -' + choice(Person)
