from csv import DictReader
from django.core.management import BaseCommand
from rental_car.models import Car, Record, Discount, Rental, PickUpStore, DropOffStore, Store, Client
from pytz import UTC

class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from pet_data.csv into our Pet model"

    def handle(self, *args, **options):

        read_car = DictReader(open('./car_data.csv'))
        print("loading car data")
        for row in read_car:
            car = Car()
            car.car_id = row['Car_ID']
            car.brand_name = row['BrandName']
            car.type = row['Type']
            car.transmission = row['Transmission']
            car.price = row['Price']
            car.luggage_size = row['LuggageSize']
            car.seat_number = row['SeatNumber']
            car.release_year = row['ReleaseYear']
            
            car.save()
        print("car data imported")
        
        read_record = DictReader(open('./record_data.csv'))
        print("loading record data")
        for row in read_record:
            record = Record()
            record.record_id = row['Record_ID']
            record.accident_type = row['AccidentType']
            record.accident_address = row['AccidentAddress']

            record.save()
        print("record data imported")
        
        read_discount = DictReader(open('./discount_data.csv'))
        print("loading discount data")
        for row in read_discount:
            discount = Discount()
            discount.discount_id = row['Discount_ID']
            discount.discount_code = row['DiscountCode']
            discount.starting_date = row['StartingDate']
            discount.ending_date = row['EndingDate']

            discount.save()
        print("discount data imported")

        read_rental = DictReader(open('./rental_data.csv'))
        print("loading rental data")
        for row in read_rental:
            rental = Rental()
            rental.rental_id = row['Rental_ID']
            rental.rent_date = row['RentDate']
            rental.end_rent_date = row['EndRentDate']
            rental.rent_price_total = row['RentPriceTotal']
            rental.pick_up_city = row['PickUpCity']
            rental.drop_off_city = row['DropOffCity']
            rental.insurance_number = row['InsuranceNumber']
            
            rental.save()
        print("rental data imported")

        read_pick_up_store = DictReader(open('./pick_up_store_data.csv'))
        print("loading pick up store data")
        for row in read_pick_up_store:
            pick_up_store = PickUpStore()
            pick_up_store.pick_up_store_id = row['Pick_Up_Store_ID']

            pick_up_store.save()
        print("pick up store data imported")

        read_drop_off_store = DictReader(open('./drop_off_store_data.csv'))
        print("loading drop off store data")
        for row in read_drop_off_store:
            drop_off_store = DropOffStore()
            drop_off_store.drop_off_store_id = row['Drop_Off_Store_ID']

            drop_off_store.save()
        print("drop off store data imported")

        read_store = DictReader(open('./store_data.csv'))
        print("loading store data")
        for row in read_store:
            store = Store()
            store.store_id = row['Store_ID']
            store.store_name = row['Store_Name']
            store.store_address = row['Store_Address']
            store.store_phone = row['Store_Phone']
            store.store_city = row['Store_City']
            store.store_state_name = row['Store_State_Name']

            store.save()
        print("store data imported")

        read_client = DictReader(open('./client_data.csv'))
        print("loading client data")
        for row in read_client:
            client = Client()
            client.client_id = row['Client_ID']
            client.client_name = row['Client_Name']
            client.client_phone = row['Client_Phone']
            client.client_address = row['Client_Address']
            client.client_brithday = row['Client_Brithday']
            client.client_occupation = row['Client_Occupation']
            client.client_gender = row['Client_Gender']

            client.save()
        print("client data imported")
        
