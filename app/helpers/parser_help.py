

def int_get(value, default=1):
    """Converts a value to an integer, returning a default if conversion fails."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default