from random import randint


#Interactions Between Functions Practice #1
# Create a function (throw_dice) that "throws" two random dice and returns its results (the function MUST RETURN TWO VALUES AS A RESULT, both of which must be between 1 and 6, randomly).

def throw_dice():
  dice1 = randint(1,6)
  dice2 = randint(1,6)
  return dice1, dice2
dice1 = throw_dice()
dice2 = throw_dice()
def roll_result(a_dice1,a_dice2):
  sum = dice1 + dice2
  if sum < 6 or sum == 6:
    print(f"The sum of your dice is {sum}. Unfortunate")
  elif sum > 6 and sum > 10:
    print(f"The sum of your dice is {sum}. You have a good chance")
  elif sum > 10 or sum == 10:
    print(f"The sum of your dice is {sum}. It looks like a winning roll")


roll_result(dice1,dice2)
  # Pass the result of these two dice to a function called roll_result (meaning that this second function MUST RECEIVE TWO ARGUMENTS) and return -without printing it- a certain message according to the what the sum of these values results:

# If the sum is less than or equal to 6:

# "The sum of your dice is {sum_dice}. Unfortunate"

# If the sum is greater than 6 and less than 10:

# "The sum of your dice is {sum_dice}. You have a good chance"

# If the sum is greater than or equal to 10:

# "The sum of your dice is {sum_dice}. It looks like a winning roll"

# Hint: use the random library's choice or randint method to choose a random value between 1 and 6.

#   "The sum of your dice is {suma_dados}. Unfortunate"
# "The sum of your dice is {suma_dados}. You have a good chance"
# "The sum of your dice is {sum_dice}. It looks like a winning roll"




  
#####################################################################################################

# Interactions Between Functions Practice #2
# Create a function called reduce_list() that takes a list (numbers) as an argument, and returns also a list, but removing duplicates (leaving only one of the numbers if there are duplicates) and removing the highest value. The order of the elements can be changed.

# For example, if given the list [1,2,15,7,2] it should return [1,2,7].
aList = int(input("Number 1: "))
aList2 = int(input("Number 2: "))
aList3 = int(input("Number 3: "))
aList4 = int(input("Number 4: "))
aList5 = int(input("Number 5: "))
fullList = [aList, aList2, aList3, aList4, aList5]
def reduce_list():
  print(f"List: {fullList}")
  res = [*set(fullList)]
  print(f"List without duplicates: {res}")
  fullList.sort()
  trimmed = fullList[:-1]
  print(f"List without maximum value: {trimmed}")

reduce_list()
# Create a function called average() that can receive as an argument the list returned by the previous function, and that calculates the average of its values. It should return the result (a float), without printing it.
def average():
  avg = (aList + aList2 + aList3 + aList4 + aList5) / 5
  print(f"avergage of list is {avg}")

average()
  




#####################################################################################################
# Interactions Between Functions Practice #3
# You must create a list with values and call it secret_codes.
secret_codes = []
# Create a function called toss_coin that returns the result of a random coin toss. Such a function must be able to return the results "Heads" or "Tails", and must not receive any arguments to work.

# Create a second function called luck, that takes two arguments: the first must be the result of the coin toss. The second argument will be any list (the secret_codes variable that was created at the beginning).

# If the coin comes up "Tails", luck should print this message to the user: "List will self-destruct", and return said list as empty list = [ ].

# If the coin comes up "Heads", it should print to the screen: "List was saved" and return the list intact.

# Hint: Use the random library's choice method to choose an element at random from a sequence.