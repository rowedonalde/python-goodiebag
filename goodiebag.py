import datetime

def iso_to_date(date):
    """
    Take a date in ISO 8601 YYYY-MM-DD format and return the
    equivalent Python datetime.date object.
    
    Requires:
    datetime
    
    """
    date_chunks = date.split('-')
    return datetime.date(int(date_chunks[0]), int(date_chunks[1]),
                         int(date_chunks[2]))