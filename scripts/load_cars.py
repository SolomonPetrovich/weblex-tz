from transport.models import Car, Location, Product
from tqdm import tqdm
import random
from string import ascii_uppercase

def run():
    letters = list(ascii_uppercase)
    
    Product.objects.all().delete()
    Car.objects.all().delete()

    for row in tqdm(range(20), total=20, colour='#228a3e', unit=' row', desc='Progress: '):
        random_number = str(random.randint(1000, 10000)) + random.choice(letters)
        random_location = random.choice(Location.objects.all())
        random_capacity = random.randint(1, 1000)

        car = Car.objects.create(
            number=random_number,
            current_location=random_location,
            capacity=random_capacity
        )
        car.save()