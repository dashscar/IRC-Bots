import random
tenper = random.randrange(1,11)
fifiy = random.randrange(1,3)
quote = ''
Sciencething = ['grains of sand', 'atoms', 'brains', 'bodies', 'stars', 'electrons', 'molecules', 'software', 'itunes', 'music', 'songs', 'programs']
Species = ['humans', 'monkeys']
Person = ['Carl Sagan', 'Gandalf', 'Albert Einstein', 'Oprah', 'Steve Jobs', 'Obama', 'Bill Cosby', 'Darth Vader', 'Richard Stallman', 'Linus Torvalds']
Namecall = ['asshole', 'retard', 'faggot']
def part1(getcase = 0):
    rand10 = random.randrange(1,11)
    rand2 = random.randrange(1,3)
    result = ''
    if rand2 % 2 == 0:
        case = 1
        result += '"There are '
        if rand2 % 2 == 0:
            result += 'less '
        else:
            result += 'more '
        result += random.choice(Sciencething) + ' '
    elif rand2 % 2 != 0:
        case = 2
        result += '"If '
        result += random.choice(Species) + ' evolved from ' + random.choice(Species)
    if getcase == 1:
        return case
    elif getcase == 0:
        return result

def part2(getcase = 0):
    rand1 = random.randrange(1,11)
    rand2 = random.randrange(1,3) 
    result = part1()
    #print part1(1)
    #print result
    if part1(1) == 1:
        if rand2 % 2 ==0:
            result += 'in your '
        else:
            result += 'in all the '
        result += random.choice(Sciencething) + ' than there are ' + random.choice(Sciencething) + ' in all the ' + random.choice(Sciencething) + '"'
        case = 1
    if part1(1) == 2:
        result += ' than why do ' + random.choice(Species)
        if rand2 % 2 == 0:
            result += ' not'
        result += ' look like ' + random.choice(Species)
        if rand1 % 5 == 0:
            result += ', you ' + random.choice(Namecall)
        result += '?"'
    if getcase == 1:
            return case
        else:
        return result
def attribute():
    result = ' -'
    result += random.choice(Person)
    return result
#while True:
quote = str(part2()) + attribute()
print quote

