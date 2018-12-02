#!/usr/bin/env python3

'''
Revature is building a new API! This API contains functions for validating data, 
solving problems, and encoding data. 

The API consists of 10 functions that you must implement.

Guidelines:
1) Edit the file to match your first name and last name with the format shown.

2) Provide tests in the main method for all functions, We should be able to run
this script and see the outputs in an organized manner.

3) You can leverage the operating system if needed, however, do not use any non
legacy command that solves the problem by just calling the command.

4) We believe in self commenting code, however, provide comments to your solutions
and be organized.

5) Leverage resources online if needed, but remember, be able to back your solutions
up since you can be asked.

6) Plagiarism is a serious issue, avoid it at all costs.

7) Don't import external libraries which are not python native

8) Don't change the parameters or returns, follow the directions.

9) Assignment is optional, but totally recommend to achieve before Monday for practice.

Happy Scripting!

© 2018 Revature. All rights reserved.
'''

'''
Use the main function for testing purposes and to show me results for all functions.
'''
def main():
	print("\nQuestion 1")
	print("----------")
	print(reverse(""))
	print(reverse("tobor"))
	print(reverse("nemaR"))
	print(reverse("!yrgnuh m'I"))
	print(reverse("racecar"))

	print("\nQuestion 2")
	print("----------")
	print(acronym("Portable Network Graphics"))
	print(acronym("First In, First Out"))
	print(acronym("GNU Image Manipulation Program"))
	print(acronym("Complementary metal-oxide semiconductor"))

	print("\nQuestion 3")
	print("----------")
	print(whichTriangle(5, 4, 6))
	print(whichTriangle(0.5, 0.5, 0.5))
	print(whichTriangle(2, 3, 4))
	print(whichTriangle(0.5, 0.4, 0.5))
	print(whichTriangle(4, 4, 4))
	print(whichTriangle(0.5, 0.4, 0.6))

	print("\nQuestion 4")
	print("----------")
	print(scrabble("f"))
	print(scrabble("zoo"))
	print(scrabble("street"))
	print(scrabble("quirky"))
	print(scrabble("OxyphenButazone"))

	print("\nQuestion 5")
	print("----------")
	print(armstrong(5))
	print(armstrong(10))
	print(armstrong(153))
	print(armstrong(100))
	print(armstrong(9474))

	print("\nQuestion 6")
	print("----------")
	print(primeFactors(2))
	print(primeFactors(9))
	print(primeFactors(8))
	print(primeFactors(12))
	print(primeFactors(901255))

	print("\nQuestion 7")
	print("----------")
	print(pangram(""))
	print(pangram("abcdefghijklmnopqrstuvwxyz"))
	print(pangram("the quick brown fox jumps over the lazy dog"))
	print(pangram("a quick movement of the enemy will jeopardize five gunboats"))
	print(pangram("five boxing wizards jump quickly at it"))

	print("\nQuestion 8")
	print("----------")
	print(sort([]))
	print(sort([2,4,5,1,3,1]))
	print(sort([89,144,634,8,34,21,1,3,233,55,5,377,13]))
	print(sort([4,6,3,9,11,3,1,8]))
	print(sort([48,86,52,46,34,95,76,83,48,66,83,41,52,47,80,10,51,49,20,1]))

	print("\nQuestion 9")
	print("----------")
	print(rotate(13, "n"))
	print(rotate(5, "OMG"))
	print(rotate(4, "Testing 1 2 3 testing"))
	print(rotate(21, "Let's eat, Grandma!"))
	print(rotate(13, "Gur dhvpx oebja sbk whzcf bire gur ynml qbt."))

	print("\nQuestion 10")
	print("----------")
	evenAndOdds()

'''
1. Reverse a String. Example: reverse("example"); -> "elpmaxe"

Rules:
- Do NOT use built-in tools
- Reverse it your own way

param: str
return: str
'''
def reverse(string : str):
	return string[::-1]

'''
2. Convert a phrase to its acronym. Techies love their TLA (Three Letter
Acronyms)! Help generate some jargon by writing a program that converts a
long name like Portable Network Graphics to its acronym (PNG).

param: str
return: str
'''
def acronym(phrase : str):
	return "".join(word[0].upper() for word in phrase.replace("-", " ").split(" "))

'''
3. Determine if a triangle is equilateral, isosceles, or scalene. An
equilateral triangle has all three sides the same length. An isosceles
triangle has at least two sides the same length. (It is sometimes specified
as having exactly two sides the same length, but for the purposes of this
exercise we'll say at least two.) A scalene triangle has all sides of
different lengths.

param: float, float, float
return: str -> 'equilateral', 'isoceles', 'scalene'
'''
def whichTriangle(sideOne : float, sideTwo : float, sideThree : float):
	return "equilateral" if sideOne == sideTwo and sideTwo == sideThree else "isoceles" if sideOne == sideTwo or sideTwo == sideThree or sideThree == sideOne else "scalene"

'''
4. Given a word, compute the scrabble score for that word.

--Letter Values-- Letter Value A, E, I, O, U, L, N, R, S, T = 1; D, G = 2; B,
C, M, P = 3; F, H, V, W, Y = 4; K = 5; J, X = 8; Q, Z = 10; Examples
"cabbage" should be scored as worth 14 points:

3 points for C, 1 point for A, twice 3 points for B, twice 2 points for G, 1
point for E And to total:

3 + 2*1 + 2*3 + 2 + 1 = 3 + 2 + 6 + 3 = 5 + 9 = 14

param: str
return: int
'''
def scrabble(word : str):
	return sum([1 if c in "AEIOULNRST" else 2 if c in "DG" else 3 if c in "BCMP" else 4 if c in "FHVWY" else 8 if c in "JX" else 10 if c in "QZ" else 5 for c in list(word.upper())])

'''
5. An Armstrong number is a number that is the sum of its own digits each
raised to the power of the number of digits.

For example:

9 is an Armstrong number, because 9 = 9^1 = 9 10 is not an Armstrong number,
because 10 != 1^2 + 0^2 = 2 153 is an Armstrong number, because: 153 = 1^3 +
5^3 + 3^3 = 1 + 125 + 27 = 153 154 is not an Armstrong number, because: 154
!= 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190 Write some code to determine whether
a number is an Armstrong number.

param: int
return: bool
'''
def armstrong(number : int):
	return number == sum([pow((number // pow(10, i) - number // pow(10, i + 1) * 10), len(str(number))) for i in range(len(str(number)), -1, -1)])

'''
6. Compute the prime factors of a given natural number.

A prime number is only evenly divisible by itself and 1.
 
Note that 1 is not a prime number.

param: int
return: list
'''
def primeFactors(number: int):
	factors = []
	factor = 2
	while(number != 1):
		if(number % factor == 0):
			factors.append(factor)
			number //= factor
		else:
			factor += 1
	return factors

'''
7. Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan
gramma, "every letter") is a sentence using every letter of the alphabet at
least once. The best known English pangram is:

The quick brown fox jumps over the lazy dog.
 
The alphabet used consists of ASCII letters a to z, inclusive, and is case
insensitive. Input will not contain non-ASCII symbols.
 
param: str
return: bool
'''
def pangram(sentence : str):
	for x in range(97, 123):
		if chr(x) not in sentence.strip(" ").lower():
			return False
	return True

'''
8. Sort list of integers.
f([2,4,5,1,3,1]) = [1,1,2,3,4,5]

Rules:
- Do NOT sort it with .sort() or sorted(list) or any built-in tools.
- Sort it your own way

param: list
return: list
'''
def sort(numbers: list):
	sortedList = []
	while(len(numbers) != 0):
		sortedList.append(min(numbers))
		numbers.remove(min(numbers))
	return sortedList

'''
9. Create an implementation of the rotational cipher, also sometimes called
the Caesar cipher.

The Caesar cipher is a simple shift cipher that relies on transposing all the
letters in the alphabet using an integer key between 0 and 26. Using a key of
0 or 26 will always yield the same output due to modular arithmetic. The
letter is shifted for as many values as the value of the key.

The general notation for rotational ciphers is ROT + <key>. The most commonly
used rotational cipher is ROT13.

A ROT13 on the Latin alphabet would be as follows:

Plain: abcdefghijklmnopqrstuvwxyz Cipher: nopqrstuvwxyzabcdefghijklm It is
stronger than the Atbash cipher because it has 27 possible keys, and 25
usable keys.

Ciphertext is written out in the same formatting as the input including
spaces and punctuation.

Examples: ROT5 omg gives trl ROT0 c gives c ROT26 Cool gives Cool ROT13 The
quick brown fox jumps over the lazy dog. gives Gur dhvpx oebja sbk whzcf bire
gur ynml qbt. ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. gives The
quick brown fox jumps over the lazy dog.

param: int, str
return: str
'''
def rotate(key: int, string: str):
	ciphertext = ""
	for c in string:
		if ord(c) >= 65 and ord(c) <= 90:
			ciphertext += chr(ord(c) + key - 26) if ord(c) + key > 90 else chr(ord(c) + key)
		elif ord(c) >= 97 and ord(c) <= 122:
			ciphertext += chr(ord(c) + key - 26) if ord(c) + key > 122 else chr(ord(c) + key)
		else:
			ciphertext += c
	return ciphertext

'''
10. Take 10 numbers as input from the user and store all the even numbers in a file called even.txt and
the odd numbers in a file called odd.txt.

param: none, from the keyboard
return: nothing
'''
def evenAndOdds():
	numbers = [int(input()) for x in range(10)]
	with open("even.txt", "w") as e, open("odd.txt", "w") as o:
		for n in numbers:
			if n % 2 == 0:
				e.write("{}\n".format(n))
			else:
				o.write("{}\n".format(n))

if __name__ == "__main__":
    main()
