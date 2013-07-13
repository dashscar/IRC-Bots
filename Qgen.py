import random
tenper = random.randrange(1,11)
fifiy = random.randrange(1,3)
print fifiy
quote = '"'
def part1(rand10 = random.randrange(1,11), rand2 = random.randrange(1,3)):
    result = ''
    Sciencething = ['grains of sand', 'atoms', 'brains', 'bodies', 'gigabytes']
    Species = ['humans', 'monkeys']
    if rand10 % 2 == 0:
        result += '"There are '
        if rand2 % 2 == 0:
            result += 'less '
        else:
            result += 'more '
        result += random.choice(Sciencething)
        case = 1
    else:
        result += '"If '
        result += random.choice(Species)
        case = 2
    return result, case
quote += str(part1())
#def part2(rand10, rand2)
print quote
