"""
Generates the official Word document (.docx) for Google Docs submission:
'YourName_AgileAutomate_tech.docx'

This document contains all 3 tasks formatted with clean typography, styled tables,
code snippets, and executive summaries.
Uploading this file to Google Drive and opening it creates an instant, perfectly-formatted Google Doc!
"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from pathlib import Path


def set_cell_background(cell, fill_hex):
    """Sets background color of a table cell."""
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tc_pr.append(shd)


def set_cell_margins(cell, top=120, bottom=120, left=160, right=160):
    """Sets internal padding for a table cell (in twips: 20 twips = 1 pt)."""
    tc_pr = cell._tc.get_or_add_tcPr()
    tc_mar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tc_pr.append(tc_mar)


def create_submission_doc(output_path: str):
    doc = docx.Document()

    # Set page margins (0.75 inch for a clean modern layout)
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)

    # Base Colors
    PRIMARY_COLOR = RGBColor(30, 64, 175)     # Deep Corporate Blue
    SECONDARY_COLOR = RGBColor(15, 118, 110) # Teal
    TEXT_DARK = RGBColor(31, 41, 55)         # Charcoal Black
    MUTED_GRAY = RGBColor(107, 114, 128)     # Slate Gray

    # Document Header / Banner Title
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(0)
    title_p.paragraph_format.space_after = Pt(4)
    run_sub = title_p.add_run("AGILE AUTOMATE • TECHNICAL IMPLEMENTATION SPECIALIST (INTERN)\n")
    run_sub.font.name = "Arial"
    run_sub.font.size = Pt(10)
    run_sub.font.bold = True
    run_sub.font.color.rgb = SECONDARY_COLOR

    run_title = title_p.add_run("Technical Implementation Assignment: Sunrise Interiors")
    run_title.font.name = "Arial"
    run_title.font.size = Pt(22)
    run_title.font.bold = True
    run_title.font.color.rgb = PRIMARY_COLOR

    # Metadata Box Table
    meta_table = doc.add_table(rows=2, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_table.autofit = False

    meta_data = [
        ("Candidate Name:", "[Your Name] (e.g. Yash Mishra)", "Target Scenario:", "Sunrise Interiors (6-person Design Studio)"),
        ("Submission Recipient:", "amit12@agileautomate.co (CC: aryansh@agileautomate.co)", "File Naming:", "YourName_AgileAutomate_tech")
    ]

    for row_idx, row in enumerate(meta_table.rows):
        d = meta_data[row_idx]
        # Col 0
        p0 = row.cells[0].paragraphs[0]
        p0.paragraph_format.space_after = Pt(2)
        r0_lbl = p0.add_run(d[0] + " ")
        r0_lbl.bold = True
        r0_lbl.font.size = Pt(9.5)
        p0.add_run(d[1]).font.size = Pt(9.5)

        # Col 1
        p1 = row.cells[1].paragraphs[0]
        p1.paragraph_format.space_after = Pt(2)
        r1_lbl = p1.add_run(d[2] + " ")
        r1_lbl.bold = True
        r1_lbl.font.size = Pt(9.5)
        p1.add_run(d[3]).font.size = Pt(9.5)

        for cell in row.cells:
            set_cell_background(cell, "F3F4F6")
            set_cell_margins(cell, top=100, bottom=100, left=140, right=140)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # -------------------------------------------------------------
    # TASK 1: CLICKUP WORKSPACE IMPLEMENTATION
    # -------------------------------------------------------------
    h1 = doc.add_heading("TASK 1: ClickUp Workspace Implementation", level=1)
    h1.paragraph_format.space_before = Pt(14)
    h1.paragraph_format.space_after = Pt(6)

    p_intro = doc.add_paragraph()
    p_intro.add_run(
        "Sunrise Interiors is currently suffering from 3 critical operational breakdowns: missed project deadlines, "
        "vendors getting paid twice, and complete lack of executive visibility for the owner. "
        "Below is the complete architectural build designed in ClickUp to solve these pain points permanently."
    )

    # ClickUp Guest Link Box
    link_p = doc.add_paragraph()
    link_p.paragraph_format.space_before = Pt(4)
    link_p.paragraph_format.space_after = Pt(8)
    r_link_lbl = link_p.add_run("🔗 ClickUp Workspace Guest Share Link:\n")
    r_link_lbl.bold = True
    r_link_lbl.font.color.rgb = PRIMARY_COLOR
    r_link_val = link_p.add_run("[PASTE YOUR CLICKUP GUEST/PUBLIC LINK HERE - e.g. https://app.clickup.com/...]")
    r_link_val.bold = True
    r_link_val.underline = True

    # Section 1.1 Hierarchy
    h2 = doc.add_heading("1. Hierarchy & Structure", level=2)
    h2.paragraph_format.space_before = Pt(10)
    h2.paragraph_format.space_after = Pt(4)

    p_struct = doc.add_paragraph()
    p_struct.add_run(
        "• Workspace: Sunrise Interiors Studio\n"
        "  └── Space: Interior Projects & Operations\n"
        "      ├── Folder 1: Client Projects (Lists: Residential Projects, Commercial Projects)\n"
        "      ├── Folder 2: Vendor & Procurement Tracker (Lists: Material POs & Contractor Ledger)\n"
        "      └── Folder 3: Design Studio Tasks (List: Design Deliverables across 3 Designers)"
    )

    # Section 1.2 Statuses
    h2 = doc.add_heading("2. Stage-Gate Status Workflows", level=2)
    h2.paragraph_format.space_before = Pt(10)
    h2.paragraph_format.space_after = Pt(4)

    p_stat = doc.add_paragraph()
    p_stat.add_run("Client Projects Status Flow:\n").bold = True
    p_stat.add_run(
        "01. Lead / Initial Inquiry ➔ 02. Site Visit & Briefing ➔ 03. Concept & 3D Design ➔ "
        "04. Client Approval & Sign-off ➔ 05. Sourcing & Procurement ➔ 06. Site Execution / Fit-out ➔ "
        "07. Snagging & Quality Check ➔ 08. Handover & Completed (Closed)\n\n"
    )
    p_stat.add_run("Vendor Billing Status Flow (Prevents Double Payouts):\n").bold = True
    p_stat.add_run(
        "Quote Requested ➔ Quote Approved / PO Issued ➔ Advance Paid ➔ Work in Progress ➔ "
        "Final Quality Approved ➔ Payment Cleared / Closed"
    )

    # Section 1.3 Custom Fields Table
    h2 = doc.add_heading("3. Custom Fields Designed for Sunrise Interiors", level=2)
    h2.paragraph_format.space_before = Pt(10)
    h2.paragraph_format.space_after = Pt(4)

    cf_table = doc.add_table(rows=1, cols=3)
    cf_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cf_headers = ["Custom Field Name", "Field Type", "Business Function & Value"]
    for i, h in enumerate(cf_headers):
        cell = cf_table.rows[0].cells[i]
        set_cell_background(cell, "1E40AF")
        set_cell_margins(cell, top=140, bottom=140, left=160, right=160)
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(9.5)

    custom_fields_data = [
        ("Carpet Area (Sq Ft)", "Number", "Estimates site execution duration and material quantity."),
        ("Total Project Budget", "Currency (₹)", "Contract value of interior project agreed with client."),
        ("Lead Designer", "People", "Assigns responsibility to 1 of 3 interior designers."),
        ("Vendor Name & Trade", "Dropdown", "Modular Kitchen, Carpentry, Electrical, False Ceiling, Painting, Civil."),
        ("Total Invoiced Amount", "Currency (₹)", "Total bill submitted by contractor / vendor."),
        ("Amount Paid", "Currency (₹)", "Disbursed advance and running payments to date."),
        ("Balance Due", "Formula / Number", "Formula: Total Invoiced - Amount Paid (Completely stops double payments!)."),
        ("Payment Status", "Dropdown", "Unpaid | Partially Paid | Fully Paid (Locks task when fully settled)."),
        ("Milestone Due Date", "Date", "Strict handover and delivery dates to eliminate missed deadlines.")
    ]

    for row_data in custom_fields_data:
        row = cf_table.add_row()
        for idx, text in enumerate(row_data):
            cell = row.cells[idx]
            set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(2)
            r = p.add_run(text)
            r.font.size = Pt(9)
            if idx == 0:
                r.bold = True

    # Section 1.4 Automations
    h2 = doc.add_heading("4. Automations Implemented", level=2)
    h2.paragraph_format.space_before = Pt(10)
    h2.paragraph_format.space_after = Pt(4)

    doc.add_paragraph().add_run(
        "• Automation 1: Overpayment & Double-Payment Prevention (Critical)\n"
        "  - Trigger: When Custom Field 'Payment Status' changes to 'Fully Paid'\n"
        "  - Action: Update task status to 'Payment Cleared / Closed', set 'Balance Due' to ₹0, "
        "and post an internal audit comment: '[AUTOMATION] Vendor invoice marked FULLY PAID. Balance ₹0. Do not disburse additional advances.'\n\n"
        "• Automation 2: Automated Phase Handoff (Design to Procurement)\n"
        "  - Trigger: When Project Status changes to '05. Sourcing & Procurement'\n"
        "  - Action: Automatically create linked procurement tasks ('Generate BOQ & Issue Vendor POs'), "
        "set due date to Trigger + 5 days, and assign to Procurement Lead.\n\n"
        "• Automation 3: Project Delay Early Warning System\n"
        "  - Trigger: When Due Date arrives and Status is NOT '08. Handover & Completed'\n"
        "  - Action: Automatically escalate priority to 'Urgent (Red)' and alert Studio Owner."
    )

    # Section 1.5 Owner 10-Second Health Dashboard
    h2 = doc.add_heading("5. Owner's 10-Second Executive Health Dashboard", level=2)
    h2.paragraph_format.space_before = Pt(10)
    h2.paragraph_format.space_after = Pt(4)

    doc.add_paragraph().add_run(
        "Designed specifically so the studio owner can check overall business health in under 10 seconds without asking for updates on WhatsApp:\n\n"
        "1. Widget 1: Projects by Stage (Status Pie/Bar Chart) — Instant visual snapshot of all active client projects in Concept vs. Site Execution vs. Handover.\n"
        "2. Widget 2: Pending Vendor Payouts (Calculation Widget) — Sum of all 'Balance Due' values across active vendors. Zero surprises on cash flow.\n"
        "3. Widget 3: Overdue Tasks & Milestones (Task List Widget) — Filtered by 'Due Date is Overdue' and 'Status != Closed'. Highlights stalled projects immediately.\n"
        "4. Widget 4: Designer Workload & Capacity (Workload View) — Live task distribution across Designer 1, Designer 2, and Designer 3 to balance project allocations."
    )

    # -------------------------------------------------------------
    # TASK 2: DATA CLEANING (PYTHON)
    # -------------------------------------------------------------
    h1 = doc.add_heading("TASK 2: Data Cleaning (Python)", level=1)
    h1.paragraph_format.space_before = Pt(16)
    h1.paragraph_format.space_after = Pt(6)

    doc.add_paragraph().add_run(
        "Standardizes raw lead contact numbers into the uniform '+91XXXXXXXXXX' format, removes spaces, hyphens, "
        "and trunk zeros, and eliminates exact duplicate rows."
    )

    h2 = doc.add_heading("Cleaned Output Comparison Table", level=2)
    h2.paragraph_format.space_before = Pt(8)
    h2.paragraph_format.space_after = Pt(4)

    py_table = doc.add_table(rows=1, cols=4)
    py_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    py_headers = ["Name", "Original Messy Input", "Standardized Phone (+91XXXXXXXXXX)", "Cleaning Action"]
    for i, h in enumerate(py_headers):
        cell = py_table.rows[0].cells[i]
        set_cell_background(cell, "0F766E")
        set_cell_margins(cell, top=140, bottom=140, left=140, right=140)
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(9.5)

    py_results = [
        ("Ravi Kumar", "9876543210", "+919876543210", "Appended +91 country prefix"),
        ("Priya Shah", "91 98765 12345", "+919876512345", "Removed spaces; normalized '91' to '+91'"),
        ("Amit Verma", "098-765-99887", "+919876599887", "Stripped leading zero '0' and hyphens"),
        ("Sneha Reddy", "+919876500000 / 9876500000", "+919876500000", "Normalized and removed exact duplicate row"),
        ("Karan Mehta", "+91-9876511111", "+919876511111", "Stripped hyphens; preserved +91 format")
    ]

    for row_data in py_results:
        row = py_table.add_row()
        for idx, text in enumerate(row_data):
            cell = row.cells[idx]
            set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
            p = cell.paragraphs[0]
            p.paragraph_format.space_after = Pt(2)
            r = p.add_run(text)
            r.font.size = Pt(9)
            if idx == 0 or idx == 2:
                r.bold = True

    p_summary = doc.add_paragraph()
    p_summary.paragraph_format.space_before = Pt(4)
    p_summary.add_run("Result Summary: 6 initial rows processed ➔ 5 unique records output ➔ 1 duplicate eliminated.").italic = True

    h2 = doc.add_heading("Python Script: clean_leads.py", level=2)
    h2.paragraph_format.space_before = Pt(8)
    h2.paragraph_format.space_after = Pt(4)

    script_text = """import csv
import re
from pathlib import Path

def standardize_phone(phone_raw: str) -> str:
    \"\"\"Standardizes Indian phone numbers to '+91XXXXXXXXXX'.\"\"\"
    if not phone_raw:
        return ""
    digits = re.sub(r"\\D", "", phone_raw)
    if len(digits) == 12 and digits.startswith("91"):
        digits = digits[2:]
    elif len(digits) == 11 and digits.startswith("0"):
        digits = digits[1:]
    return f"+91{digits}" if len(digits) == 10 else f"+91{digits[-10:]}"

def clean_leads_csv(input_path: str, output_path: str):
    cleaned_records, seen_rows = [], set()
    with open(input_path, mode="r", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            name = row.get("Name", "").strip()
            phone = standardize_phone(row.get("Phone", "").strip())
            record_key = (name, phone)
            if record_key not in seen_rows:
                seen_rows.add(record_key)
                cleaned_records.append({"Name": name, "Phone": phone})

    with open(output_path, mode="w", newline="", encoding="utf-8") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=["Name", "Phone"])
        writer.writeheader()
        writer.writerows(cleaned_records)
    return cleaned_records

if __name__ == "__main__":
    clean_leads_csv("messy_leads.csv", "cleaned_leads.csv")"""

    code_p = doc.add_paragraph()
    code_p.paragraph_format.space_before = Pt(4)
    code_p.paragraph_format.space_after = Pt(8)
    code_run = code_p.add_run(script_text)
    code_run.font.name = "Courier New"
    code_run.font.size = Pt(8.5)

    # -------------------------------------------------------------
    # TASK 3: AUTOMATION LOGIC (N8N)
    # -------------------------------------------------------------
    h1 = doc.add_heading("TASK 3: Automation Logic (n8n Workflow)", level=1)
    h1.paragraph_format.space_before = Pt(16)
    h1.paragraph_format.space_after = Pt(6)

    doc.add_paragraph().add_run(
        "Event-driven architecture connecting Google Forms, ClickUp, Client Auto-Confirmation, and High-Priority Design Alerts."
    )

    h2 = doc.add_heading("1. Workflow Architecture & Flow Diagram", level=2)
    h2.paragraph_format.space_before = Pt(8)
    h2.paragraph_format.space_after = Pt(4)

    flow_text = """[ Google Form Submission ] (Trigger)
            │
            ▼
[ Node 1: Code / Normalizer ] ───> Cleans phone to +91XXXXXXXXXX & parses budget to integer
            │
            ▼
[ Node 2: ClickUp Create Task ] ──> Creates Lead card in 'Client Inquiries' list with custom fields
            │
            ▼
[ Node 3: Send Client Confirmation ] ──> Sends automated WhatsApp / Email acknowledgment to client
            │
            ▼
[ Node 4: IF Condition ] ───> Is budgetNumber >= 500000?
            │
     ┌──────┴────────────────────────┐
     ▼                               ▼
[ TRUE Branch: High-Value Lead ]   [ FALSE Branch: Standard Lead ]
[ Node 5: Alert Design Team ]     [ Node 6: Standard Queue ]
(Slack / WhatsApp alert to team)  (Saved in ClickUp without team ping)"""

    flow_p = doc.add_paragraph()
    flow_run = flow_p.add_run(flow_text)
    flow_run.font.name = "Courier New"
    flow_run.font.size = Pt(8.5)

    h2 = doc.add_heading("2. Sequence of Actions & Node Roles", level=2)
    h2.paragraph_format.space_before = Pt(8)
    h2.paragraph_format.space_after = Pt(4)

    doc.add_paragraph().add_run(
        "1. Trigger (Google Forms Trigger): Activates instantaneously when a prospective client submits an inquiry.\n"
        "2. Data Normalizer (Code Node): Strips formatting from phone numbers and parses budget strings ('7,50,000' or '8 Lakhs') into integers.\n"
        "3. ClickUp Integration (ClickUp Node): Creates a task in 'Client Projects' space with status '01. Lead / Initial Inquiry', mapping Budget, Phone, and Property Type.\n"
        "4. Client Confirmation (Gmail / WhatsApp Node): Sends immediate confirmation acknowledging receipt and promising a follow-up consultation within 24 hours.\n"
        "5. Conditional Filter (IF Node): Evaluates condition: {{$json.budgetNumber}} >= 500000.\n"
        "6. High-Value Alert (Slack / WhatsApp Node): If TRUE, dispatches an urgent alert to the design team channel with lead details and ClickUp task link."
    )

    h2 = doc.add_heading("3. Where the ₹5 Lakh Conditional Logic Fits", level=2)
    h2.paragraph_format.space_before = Pt(8)
    h2.paragraph_format.space_after = Pt(4)

    doc.add_paragraph().add_run(
        "The conditional check is intentionally placed after the ClickUp task is created and after the client receives confirmation, "
        "but before internal team notifications. This ensures:\n"
        "• 100% of leads are captured in the CRM and acknowledged, avoiding lost revenue.\n"
        "• The 3-person design team avoids alert fatigue, receiving high-priority interruptions only for high-ticket projects (₹5L+)."
    )

    h2 = doc.add_heading("4. What Could Go Wrong & Production-Grade Error Handling", level=2)
    h2.paragraph_format.space_before = Pt(8)
    h2.paragraph_format.space_after = Pt(4)

    doc.add_paragraph().add_run(
        "Potential Failure Modes:\n"
        "1. Malformed Budget String: If the client types free text like 'To be discussed' or 'Around 6L', standard numeric parsing could throw NaN.\n"
        "2. Transient API Downtime: ClickUp or WhatsApp API could return HTTP 429 (Rate Limit) or 500 error, resulting in a dropped lead.\n\n"
        "Handling Strategy:\n"
        "• Defensive Parsing: If the budget cannot be parsed, assign flag 'requires_manual_budget = true' and route it to the high-value branch so no potential client is neglected.\n"
        "• n8n Error Trigger Workflow: An attached 'Error Trigger' node logs any failed execution to a backup Google Sheet and pings the Operations Lead on Telegram/Slack with automated 3x Exponential Backoff Retry enabled on external API calls."
    )

    # -------------------------------------------------------------
    # SUBMISSION EMAIL TEMPLATE
    # -------------------------------------------------------------
    h1 = doc.add_heading("Submission Email Template", level=1)
    h1.paragraph_format.space_before = Pt(16)
    h1.paragraph_format.space_after = Pt(6)

    email_text = """To: amit12@agileautomate.co
CC: aryansh@agileautomate.co
Subject: Technical Implementation Specialist Assignment - [Your Name]

Dear Amit and Aryansh,

Please find my submission for the Technical Implementation Specialist (Intern) assignment for Agile Automate:

📄 Complete Assignment Document (Google Doc):
[PASTE YOUR GOOGLE DOC SHARE LINK HERE - with view/edit access]

📌 Quick Overview:
1. Task 1 (ClickUp System): Complete workspace for Sunrise Interiors with custom fields, double-payment prevention automation, and an Owner 10-Second Executive Health Dashboard.
   • ClickUp Guest Link: [PASTE YOUR CLICKUP GUEST LINK HERE]
2. Task 2 (Python Data Cleaning): clean_leads.py script standardizing raw contacts to +91XXXXXXXXXX and deduplicating records.
3. Task 3 (n8n Automation Architecture): End-to-end event-driven architecture, conditional logic placement, and failure-handling strategy.

Looking forward to your feedback and the next discussion!

Best regards,
[Your Name]
[Phone Number] | [LinkedIn Profile]"""

    email_p = doc.add_paragraph()
    email_run = email_p.add_run(email_text)
    email_run.font.name = "Courier New"
    email_run.font.size = Pt(8.5)

    doc.save(output_path)
    print(f"[+] Document created successfully at: {output_path}")


if __name__ == "__main__":
    out = Path(__file__).parent / "YourName_AgileAutomate_tech.docx"
    create_submission_doc(str(out))
