# --------------------------------------
# CSCI 127, Lab 5                      |
# Month 9, 2021                    |
# Tiegan Cozzie                       |
# -------------------------------------- 
# Calculate how many vowels are in a   |
# sentence using three techniques.     |
# --------------------------------------
vowels=["a","e","i","o","u"]
def count_built_in(sentence):
    ans=sentence.count(vowels[0])+sentence.count(vowels[1])+sentence.count(vowels[2])+sentence.count(vowels[3])+sentence.count(vowels[4])
    return ans

def count_iterative(sentence):
    count=0
    for x in range(0,len(sentence)):
        if sentence[x] in vowels:
            count+=1
    return count
    
def is_vowel(letter):
    if letter in vowels:
        return 1
    else:
        return 0
    
def count_recursive(sentence):
    if len(sentence)==0:
        return 0
    elif is_vowel(sentence[0])==1:
        return 1 + count_recursive(sentence[1:])
    elif is_vowel(sentence[0])==0:
        return 0 + count_recursive(sentence[1:])
            

# --------------------------------------

def main():
    answer = "yes"
    while (answer == "yes") or (answer == "y"):
        sentence = input("Please enter a sentence: ")
        sentence = sentence.lower()
        print()
        print("Calculating the number of vowels  using ...")
        print("-------------------------------------------")
        print("Built-in function =", count_built_in(sentence))
        print("Iteration =", count_iterative(sentence))
        print("Recursion =", count_recursive(sentence))
        print()
        answer = input("Would you like to continue: ").lower()
        print()

# --------------------------------------

main()
