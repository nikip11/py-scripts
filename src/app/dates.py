import dateparser

def transform_date(date, dateFormat: str = "%Y-%m-%d"):
    try:
        parsed_date = dateparser.parse(date)
        return parsed_date.strftime(dateFormat)
    except (ValueError, AttributeError):
        return None
