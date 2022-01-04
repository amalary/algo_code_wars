# You forgot to count the number of toast you put into there, you don't know if you put exactly six pieces of toast into the toasters.

# Define a function that counts how many more (or less) pieces of toast you need in the toasters. Even though you need more or less, the number will still be positive, not negative.

def six_pieces(pieces):

    if pieces > 6:
        return abs(pieces - 6)

    else: 
        if pieces < 6:
            return abs(6 - pieces)


print(six_pieces(4))

    

