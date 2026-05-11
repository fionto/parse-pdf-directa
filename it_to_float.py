def it_to_float(s: str) -> float:
    """
    Parameters
    ----------
    s : str
        A string representing a number in Italian format.
        Thousands separator: '.' | Decimal separator: ','
    
    Returns
    -------
    float
        The converted numeric value.
    
    Raises
    ------
    ValueError
        If s is empty, contains invalid characters, or cannot be parsed.
    """
    
    if not s or not s.strip():
        raise ValueError(f"Cannot convert empty string to float")
  
    cleaned = s.strip()
    
    # Reject mixed or ambiguous formats
    if ',' in cleaned and '.' in cleaned:
        # Valid Italian: dots for thousands, comma for decimal (e.g., "1.234,56")
        # Invalid: comma before dot (e.g., "1,234.56" = US format)
        if cleaned.rfind(',') > cleaned.rfind('.'): # Does the last comma appear after the last dot?
            # Italian format: remove thousands separators, replace decimal comma
            normalized = cleaned.replace('.', '').replace(',', '.')
        else:
            raise ValueError(
                f"Ambiguous numeric format: '{s}'. "
                f"Expected Italian format (e.g., '1.234,56')"
            )
    elif ',' in cleaned:
        # Only comma: treat as decimal separator
        normalized = cleaned.replace(',', '.')
    elif '.' in cleaned:
        # Only dot: could be thousands separator (e.g., "1.234") or decimal (e.g., "1.23")
        # Heuristic: if more than 3 digits after last dot, assume thousands separator
        parts = cleaned.split('.')
        if len(parts[-1]) > 3:
            raise ValueError(
                f"Invalid thousands separator placement: '{s}'. "
                f"Expected format like '1.234' or '1.234,56'"
            )
        # Assume decimal point (US format) — accept but warn? Or reject?
        # For strictness: reject US format to avoid silent errors
        raise ValueError(
            f"US numeric format detected: '{s}'. "
            f"This parser expects Italian format (comma for decimal)"
        )
    else:
        # No separators: plain integer string
        normalized = cleaned
    
    try:
        return float(normalized)
    except ValueError as e:
        raise ValueError(f"Cannot parse '{s}' as float: {e}") from e
    
print(it_to_float("1.234"))