from transport.models import Location, Product
import csv
from tqdm import tqdm

def run():
    with open('./dataset/uszips.csv') as file:
        reader = csv.reader(file)
        next(reader)

        Product.objects.all().delete()
        Location.objects.all().delete()
        for row in tqdm(reader, total=33788, colour='#228a3e', unit=' row', desc='Progress: '):
            location = Location.objects.create(
                zipcode=row[0],
                latitude=row[1],
                longitude=row[2],
                city=row[3],
                state=row[5],
                )
            location.save()