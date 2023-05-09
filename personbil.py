import fordon

class personbil:

    def __init__(self, fabrikat, color, bagagevolym):
        self.bagagevolym = bagagevolym
        self.fabrikat = fabrikat
        self.color = color



    #metoder
    def set_bagagevolym(self, bagagevolym):
        self.bagagevolym = bagagevolym

    def get_bagagevolym(self):
        return self.bagagevolym

    def print_fordon(self):
        print(self.fabrikat +" Färg: "+ self.color +" bagagevolym= "+ str(self.bagagevolym))

