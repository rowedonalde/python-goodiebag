import datetime

def iso_to_date(date):
    '''
    Takes a date in ISO 8601 YYYY-MM-DD format and returns the
    equivalent Python datetime.date object.
    
    Requires:
    datetime
    '''
    date_chunks = date.split('-')
    return datetime.date(date_chunks[0], date_chunks[1], date_chunks[2])