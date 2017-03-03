'''
Jenny Tso
Python Program
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

x = (a + b) - (c + 1)   #1.0
y = float((a * b) % 5)  #2.0
z = int(a * (b / c))    #2

if (a == "ham") and (x == "jam"):
    print("Camelot! ...It's only a model.")
elif ((y > 3) and (y < 5)) or (z == "spam"):
    print("We eat ham and jam and Spam a lot!")
elif not z == "pram":
    print("He was not at all afraid \nTo be killed in nasty ways!")
else:    
    print("On second thought, let's not go to Camelot. It is a silly place.")

i = 0
while i < 3:
    print("Brave, ")
    i += 1

print epithet + "\n"

print("He was not in the least bit scared ")

grievousBodilyHarm_list = ["To be mashed into a pulp!", "Or to have his eyes gouged out, ",
                      "And his elbows broken. ", "To have his kneecaps split, ",
                      "And his body burned away, ", "And his limbs all hacked and mangled, "]

j = 0
harm = grievousBodilyHarm_list[j]

for harm in grievousBodilyHarm_list:
    print harm

print epithet + "\n"

moreHarm_tuple = ("His head smashed in", "And his heart cut out", "And his liver removed", "And his bowels unplugged",
                  "And his nostrils raped","And his bottom burnt off","And his penis--")

def tooSilly():
    target = "this program"
    stop = "stop that! "
    silly = target + " is too silly"
    interrupt = stop + stop + silly + "!"
    return interrupt

k = 0
moreHarm = moreHarm_tuple[k]

for moreHarm in moreHarm_tuple:
    print moreHarm
    k += 1
    if k > 6:
        print tooSilly().upper() 

