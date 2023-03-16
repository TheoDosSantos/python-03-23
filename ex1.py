import random

class Collection(object):
    def __init__(self):
        self.type = 'Quote by famous people'
        self.quotes = ["The greatest glory in living lies not in never falling, but in rising every time we fall. -Nelson Mandela"]
        # Can be empty, but in this case you must, at least, add one quote with setter before using getter or it would return nothing

    def get_quotes(self):
        return self.quotes
        # Return quotes

    def set_quotes(self, u):
        self.quotes.append(u)
        # Allow to add citation in the array

my_collection = Collection()

my_collection.set_quotes("The way to get started is to quit talking and begin doing. -Walt Disney")
my_collection.set_quotes("Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking. -Steve Jobs")
my_collection.set_quotes("If life were predictable it would cease to be life, and be without flavor. -Eleanor Roosevelt")
my_collection.set_quotes("If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough. -Oprah Winfrey")
my_collection.set_quotes("If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success. -James Cameron")
my_collection.set_quotes("Life is what happens when you're busy making other plans. -John Lennon")
my_collection.set_quotes("Tell me and I forget. Teach me and I remember. Involve me and I learn. -Benjamin Franklin")
my_collection.set_quotes("Don't judge each day by the harvest you reap but by the seeds that you plant. -Robert Louis Stevenson")
my_collection.set_quotes("In the end, it's not the years in your life that count. It's the life in your years. -Abraham Lincoln")
# Adding some new quotes

index_r = random.randint(0, len(my_collection.get_quotes()) - 1)
# Randomize a number between 0 and quotes array's length to get a different index on each execution of the script

print(my_collection.type + " :")
print(my_collection.get_quotes()[index_r])
# Displaying a random quote contains in the quotes array
