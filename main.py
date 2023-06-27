#Create a function that grabs the email website domain from a string in the form:
def domainGet(i):
   k = i.partition("@")
   l = k[2]
   return l

print(domainGet("katerina@word.com"))

#Create a basic function that returns True if the word 'dog' is contained in the input string.

def findDog(k):
    k = k.lower()
    l = k.find("dog")

    if l == -1:
        x = 'False'
    else:
        x = 'True'

    return x

print(findDog("where is my doG."))

#Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'.

seq= ['soup','dog','salad','cat','great']
x = lambda a: [x for x in seq if x.startswith('s')]
print(x(seq))

#You are driving a little too fast, and a police officer stops you. Write a function to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket".
#If your speed is 60 or less, the result is "No Ticket".
#If speed is 81 or more, the result is "Big Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all cases.
def caught_speeding(speed,is_birthday):

    if is_birthday:
        speeding = speed-5
    else:
        speeding = speed

    if speeding > 80:
        return 'Big Ticket'
    elif speeding > 60:
        return 'Small Ticket'
    else:
        return 'No Ticket'

print(caught_speeding(81,False))
