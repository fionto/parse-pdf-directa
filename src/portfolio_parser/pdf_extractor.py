"""
Parser for semi-structured PDF portfolio statements.

The module extracts financial instrument data from PDF documents using
pdfplumber. Because the original PDFs lack a consistent table layout,
content is analyzed sequentially on a line-by-line basis.

Field extraction is performed via regular-expression matching against
rows of the form:

    NAME (ISIN) QUANTITY PRICE TOTAL_VALUE [*]

Parsed records are represented as dataclass objects and aggregated into
a pandas DataFrame.

The parser assumes European-style numeric formatting and supports:
    - thousands separators ('.')
    - decimal separators (',')

Limitations:
    - No support for multi-line entries
    - No reconstruction of page-break-split rows
    - Non-matching rows are skipped and logged
"""

from dataclasses import dataclass
from pathlib import Path
import pandas as pd


@dataclass(frozen=True)
class PortfolioEntry:
    nome_asset: str
    isin: str
    quantita: float
    prezzo: float
    valore_eur: float
    isee_nominale: bool = False


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
    
    


def extract_portfolio_entries(pdf_path: Path) -> list[PortfolioEntry]:
    """
    Extract portfolio entries from a Directa monthly statement PDF.
    
    Parameters
    ----------
    pdf_path : Path
        Path to the PDF file. Must exist and be readable.
    
    Returns
    -------
    list[PortfolioEntry]
        List of PortfolioEntry object empty if file is empty or only has header
    
    Raises
    ------
    FileNotFoundError
        If pdf_path does not exist.
    ValueError
        If PDF cannot be parsed or regex yields inconsistent fields.
    """
    pass

def entries_to_dataframe(entries: list[PortfolioEntry]) -> pd.DataFrame:
    """
    Convert a list of PortfolioEntry objects to a pandas DataFrame.
    
    Parameters
    ----------
    entries : List[PortfolioEntry]
    
    Returns
    -------
    pd.DataFrame
        DataFrame with columns matching PortfolioEntry fields.
    """
    pass