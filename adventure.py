from data import locations
from data import descriptions
from data import objects

directions = {
    'west': (-1, 0),
    'east': (1, 0),
    'north': (0, -1),
    'south': (0, 1),
}

map = ['H', 'P', 'L', 'M']

position = (0, 0)
pocket = []

while True:
    location = locations[position]
    description = descriptions[location]
    object = objects[location]

    print 'you are at the %s ' % description,
    print ' and have %s in Your pocket' % pocket
    print ' There are such objects You can pick: %s' % object
    choice = []
    while  choice not in object:
        choice = raw_input('What do You pick from the location ?')
    print 'You picked %s' % choice
    pocket.append(choice)


    valid_directions = {}
    for k, v in directions.iteritems():
        possible_position = (position[0] + v[0], position[1] + v[1])
        # print possible_position ,
        possible_location = locations.get(possible_position)
        # print possible_location
        if possible_location:
            print 'to the %s is a %s' % (k, possible_location)
            valid_directions[k] = possible_position

    # print valid_directions
    direction = ''
    while direction not in valid_directions:
        direction = raw_input('which direction do you want to go?\n')

    position = valid_directions[direction]

    pos_short = locations[position]
    position_short = pos_short[0].upper()

    for place in map:
        # print place, position_short
        if place == position_short:
            print ' ',
        else:
            print place,
        if place == 'P':
            print
    print

