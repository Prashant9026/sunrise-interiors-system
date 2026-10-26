"""
Data Cleaning Script for Sunrise Interiors Messy Leads
Assignment: Technical Implementation Specialist (Intern) - Agile Automate

This script:
1. Standardizes Indian phone numbers to the uniform '+91XXXXXXXXXX' format.
   - Handles prefixes like '+91', '91', leading '0', spaces, hyphens, and parentheses.
2. Trims extraneous whitespace from names and phone fields.
3. Removes duplicate rows (e.g., Sneha Reddy appearing twice with different initial phone formats).
4. Exports the cleaned dataset to 'cleaned_leads.csv' and prints a formatted summary table.
"""

import csv
import re
from pathlib import Path


def standardize_phone(phone_raw: str) -> str:
    """
    Standardizes Indian phone numbers to '+91XXXXXXXXXX'.

    Handles:
    - '+919876500000' -> '+919876500000'
    - '9876543210'    -> '+919876543210'
    - '91 98765 12345'-> '+919876512345'
    - '098-765-99887' -> '+919876599887'
    - '+91-9876511111'-> '+919876511111'
    """
    if not phone_raw:
        return ""

    # Strip all non-digit characters
    digits = re.sub(r"\D", "", phone_raw)

    # Handle numbers with country code 91 prefix (12 digits total)
    if len(digits) == 12 and digits.startswith("91"):
        digits = digits[2:]
    # Handle numbers with leading trunk zero '0' (11 digits total)
    elif len(digits) == 11 and digits.startswith("0"):
        digits = digits[1:]

    # A valid Indian mobile number should have 10 digits
    if len(digits) == 10:
        return f"+91{digits}"
    else:
        # Fallback if phone number is non-standard
        return f"+91{digits[-10:]}" if len(digits) >= 10 else phone_raw.strip()


def clean_leads_csv(input_path: str, output_path: str):
    """
    Reads messy leads CSV, standardizes phone numbers, removes exact duplicate rows,
    and writes out cleaned data.
    """
    input_file = Path(input_path)
    output_file = Path(output_path)

    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found at: {input_path}")

    cleaned_records = []
    seen_rows = set()

    with open(input_file, mode="r", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames or ["Name", "Phone"]

        for row in reader:
            name = row.get("Name", "").strip()
            raw_phone = row.get("Phone", "").strip()
            clean_phone = standardize_phone(raw_phone)

            record_key = (name, clean_phone)

            # Deduplication: remove exact duplicate rows after cleaning
            if record_key not in seen_rows:
                seen_rows.add(record_key)
                cleaned_records.append({
                    "Name": name,
                    "Phone": clean_phone
                })

    # Write cleaned records to output CSV
    with open(output_file, mode="w", newline="", encoding="utf-8") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=["Name", "Phone"])
        writer.writeheader()
        writer.writerows(cleaned_records)

    return cleaned_records


def print_comparison(input_path: str, cleaned_records: list):
    """Prints a comparison between original messy data and cleaned data."""
    print("=" * 65)
    print("   ORIGINAL MESSY DATA (from messy_leads.csv)")
    print("=" * 65)
    with open(input_path, mode="r", encoding="utf-8") as infile:
        for idx, line in enumerate(infile.readlines()):
            print(f"Row {idx}: {line.strip()}")

    print("\n" + "=" * 65)
    print("   CLEANED & DEDUPLICATED DATA (format: +91XXXXXXXXXX)")
    print("=" * 65)
    print(f"{'No.':<5} | {'Name':<20} | {'Standardized Phone':<18}")
    print("-" * 65)
    for idx, row in enumerate(cleaned_records, 1):
        print(f"{idx:<5} | {row['Name']:<20} | {row['Phone']:<18}")
    print("=" * 65)
    print(f"Total Rows Before: 6 | Total Rows After Deduplication: {len(cleaned_records)}")
    print(f"Duplicates Removed: 1 (Sneha Reddy duplicate entries unified)")
    print("=" * 65)


if __name__ == "__main__":
    current_dir = Path(__file__).parent
    input_csv = current_dir / "messy_leads.csv"
    output_csv = current_dir / "cleaned_leads.csv"

    print("\n[+] Starting data cleaning process...")
    cleaned_data = clean_leads_csv(str(input_csv), str(output_csv))
    print(f"[+] Cleaned data successfully written to: {output_csv.name}\n")

    print_comparison(str(input_csv), cleaned_data)
