import json
import urllib.request
import pickle, pandas, os, sys
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class Command(BaseCommand):

    help = 'Imports data from Google Sheets'

    def handle(self, *args, **options):
        try:
            print('Processing...')
            # If modifying these scopes, delete the file token.pickle.
            SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

            # The ID and range of a sample spreadsheet.
            SAMPLE_SPREADSHEET_ID = '1ljt1URrDZRqTK0qke2yV3lD24CqrfnemhLKClMBYYrQ'
            SAMPLE_RANGE_NAME = 'INTL!A:D'

            """Shows basic usage of the Sheets API.
            Prints values from a sample spreadsheet.
            """
            creds = None
            # The file token.pickle stores the user's access and refresh tokens, and is
            # created automatically when the authorization flow completes for the first
            # time.
            if os.path.exists('token.pickle'):
                with open('token.pickle', 'rb') as token:
                    creds = pickle.load(token)
            # If there are no (valid) credentials available, let the user log in.
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'credentials.json', SCOPES)
                    creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open('token.pickle', 'wb') as token:
                    pickle.dump(creds, token)

            service = build('sheets', 'v4', credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
            values = result.get('values', [])

            df = pandas.DataFrame(values)
            df.to_csv('INTL.csv', index=False)
            print(f'Done... {df.shape[0]} rows imported')

        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f'{exc_type.__name__} : {str(exc_obj)} in <{str(fname)}> at line {str(exc_tb.tb_lineno)}')
