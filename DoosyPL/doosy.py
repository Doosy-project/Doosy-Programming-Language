var=0
mlist=[]
newlist=[]
import random
def write(write):
    print(write)
def makevar(val):
    var=val
def addvar(val):
    var += val
def subvar(val):
    var -= val
def makelist():
    mlist=[]
def addtolist(add):
    mlist.append(add)
def removefromlist(sub):
    mlist.remove(sub)
def copylist():
    newlist = mlist.copy()
def comment(this):
    print('!' + this + '!')
def howto():
    print('====================DOOSY PROGRAMMING LANGUAGE=====================')
    print('write("write here") prints out whats in the ()')
    print('makevar("data") makes a variable with the value in the ()  -var-')
    print('addvar("this") adds whats in the () to a variable')
    print('subvar("there") subtracts from a variable with the value in the ()')
    print('makelist() makes a new list  -mlist-')
    print('addtolist("add to") adds whats in the () to a list')
    print('removefromlist("remove") takes whats in the () and removes it from the list')
    print('copylist() copys the list to a new one  -newlist-')
    print('comment("comment") makes a comment, not run by the code')
    print('howto() writes this!')
    print('importpypto() imports the pypto module, used for making cryptocurrency related things')
    print('importenterprise() imports the enterprise module, used for enterprise related things')
    print('importhydra() imports the hydra module')
    print('importfalafel() imports the falafel module')
def setup():
    print('DOOSY PROGRAMMING LANGUAGE VERSION 0.0.1')
    print('newfile')
    print('user ID ' + random.randint(11111111, 99999999))
    print('type howto() to learn how to use Doosy')
    print('program:')

setup()
def importpypto():
    import pyptomodules
def importenterprise():
    import enterprise
def importhydra():
    import hydra
def importcalcium():
    import calcium
def importfalafel():
    import falafel
