class Pet:
    PET_TYPES=['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []
    def __init__(self, name, pet_type, owner=None):
        self.name=name
        self.pet_type=pet_type
        if pet_type.lower() not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type. Allowed types are:{', '.join(Pet.PET_TYPES)}")
        self.owner=owner 
        if owner is not None:
            owner.add_pet(self)

        Pet.all.append(self)
        

class Owner:
    def __init__(self, name):
        self.name=name
        self.pets_list=[]
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Invalid pet type. The pet should be an instance of the Pet class.")
        pet.owner = self
        self.pets_list.append(pet)
    def pets(self):
        return self.pets_list
    def get_sorted_pets(self):
        return sorted(self.pets_list, key=lambda pet: pet.name)
