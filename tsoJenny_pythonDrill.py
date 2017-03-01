'''
Jenny Tso
Python Program Drill
Gosh, we're all really impressed.

'''

knight = "Sir Robin"
epithet = "Brave " + knight +"!"
kingdom = "Camelot"
song = "Brave " + knight

print song
print("\n\nBravely, bold {} \nRode forth from {}. \nHe was not afraid to die, \nO, brave {}!".format(knight,kingdom,knight))

a = 3
b = 4
c = 5.0
x = int((a + b) - c)
y = (a * (b / c))
z = (x * y) % 5

a += 4

if (a == 1) and (x == 2):
    print("Camelot! ...It's only a model.")
elif (b < 3) or (y == 4):
    print("We eat ham and jam and Spam a lot!")
elif not z > 7.0:
    print("He was not at all afraid \nTo be killed in nasty ways!")
else:    
    print("On second thought, let's not go to Camelot. It is a silly place.")

i = 1
for i in range(3):
    print("Brave, ")

print epithet + "\n"

print("He was not in the least bit scared ")

grievousBodilyHarm = ["To be mashed into a pulp!", "Or to have his eyes gouged out, ",
                      "And his elbows broken. ", "To have his kneecaps split, ",
                      "And his body burned away, ", "And his limbs all hacked and mangled, "]

j = 0
while j < len(grievousBodilyHarm):
    print grievousBodilyHarm[j]
    j += 1

print epithet + "\n"

moreHarm_tuple = ("His head smashed in", "And his heart cut out", "And his liver removed", "And his bowels unplugged",
                  "And his nostrils raped","And his bottom burnt off","And his penis--")

k = 0
while k < len(moreHarm_tuple):
    print moreHarm_tuple[k]
    k += 1

def tooSilly():
    target = "this program"
    stop = "stop that! "
    silly = target + " is too silly"
    return stop + stop + silly + "!"

print tooSilly().upper()


