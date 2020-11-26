#34 Write a program that reads an integer from the user. Then your program should
display a message indicating whether the integer is even or odd

number = int(input("Please enter an integer: "))

if number % 2 == 0:
	print("This number is even.")
else:
	print("The number is odd")
----------------------------
  
#35 It is commonly said that one human year is equivalent to 7 dog years. However this
simple conversion fails to recognize that dogs reach adulthood in approximately two
years. As a result, some people believe that it is better to count each of the first two
human years as 10.5 dog years, and then count each additional human year as 4 dog
years. Write a program that implements the conversion from human years to dog years
described in the previous paragraph. Ensure that your program works correctly for
conversions of less than two human years and for conversions of two or more human
years. Your program should display an appropriate error message if the user enters
a negative number.

humanYearsOld = int(input("Please enter the age of a dog in human years: "))

humanYearsOld = 0

if humanYearsOld <= 2:
	dogYears = humanYearsOld * 10.5
elif humanYearsOld > 2:
	dogYears = 2 * 10.5
	dogYears += (humanYearsOld-2) * 4

if humanYearsOld == 0:
	print("Please enter a positive integer.")
else:
	print("The dog is {} years old in dog years.".format(dogYears))
------------------------------------------------------------------

#36 In this exercise you will create a program that reads a letter of the alphabet from the
user. If the user enters a, e, i, o or u then your program should display a message
indicating that the entered letter is a vowel. If the user enters y then your program
should display a message indicating that sometimes y is a vowel, and sometimes y is
a consonant. Otherwise your program should display a message indicating that the
letter is a consonant.

letter = input("Please enter a letter of the alphabet: ")

if letter in "aeiou":
	print("This letter is a vowel.")
else:
	print("This letter is a consonant.")
---------------------------------------

#37 Write a program that determines the name of a shape from its number of sides. Read
the number of sides from the user and then report the appropriate name as part of
a meaningful message. Your program should support shapes with anywhere from 3
up to (and including) 10 sides. If a number of sides outside of this range is entered
then your program should display an appropriate error message.
noOfSides = int(input("Please enter the number of sides of a shape: "))

if noOfSides == 3:
	print("That's a triangle.")
elif noOfSides == 4:
	print("That's a square.")
elif noOfSides == 5:
	print("That's a pentagon.")
elif noOfSides == 6:
	print("That's a hexagon.")
elif noOfSides == 7:
	print("That's a heptagon.")
elif noOfSides == 8:
	print("That's a octagon.")
elif noOfSides == 9:
	print("That's a nonagon.")
elif noOfSides == 10:
	print("That's a decagon")
else:
	print("Please enter an integer greater than 2")
--------------------------------------------------

#38 The length of a month varies from 28 to 31 days. In this exercise you will create
a program that reads the name of a month from the user as a string. Then your
program should display the number of days in that month. Display “28 or 29 days”
for February so that leap years are addressed.

month = input("Please enter the name of a month: ")
month = month.lower()

if month == "september" or month == "april" or month == "june" or month == "november":
	print("There are 30 days in this month.")
elif month == "february":
	print("There are 28 or 29 days in this month.")
else:
	print("There are 31 days in this month.") 
  ------------------------------------------
  
#39  The following table lists the sound level in decibels for several common noises. Write a program that reads a sound level in decibels from the user. If the user
enters a decibel level that matches one of the noises in the table then your program
should display a message containing only that noise. If the user enters a number
of decibels between the noises listed then your program should display a message
indicating which noises the level is between. Ensure that your program also generates
reasonable output for a value smaller than the quietest noise in the table, and for a
value larger than the loudest noise in the table.

dbLevel = float(input("Please enter a dB level: "))

if dbLevel < 40:
	print("This is extremely quite.")
elif dbLevel > 130:
	print("This is extremely loud.")


if dbLevel > 40:
	print("This is between a quiet room and an alram clock.")
elif dbLevel > 70:
	print("This is between an alarm clock and a gas lawnmower.")
elif dbLevel > 106:
	print("This is between a gas lawnmower and a jackhammer.")

if dbLevel == 40:
	print("This is a quiet room.")
elif dbLevel == 70:
	print("This is an alarm clock.")
elif dbLevel == 106:
	print("This is a gas lawnmower.")
elif dbLevel == 130:
	print("This is a jackhammer.")
  -------------------------------------
 #40 A triangle can be classified based on the lengths of its sides as equilateral, isosceles
or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
triangle has two sides that are the same length, and a third side that is a different
length. If all of the sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of 3 sides of a triangle from the user.
Display a message indicating the type of the triangle.

side1 = float(input("Please enter the length of first side of a triangle: "))
side2 = float(input("Please enter the length of the second side of the triangle: "))
side3 = float(input("Please enter the length of the third side of the triangle: "))

triangleType = ""

if side1 == side2 == side3:
	triangleType = "equalateral"
elif side1 == side2 or side1 == side3 or side2 == side3:
	triangleType = "isoseles"
else:
	triangleType = "scalene"

print("That is a {} triangle.".format(triangleType)
----------------------------------------------------

#41 The following table lists an octave of music notes, beginning with middle C, along
with their frequencies. Begin by writing a program that reads the name of a note from the user and
displays the note’s frequency. Your program should support all of the notes listed
previously.
Once you have your program working correctly for the notes listed previously you
should add support for all of the notes from C0 to C8. While this could be done by
adding many additional cases to your if statement, such a solution is cumbersome,
inelegant and unacceptable for the purposes of this exercise. Instead, you should
exploit the relationship between notes in adjacent octaves. In particular, the frequency
of any note in octave n is half the frequency of the corresponding note in octave n+1.
By using this relationship, you should be able to add support for the additional notes
without adding additional cases to your if statement.

noteAndOctave = input("Please enter a musical note: ")

# Notes are written in the form note, octave eg. C4
note = noteAndOctave[0]
octave = int(noteAndOctave[1])

note = note.upper()

frequency = -1

if note == "C":
	frequency = 261.63
elif note == "D":
	frequency = 293.66
elif note == "E":
	frequency = 329.63
elif note == "F":
	frequency = 349.23
elif note == "G":
	frequency = 392.00
elif note == "A":
	frequency = 440.00
elif note == "B":
	frequency = 493.88

frequency /= 2 ** (4 - octave) # Formula to find the frequency in a different octave

print("The note's frequency is {}Hz".format(frequency))
------------------------------------------------------
#42 In the previous question you converted from note name to frequency. In this question
you will write a program that reverses that process. Begin by reading a frequency
from the user. If the frequency is within one Hertz of a value listed in the table in
the previous question then report the name of the note. Otherwise report that the
frequency does not correspond to a known note. In this exercise you only need to
consider the notes listed in the table. There is no need to consider notes from other
octaves.

frequency = float(input("Please enter a frequency in Hertz: "))

note = ""

if frequency > 261.63 - 1 and frequency < 261.63 + 1:
	note = "C"
elif frequency > 293.66 - 1 and frequency < 293.66 + 1:
	note = "D"
elif frequency > 329.63 - 1 and frequency < 329.63 + 1:
	note = "E"
elif frequency > 349.23 - 1 and frequency < 349.23 + 1:
	note = "F"
elif frequency > 392.00 - 1 and frequency < 392.00 + 1:
	note = "G"
elif frequency > 440.00 - 1 and frequency < 440.00 + 1:
	note = "A"
elif frequency > 493.88 - 1 and frequency < 493.88 + 1:
	note = "B"

if note == "":
	print("This is not an in tune note.")
else:
	print("This is a {} note.".format(note))
-------------------------------------------

# 43 It is common for images of a country’s previous leaders, or other individuals of his-
torical significance, to appear on its money. The individuals that appear on banknotes
in the United States are listed in Table 2.1. 
Write a program that begins by reading the denomination of a banknote from the
user. Then your program should display the name of the individual that appears on the 
banknote of the entered amount. An appropriate error message should be displayed
if no such note exists.

bankNoteAmount = int(input("Please enter a bank note amount: $"))

individualName = ""

if bankNoteAmount == 1:
	individualName = "George Washington"
if bankNoteAmount == 2:
	individualName = "Thomas Jefferson"
if bankNoteAmount == 5:
	individualName = "Abraham Lincoln"
if bankNoteAmount == 10:
	individualName = "Alexander Hamilton"
if bankNoteAmount == 20:
	individualName = "Andrew Jackson"
if bankNoteAmount == 50:
	individualName = "Ulysses S. Grant"
if bankNoteAmount == 100:
	individualName = "Benjamin Franklin"

if individualName == "":
	print("That is not an American bank note in circulation.")
else:
	print("The individual on this bank note is {}.".format(individualName))
      -----------------------------------------------------------------------
      
    # Get a name from the user, e.g. “Bob”, then output a greeting of the form “Hello Bob!”.
      
      public String helloName(String name)
{	return ("Hello " + name + '!');	}
      -------------------------------------
      
    # Given two strings, a and b, return the result of putting them together in the order abba,
     e.g. "Hi" and "Bye" returns "HiByeByeHi".

      public String makeAbba(String a, String b)
{	return (a+b+b+a);	}
      -----------------------------
      
      # The web is built with HTML strings like “<i>Yay</i>” which draws Yay as italic text. 
      # In this example, the “i” tag makes <i> and </i> which surround the word “Yay”. 
      # Ask the user for a tag string, then ask the user for a word string. 
      # Print out the HTML string with tags around the word, e.g. “<i>Yay</i>”.
      
      public String makeTags(String tag, String word)
  {return ('<' + tag + '>' + word + '<' + '/' + tag + '>');}
   -------------------------------------------------------
      
      
 
