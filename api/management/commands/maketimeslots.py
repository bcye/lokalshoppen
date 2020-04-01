from django.core.management.base import BaseCommand
from api.models import TimeSlot, Company, BusinessHours
from django.utils.timezone import datetime, timedelta
import pytz
from lokalshoppen.settings import TIME_ZONE


TZ = pytz.timezone(TIME_ZONE)


def create_timeslot_day(company, date):
    # get the business hours for that weekday
    weekday = date.isoweekday()
    biz_hours_set = BusinessHours.objects.filter(company=company, weekday=weekday)

    print("Generating for: " + str(date))

    # a day can have multiple business hours
    # i.e. 10-15 and 16-18
    for biz_hours in biz_hours_set:
        # get an initial time
        time = datetime.combine(date, biz_hours.start, tzinfo=TZ)
        end = datetime.combine(date, biz_hours.end, tzinfo=TZ)

        while time < end:
            end_time = time + timedelta(minutes=30)

            if len(TimeSlot.objects.filter(company=company, start=time, end=end_time)) > 1:
                # bail out, timeslot exists already
                print("\tTimeslot exists, bailing out...")
                time += timedelta(minutes=30)
                continue

            # create time slot
            ts = TimeSlot()
            ts.company = company
            ts.start = time
            ts.end = end_time
            ts.save()
            print("\tSaving " + str(ts) + "...")

            # increment
            time += timedelta(minutes=30)


def create_timeslot_set(company):
    # get the dates
    date = datetime.today()
    in_one_week = (date + timedelta(days=7))

    print("Generating Set...")

    while date < in_one_week:

        # create timeslots
        create_timeslot_day(company, date)

        # increment day
        date += timedelta(days=1)

    print("Ended generating set...")


class Command(BaseCommand):
    help = 'Creates TimeSlots for the next week. Should be run periodically.'

    def handle(self, *args, **options):
        companies = Company.objects.filter(active=True)

        for company in companies:
            if len(TimeSlot.objects.filter(company=company)) == 0:
                # if it is a fresh company, we want to generate timeslots for the next 6 days
                create_timeslot_set(company)

            # no matter what, we want to generate time slots for in 7 days:
            # 1. if it's a fresh company, we will have 7 days in advance of time slots
            # 2. if it's an existing one, we currently have 6th and are generating the 7th
            create_timeslot_day(company, (datetime.today() + timedelta(days=7)))
