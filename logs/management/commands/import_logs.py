from datetime import datetime
import codecs
import pytz
import re

from django.core.management.base import BaseCommand
from django.utils import timezone

from logs.models import Log


class Command(BaseCommand):
    help = 'imports IRC logs from the specified file'

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str)

    def handle(self, *args, **options):
        file_name = options['file_name']
        file = open(file_name, 'r')

        timezone.activate(pytz.timezone('America/New_York'))

        match = re.search('(\d{4})', file_name)
        year = int(match.group(1))

        match = re.search('(\d{2})-(\d{2})', file_name)
        month = int(match.group(1))
        day = int(match.group(2))

        start_time = timezone.make_aware(datetime(year, month, day, 0, 0, 0))
        end_time = timezone.make_aware(datetime(year, month, day, 23, 59, 59))

        existing_logs = Log.objects.filter(
            time__gte=start_time,
            time__lte=end_time,
        )

        log_dict = {}
        for log in existing_logs:
            if log.time in log_dict:
                log_dict[log.time].append(log)
            else:
                log_dict[log.time] = [log]

        for line in file:
            match = re.match('(\d{2}):(\d{2}) < (.+?)> (.+)', line)
            if match:
                hour = int(match.group(1))
                minute = int(match.group(2))
                username = match.group(3)
                text = match.group(4)
                log_time = timezone.make_aware(datetime(year, month, day, hour, minute, 0))

                found = False
                if log_time in log_dict:
                    for log in log_dict[log_time]:
                        if log.user == username and log.text == text:
                            found = True

                if found is False:
                    log = Log()
                    log.time = log_time
                    log.user = username
                    log.text = text
                    log.save()

        file.close()
