'''
Jenny Tso
Python Program
Gosh, we're all really impressed.

'''

# 2. Assign a string to a variable
knight = "Sir Robin"
epithet = "Brave " + knight +"!"
kingdom = "Camelot"
song = "Brave " + knight

print song

# 4. Use the print function and .format() notation to print out variables
print("\n\nBravely, bold {} \nRode forth from {}. \nHe was not afraid to die, \nO, brave {}!".format(knight,kingdom,knight))

# 1. Assign an integer to a variable
# 3. Assign a float to a variable
a = 3
b = 4
c = 5.0
# 5. Arithmetic operators
x = (a + b) - (c + 1) # Result is 1.0
y = float((a * b) % 5) # Result is 2.0
z = int(a * (b / c)) # Result is 2

# 6. Logical operators
# 7. Conditional statements
if (a == "ham") and (x == "jam"):
    print("Camelot! ...It's only a model.")
elif ((y > 3) and (y < 5)) or (z == "spam"):
    print("We eat ham and jam and Spam a lot!")
elif not z == "pram":
    print("He was not at all afraid \nTo be killed in nasty ways!")
else:    
    print("On second thought, let's not go to Camelot. It is a silly place.")

# 8. Use of a while loop
i = 0
while i < 3:
    print("Brave, ")
    i += 1

print epithet + "\n"

print("He was not in the least bit scared ")

# List
grievousBodilyHarm_list = ["To be mashed into a pulp!", "Or to have his eyes gouged out, ",
                      "And his elbows broken. ", "To have his kneecaps split, ",
                      "And his body burned away, ", "And his limbs all hacked and mangled, "]

# 9. Use of a for loop
# 10. Iterate through list with for loop
j = 0
harm = grievousBodilyHarm_list[j]

for harm in grievousBodilyHarm_list:
    print harm

print epithet + "\n"

# Tuple
moreHarm_tuple = ("His head smashed in", "And his heart cut out", "And his liver removed", "And his bowels unplugged",
                  "And his nostrils raped","And his bottom burnt off","And his penis--")

# 12. Function that returns a string
def tooSilly():
    target = "this program"
    stop = "stop that! "
    silly = target + " is too silly"
    interrupt = stop + stop + silly + "!"
    return interrupt

# 11. Iterate through tuple with for loop
k = 0
moreHarm = moreHarm_tuple[k]

for moreHarm in moreHarm_tuple:
    print moreHarm
    k += 1
    if k > 6:
# 13. Call function and print results to the shell
        print tooSilly().upper() 

