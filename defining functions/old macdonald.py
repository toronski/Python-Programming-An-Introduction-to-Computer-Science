# old macdonald.py

def animalVerse(animal, sound):
    sound2 = sound + ', ' + sound
    print("And on that farm he had a " + animal + ", Ee-igh, Ee-igh, Oh!")
    print("With a " + sound2 + " here and a " + sound2 + "there.")
    print("Here a " + sound + ', there a ' + sound + " everywhere a " + sound2
          + '.')

def oldie():
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")

def whole(a, b):
    oldie()
    animalVerse(a, b)
    print("\n")

def main():
    animals = ['cow', 'elephant', 'chicken', 'dog', 'cat']
    sounds = ['moo', 'whooo', 'co-coo', 'wuph', 'miau']

    for (a, b) in zip(animals, sounds):
        whole(a, b)
    
     
main()
