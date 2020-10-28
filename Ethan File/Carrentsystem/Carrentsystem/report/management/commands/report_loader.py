from csv import DictReader
from django.core.management import BaseCommand
from report.models import Report
from pytz import UTC

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        read_report = DictReader(open('./total_rent.csv'))
        print("loading record data")
        for row in read_report:
            report = Report()
            report.car_id = row['Car_ID']
            report.brand_name = row['BrandName']
            report.type = row['Type']
            report.tranmission = row['Transmission']
            report.luggage_size = row['LuggageSize']
            report.seat_number = row['SeatNumber']
            report.release_year = row['ReleaseYear']
            report.total_rent_january = row['Total_Rent_January']
            report.total_rent_february = row['Total_Rent_February']
            report.total_rent_march = row['Total_Rent_March']
            report.total_rent_april = row['Total_Rent_April']
            report.total_rent_may = row['Total_Rent_May']
            report.total_rent_june = row['Total_Rent_June']
            report.total_rent_july = row['Total_Rent_July']
            report.total_rent_august = row['Total_Rent_August']
            report.total_rent_september = row['Total_Rent_September']
            report.total_rent_october = row['Total_Rent_October']
            report.total_rent_november = row['Total_Rent_November']
            report.total_rent_december = row['Total_Rent_December']

            report.save()
        print("report data imported")
