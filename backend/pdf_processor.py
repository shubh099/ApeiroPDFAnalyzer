from typing import List, Dict, Optional, Any
import logging
import re

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)


def extract_section_info_from_text(text: str) -> Dict[str, Optional[str]]:
    """
    Extract Fund and Category from text.
    Returns: {"fund": str, "category": str}
    """
    if not text:
        return {"fund": None, "category": None}

    fund = None
    category = None

    # Known fund patterns
    fund_patterns = [
        "PRIMARY HEALTHCARE FUND",
        "SOCIAL HEALTH INSURANCE FUND"
    ]

    # Known category patterns
    category_patterns = [
        "OUTPATIENT CARE SERVICES",
        "MATERNITY, NEWBORN AND CHILD HEALTH SERVICES",
        "MATERNITY SERVICES",
        "SCREENING & MANAGEMENT OF PRE-CANCEROUS LESIONS",
        "SCREENING AND MANAGEMENT OF PRE-CANCEROUS LESIONS",
        "OPTICAL HEALTH SERVICES",
        "END OF LIFE SERVICES",
        "MEDICAL INPATIENT SERVICES",
        "RENAL CARE PACKAGE",
        "MENTAL WELLNESS BENEFIT PACKAGE",
        "SURGICAL SERVICES PACKAGE",
        "ONCOLOGY SERVICES",
        "MEDICAL IMAGING AND OTHER INVESTIGATIONS PACKAGE",
        "PHARMACY PACKAGE",
        "SPECIALIZED LABORATORY SERVICE",
        "AMBULANCE EVACUATION SERVICES",
        "ACCIDENT & EMERGENCY SERVICES",
        "ACCIDENT AND EMERGENCY SERVICES",
        "CRITICAL ILLNESS PACKAGE",
        "PALLIATIVE CARE SERVICES",
        "CHRONIC ILLNESSES",
        "ASSISTIVE DEVICES"
    ]

    # Search for fund names (case-insensitive)
    for pattern in fund_patterns:
        if pattern.upper() in text.upper():
            fund = pattern
            break

    # Search for category names (case-insensitive)
    for pattern in category_patterns:
        if pattern.upper() in text.upper():
            category = pattern
            break

    return {"fund": fund, "category": category}





def get_extraction_summary(tables: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Generate a summary of the extraction results.

    Returns:
    {
        "total_tables": int,
        "total_rows": int,
        "unique_funds": int,
        "unique_categories": int,
        "funds": [str],
        "categories": [str]
    }
    """
    total_tables = len(tables)
    total_rows = sum(len(table.get("rows", [])) for table in tables)
    funds = set(table["fund"] for table in tables if table.get("fund"))
    categories = set(table["category"] for table in tables if table.get("category"))

    return {
        "total_tables": total_tables,
        "total_rows": total_rows,
        "unique_funds": len(funds),
        "unique_categories": len(categories),
        "funds": list(funds),
        "categories": list(categories)
    }
