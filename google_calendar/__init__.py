from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle
import os, os.path
import datetime

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def authenticate_google():
    creds = None
    if os.path.exists('google_calendar\token.pickle'):
        with open('google_calendar\token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'google_calendar\credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    return service


def get_events(n, service):
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print(f'Getting the upcoming {n} events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=n, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
        return start, event['summary']

service = authenticate_google()
if __name__ == "__main__":
    get_events(2, service)