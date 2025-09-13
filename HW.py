class Dog:
    species = "Bulldog"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def display(self):
        print("Name:", self.name)
        print("Breed:", self.breed)
        print("Species:", Dog.species)

dog1 = Dog("Bingo", "Golden retriever")
dog2 = Dog("Bob", "Bulldog")

print("Dog1 details:")
dog1.display()
print("\nDetails of Dog2:")
dog2.display()