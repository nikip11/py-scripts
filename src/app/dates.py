import dateparser

def transform_date(date, dateFormat: str = "%Y-%m-%d"):
    try:
        settings = {'STRICT_PARSING': True}
        parsed_date = dateparser.parse(date, settings=settings, languages=['es'])
        return parsed_date.strftime(dateFormat)
    except (ValueError, AttributeError):
        return None
