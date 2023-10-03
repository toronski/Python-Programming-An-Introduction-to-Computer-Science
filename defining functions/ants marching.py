# the ants go marching.py

def hurra():
    return ', hurrah! hurrah!'

def march():
    return 'The ants go marching '

def lyrics(number, little_does):
    number = number + ' by ' + number
    print(march() + number + hurra())
    print(march() + number + hurra())
    print(march() + number)
    print("The little one stops to " + little_does + ',')
    print("And they all go marching down...\nIn the ground... \
          \nTo get out...\nOf the rain.\nBoom! Boom! Boom!\n")

def ants():
    lyrics('one', 'suck his thumb')
    lyrics('two', 'tie his shoe')
    lyrics('three', 'to check his knee')
    lyrics('four', 'to write on the floor')
    lyrics('five', 'to feel the wind')

ants()
