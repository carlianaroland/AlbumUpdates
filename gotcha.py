import copy
import ccroland_SimpleCalc1 as SC  # using the avg method in MyMath
the_weeknd = list()  # THIS WHOLE PROGRAM IS BASICALLY THE BACKBONE OF WHAT YOU NEED YOU JUST HAVE TO CALCULATE GRADES
album = dict()
print('The Weeknd Album Favorites')
the_weeknd.append('Thursday')  # the favorties
the_weeknd.append('Valerie')
the_weeknd.append('Wicked Games')

album.update({'Trilogy': copy.deepcopy(the_weeknd)})  # pass-by-reference / this makes another album of favorites
# the album names would the categories
the_weeknd.clear()  # clears the previous album for another album of favorites

the_weeknd.append('Kissland')  # the favorites
the_weeknd.append('Pretty')
the_weeknd.append('Wanderlust')

album.update({'Kissland': the_weeknd})
album.update({'Kissland': copy.deepcopy(the_weeknd)})  # pass-by-reference / makes album of favorites
the_weeknd.clear()  # clears previous for another album of favorites

the_weeknd.append('Often')  # the favorties
the_weeknd.append('Acquainted')
the_weeknd.append('Tell Your Friends')  # the songs would be grades

album.update({'Beauty Behind the Madness': the_weeknd})  # pass-by-reference / makes another album of favorites
# the rank.update would be a new category for grades
album.update({'Beauty Behind the Madness': copy.deepcopy(the_weeknd)})
the_weeknd.clear()

the_weeknd.append('Party Monster')
the_weeknd.append('Die For You')
the_weeknd.append('Six Feet Under')

album.update({'Starboy': the_weeknd})
album.update({'Starboy': copy.deepcopy(the_weeknd)})
the_weeknd.clear()

the_weeknd.append('Privilege')
the_weeknd.append('Try Me')
the_weeknd.append('I Was Never There')

album.update({'My Dear Melancholy,': the_weeknd})
album.update({'My Dear Melancholy,': copy.deepcopy(the_weeknd)})
the_weeknd.clear()

the_weeknd.append('Alone Again')
the_weeknd.append('Repeat After Me')
the_weeknd.append('Scared to Live')

album.update({'After Hours': the_weeknd})
album.update({'After Hours': copy.deepcopy(the_weeknd)})
the_weeknd.clear()

the_weeknd.append('I Heard You\'re Married')
the_weeknd.append('Out of Time')
the_weeknd.append('Sacrifice')

album.update({'Dawn FM': the_weeknd})
album.update({'Dawn FM': copy.deepcopy(the_weeknd)})
print(album)

# TODO: add grades divided by the amount of grades (SUM(GRADES) / LEN(GRADES))

# ALLOWED TO USE BUILT-IN FUNCTIONS / USE THE MYMATH DEFINITIONS FOR MATH


def myTeacup(cup):
    print(cup)
    if cup >= 3:
        return
    myTeacup(cup + 1)

myTeacup(0)
myTeacup(1)
myTeacup(2)
myTeacup(3)