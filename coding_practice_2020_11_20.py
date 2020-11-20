#1 Create a program that will ask the user for their favourite colour. Have the program output a message saying something like: "Blue?! No why, that's my favourite colour too!".

colour = input("what is your favourite colour?: ")
print("Why {}.".format(colour))
------------------------------

#2 Create a program that asks how many cans come in a pack. Then ask the user how many packs there are. Output a message indicating the total number of cans.

Cans = int(input("Please enter the number of cans: "))
Packs = int(input("Please enter the number of packs: "))

Total_Cans = Cans * Packs

print("The total number of cans is {}.".format(Total_Cans))
------------------------------
#3 Ask the user for the three dimensions of a rectangular prism. Output the volume

width = int(input("Please enter the width of the prism: "))
length = int(input("Please enter the length of the prism: "))
height = int(input("please enter the height of the prism:"))

volume = width * length * height

print("The voulume of the prism is {}m.".format(volume))
----------------------------------------------------------
