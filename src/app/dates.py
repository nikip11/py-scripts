import dateparser

def transform_date(date, dateFormat: str = "%Y-%m-%d"):
    try:
        settings = {'STRICT_PARSING': True} # Fechas completas
        parsed_date = dateparser.parse(fecha, settings=settings, languages=['es'])
        # parsed_date = dateparser.parse(date)
        return parsed_date.strftime(dateFormat)
    except (ValueError, AttributeError):
        return None
