import json
import urllib.request
import pandas, os, sys
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    help = 'Imports data from IDIMS API'

    def handle(self, *args, **options):
        try:
            print('Processing...')
            url = settings.IDIMS_API
            with urllib.request.urlopen(url) as url:
                data = json.loads(url.read().decode())
                # print(data['data'])
                df = pandas.DataFrame.from_dict(data['data']['data'])
                df.to_csv('IDIMS.csv')
                print(f'Done... {df.shape[0]} rows imported')
        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f'{exc_type.__name__} : {str(exc_obj)} in <{str(fname)}> at line {str(exc_tb.tb_lineno)}')
        

