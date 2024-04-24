class Bread:
    nutrition_for_slice = {'calories': 10, 'carbohydrates': 20, 'sodium': 5, 'sugar': 5, 'fat': 5}

    def get_nutrition(self, number_of_slices):
        return {nutrition: value*number_of_slices for nutrition, value in self.nutrition_for_slice.items()}


class WholeWheatBread(Bread):
    nutrition_for_slice = {'calories': 1, 'carbohydrates': 1, 'sodium': 1, 'sugar': 1, 'fat': 1}


class RyeBread(Bread):
    nutrition_for_slice = {'calories': 100, 'carbohydrates': 1, 'sodium': 100, 'sugar': 0, 'fat': 0}


b1 = Bread()
print(b1.get_nutrition(5))

b2 = WholeWheatBread()
print(b2.get_nutrition(5))

b3 = RyeBread()
print(b3.get_nutrition(1))
