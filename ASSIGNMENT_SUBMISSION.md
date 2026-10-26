# Agile Automate — Technical Implementation Specialist (Intern) Assignment
**Candidate Document:** `[Your Name]_AgileAutomate_tech`  
**Submission Email:** `amit12@agileautomate.co` | **CC:** `aryansh@agileautomate.co`  
**Subject Line:** `Technical Implementation Specialist Assignment - [Your Name]`  
**Target Scenario:** Sunrise Interiors (6-person interior design studio in Bengaluru)

---

## TABLE OF CONTENTS
1. [Task 1: ClickUp Workspace Implementation](#task-1-clickup-workspace-implementation)
   - Architecture & Hierarchy (Spaces, Folders, Lists)
   - Custom Fields Designed for Interior Design
   - Double-Payment Prevention & Vendor Procurement System
   - Design Team Workload & Task Allocation
   - Workspace Automations
   - Owner 10-Second Executive Health Dashboard
   - Step-by-Step Setup Guide & Guest Link Sharing
2. [Task 2: Data Cleaning (Python Script & Output)](#task-2-data-cleaning-python-script--output)
   - Complete Python Script
   - Logic Explanation & Edge Cases Handled
   - Before vs. After Cleaned Dataset Table
3. [Task 3: n8n Automation Architecture & Logic](#task-3-n8n-automation-architecture--logic)
   - Architecture & Flow Diagram
   - Trigger, Sequence of Actions & Data Flow
   - Conditional Logic Placement (₹5 Lakh High-Value Check)
   - Failure Modes, Error Handling & Fallback Strategy
4. [Submission Checklist & Email Template](#submission-checklist--email-template)

---

# TASK 1: ClickUp Workspace Implementation

### 1. The Core Problems Sunrise Interiors is Facing & How This ClickUp Build Solves Them:
1. **Missed Project Deadlines:** Replaced unstructured WhatsApp chats with clear stage-gate project statuses and dependency dates.
2. **Vendors Paid Twice:** Solved by a dedicated **Procurement & Vendor Ledger** where every purchase order tracks `Invoice Amount`, `Advance Paid`, and auto-calculates `Balance Due` with a payment status (`Pending`, `Partially Paid`, `Fully Paid`).
3. **Owner Firefighting Daily:** Built an **Executive 10-Second Dashboard** giving immediate visual clarity on project health, overdue deliverables, designer capacity, and cash outflows.

---

### 2. Workspace Hierarchy

```text
Sunrise Interiors (Workspace)
│
└── 📁 Interior Projects & Operations (Space)
    │
    ├── 📂 1. Client Projects (Folder)
    │   ├── 📋 Residential Projects (List)
    │   └── 📋 Commercial Projects (List)
    │
    ├── 📂 2. Vendor & Procurement Tracker (Folder)
    │   ├── 📋 Material Procurement & POs (List)
    │   └── 📋 Contractor / Labor Billing (List)
    │
    └── 📂 3. Design Studio Tasks (Folder)
        └── 📋 Design Deliverables (List)
```

---

### 3. Status Workflows

#### A. Client Projects List Statuses:
- `01. Lead / Initial Inquiry` (Gray)
- `02. Site Visit & Briefing` (Blue)
- `03. Concept & 3D Design` (Purple)
- `04. Client Approval & Sign-off` (Teal)
- `05. Sourcing & Procurement` (Yellow)
- `06. Site Execution / Fit-out` (Orange)
- `07. Snagging & Quality Check` (Pink)
- `08. Handover & Completed` (Green - Closed)

#### B. Vendor & Procurement List Statuses (Double-Payment Prevention):
- `Quote Requested`
- `Quote Approved / PO Issued`
- `Advance Paid`
- `Work in Progress / Materials Dispatched`
- `Final Quality Approved`
- `Payment Cleared / Closed` (Closed)

---

### 4. Custom Fields Designed for Sunrise Interiors

| Field Name | Field Type | Purpose & Business Value |
| :--- | :--- | :--- |
| **Client Phone** | Phone / Text | Standardized client contact (`+91XXXXXXXXXX`) |
| **Carpet Area (Sq Ft)** | Number | Used to estimate timeline and material requirements |
| **Design Style** | Dropdown | Modern Minimalist, Contemporary, Bohemian, Scandinavian, Luxury |
| **Total Project Budget** | Currency (INR ₹) | Commercial valuation of the interior contract |
| **Lead Designer** | People | Responsible designer from the 3-person team |
| **Site Supervisor** | People | Responsible for on-ground vendor coordination |
| **Vendor Name** | Text / Dropdown | Specific supplier (e.g., Greenply, Hafele, Asian Paints, Local Carpenter) |
| **Vendor Trade** | Dropdown | Modular Kitchen, Carpentry, Electrical, False Ceiling, Painting, Civil |
| **Invoice / PO Number** | Text | Prevents duplicate billing and matches invoices |
| **Total Invoiced Amount**| Currency (INR ₹) | Total payable to the vendor |
| **Amount Paid** | Currency (INR ₹) | Records what has already been disbursed |
| **Balance Due** | Formula / Number | `Total Invoiced Amount - Amount Paid` (Directly prevents overpayment) |
| **Payment Status** | Dropdown | `Unpaid`, `Partially Paid`, `Fully Paid` |
| **Due Date** | Date | Payment or milestone deadline |

---

### 5. Automations Implemented

#### Automation 1: Automated Phase Handoff (Design to Procurement)
- **Trigger:** When Task Status changes to `05. Sourcing & Procurement`.
- **Condition:** List is `Client Projects`.
- **Action:** 
  1. Create a subtask / linked task in `Material Procurement & POs` list titled `"Generate BOQ & Issue Vendor POs for [Project Name]"`.
  2. Set Due Date to **Trigger Date + 5 days**.
  3. Send an internal notification to the Procurement Lead.
- **Value:** Eliminates lag between design sign-off and material ordering.

#### Automation 2: Overpayment & Double-Payment Protection
- **Trigger:** When Custom Field `Payment Status` changes to `Fully Paid`.
- **Condition:** List is `Vendor & Procurement Tracker`.
- **Action:**
  1. Automatically update task status to `Payment Cleared / Closed`.
  2. Add an activity comment: `"[AUTOMATION] Vendor invoice marked FULLY PAID. Balance set to ₹0. Do NOT disburse additional funds without owner override."`
- **Value:** Instantly resolves the owner's primary pain point of paying contractors twice.

#### Automation 3: Project Delay Early Warning System
- **Trigger:** When Due Date arrives and Status is NOT `08. Handover & Completed`.
- **Action:** Change task priority to `Urgent (Red)` and ping the Studio Owner.

---

### 6. The Owner's "10-Second Health Dashboard"
*Built specifically so the owner can glance at 4 widgets and know the exact state of the business:*

1. **Widget 1: "Projects at a Glance" (Pie / Bar Chart)**
   - Grouped by Status: Shows how many projects are in 3D Concept vs. Execution vs. Snagging.
   - *10-Second Takeaway:* Are we taking on too many new sites before finishing existing ones?
2. **Widget 2: "Cash Outflow & Vendor Balances" (Calculation Widget)**
   - Sum of `Balance Due` across all vendors where `Payment Status != Fully Paid`.
   - *10-Second Takeaway:* Exactly how much money Sunrise Interiors owes vendors this week.
3. **Widget 3: "Overdue Milestones & Blockers" (Task List Widget)**
   - Filtered by `Due Date is Overdue` and `Status != Closed`.
   - *10-Second Takeaway:* Zero-in on which site is falling behind schedule without calling anyone.
4. **Widget 4: "Designer Workload / Capacity" (Workload Widget)**
   - Shows active tasks split across:
     - Designer 1 (e.g., Ananya - 4 active projects)
     - Designer 2 (e.g., Rohan - 2 active projects)
     - Designer 3 (e.g., Kavya - 3 active projects)
   - *10-Second Takeaway:* Knows instantly who can take the next incoming client.

---

### 7. Step-by-Step Instructions to Recreate This in ClickUp:
1. Go to [clickup.com](https://clickup.com) and create a free account.
2. Name your workspace: `Sunrise Interiors Studio`.
3. Create Space: `Interior Projects & Operations`.
4. Create the 3 Folders: `1. Client Projects`, `2. Vendor Procurement`, `3. Design Studio Tasks`.
5. Under `1. Client Projects`, create a List named `Active Projects` and add sample tasks:
   - *Task 1:* "Indiranagar 3BHK Penthouse - Mrs. Kapoor" (Status: `06. Site Execution / Fit-out`)
   - *Task 2:* "Whitefield Villa - Dr. Sen" (Status: `03. Concept & 3D Design`)
   - *Task 3:* "Koramangala Studio Apartment - Mr. Nair" (Status: `01. Lead / Initial Inquiry`)
6. Add the Custom Fields (Settings > Custom Fields > Add: `Total Project Budget`, `Carpet Area`, `Lead Designer`).
7. Under `2. Vendor Procurement`, add sample vendor bills:
   - "Greenply Plywood Supply (PO-104)" -> Invoiced: ₹2,50,000 | Paid: ₹1,50,000 | Balance: ₹1,00,000 | Status: `Partially Paid`
   - "Civil Contractor - Marble Polishing" -> Invoiced: ₹85,000 | Paid: ₹85,000 | Balance: ₹0 | Status: `Fully Paid`
8. Click **Automations** (top right) > **Add Automation** > Select Trigger & Action as detailed in Section 5.
9. Click **Dashboards** on the left sidebar > Create `Owner 10-Second Health Dashboard` > Add the 4 widgets.
10. **Generate Guest Link:** Go to **Settings > Sharing & Permissions** (or click the three dots next to the Space/Dashboard) > **Share** > Enable Public Link or Invite `amit12@agileautomate.co` and `aryansh@agileautomate.co` as Guests with View access.

---

# TASK 2: Data Cleaning (Python)

### 1. Problem Statement & Solution
Standardize an incoming messy leads export from Sunrise Interiors:
- Standardize all Indian phone numbers to the strict format `+91XXXXXXXXXX`.
- Strip formatting anomalies (spaces, hyphens, leading zero, existing `+91` or `91` prefixes).
- Deduplicate exact rows (merging duplicate leads such as Sneha Reddy).

### 2. Python Script (`clean_leads.py`)

```python
"""
Data Cleaning Script for Sunrise Interiors Messy Leads
Assignment: Technical Implementation Specialist (Intern) - Agile Automate
"""

import csv
import re
from pathlib import Path


def standardize_phone(phone_raw: str) -> str:
    """
    Standardizes Indian phone numbers to the format '+91XXXXXXXXXX'.
    Handles:
    - 10-digit raw mobile: '9876543210' -> '+919876543210'
    - Country code prefix: '91 98765 12345' -> '+919876512345'
    - Leading trunk zero:  '098-765-99887' -> '+919876599887'
    - Pre-formatted +91:   '+919876500000' -> '+919876500000'
    - Hyphens and spaces:  '+91-9876511111' -> '+919876511111'
    """
    if not phone_raw:
        return ""

    # Strip all non-digit characters
    digits = re.sub(r"\D", "", phone_raw)

    # If number starts with country code 91 (12 digits)
    if len(digits) == 12 and digits.startswith("91"):
        digits = digits[2:]
    # If number starts with trunk prefix 0 (11 digits)
    elif len(digits) == 11 and digits.startswith("0"):
        digits = digits[1:]

    # A valid Indian mobile number contains 10 digits
    if len(digits) == 10:
        return f"+91{digits}"
    else:
        # Fallback for unexpected formats
        return f"+91{digits[-10:]}" if len(digits) >= 10 else phone_raw.strip()


def clean_leads_csv(input_path: str, output_path: str):
    """
    Reads raw CSV, applies phone standardization, deduplicates rows,
    and writes the cleaned records to a new CSV file.
    """
    input_file = Path(input_path)
    output_file = Path(output_path)

    cleaned_records = []
    seen_rows = set()

    with open(input_file, mode="r", encoding="utf-8") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            name = row.get("Name", "").strip()
            raw_phone = row.get("Phone", "").strip()
            clean_phone = standardize_phone(raw_phone)

            record_key = (name, clean_phone)

            # Deduplication: retain only unique (Name, Phone) combinations
            if record_key not in seen_rows:
                seen_rows.add(record_key)
                cleaned_records.append({"Name": name, "Phone": clean_phone})

    # Save cleaned output
    with open(output_file, mode="w", newline="", encoding="utf-8") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=["Name", "Phone"])
        writer.writeheader()
        writer.writerows(cleaned_records)

    return cleaned_records


if __name__ == "__main__":
    clean_leads_csv("messy_leads.csv", "cleaned_leads.csv")
```

---

### 3. Execution Results & Comparison Table

#### Original Messy Input:
```csv
Name,Phone
Ravi Kumar,9876543210
Priya Shah,91 98765 12345
Amit Verma,098-765-99887
Sneha Reddy,+919876500000
Sneha Reddy,9876500000
Karan Mehta,+91-9876511111
```

#### Cleaned Output (`cleaned_leads.csv`):
| No. | Name | Raw Input Phone | Standardized Phone (`+91XXXXXXXXXX`) | Cleaning Action Performed |
| :--- | :--- | :--- | :--- | :--- |
| 1 | **Ravi Kumar** | `9876543210` | `+919876543210` | Added `+91` country code prefix |
| 2 | **Priya Shah** | `91 98765 12345` | `+919876512345` | Removed spaces; standardized `91` to `+91` |
| 3 | **Amit Verma** | `098-765-99887` | `+919876599887` | Stripped leading `0` and hyphens; appended `+91` |
| 4 | **Sneha Reddy** | `+919876500000` / `9876500000` | `+919876500000` | Normalized both entries and **deduplicated into 1 row** |
| 5 | **Karan Mehta** | `+91-9876511111` | `+919876511111` | Stripped hyphens; preserved `+91` prefix |

*Summary:* Initial rows: 6 | Cleaned rows: 5 | Duplicate rows removed: 1 (Sneha Reddy).

---

# TASK 3: Automation Logic (n8n Workflow)

### Scenario
Sunrise Interiors captures inquiries from prospective clients via a Google Form.  
The automation must:
1. Create a new lead card in ClickUp.
2. Send an automated confirmation to the client (Email or WhatsApp).
3. Notify the design team — **only if the budget entered is above ₹5 lakh (₹5,00,000)**.

---

### 1. Visual Workflow Architecture

```text
[ Google Form Submission ] (Trigger)
            │
            ▼
[ Node 1: Data Normalizer & Cleaner ] (Code / Set Node)
  • Parse Name & Phone to +91XXXXXXXXXX
  • Clean Budget string (strip "₹", commas, "lakh") -> Number
            │
            ▼
[ Node 2: ClickUp - Create Lead Task ] (Action)
  • Space: Interior Projects
  • List: 01. Client Inquiries / Leads
  • Map Custom Fields: Budget, Phone, Project Type
            │
            ▼
[ Node 3: Client Confirmation Notification ] (Action)
  • Send WhatsApp / Email: "Thank you for contacting Sunrise Interiors!"
            │
            ▼
[ Node 4: IF Condition (Budget Check) ] (Logic Gate)
  • Condition: {{ $json.budgetNumber }} > 500000
            │
     ┌──────┴────────────────────────┐
     ▼                               ▼
[ TRUE: High-Value Lead ]       [ FALSE: Standard Lead ]
[ Node 5: Alert Design Team ]   [ Node 6: Standard Queue ]
  • Slack/Discord/WhatsApp        • Route to general queue
  • "🚨 Priority Lead Alert:        • No immediate team ping
     Budget > ₹5L! Assign
     Senior Designer ASAP."
```

---

### 2. Breakdown of Nodes & Parameters

#### Step 1: Trigger — `Google Forms Trigger` (or Webhook via Google Apps Script)
- **Event:** `On Form Submit`.
- **Payload Received:**
  - `Client Name`: e.g., "Vikram Malhotra"
  - `Phone Number`: e.g., "9880198801"
  - `Email`: e.g., "vikram@example.com"
  - `Project Budget`: e.g., "7,50,000" or "8 Lakhs"
  - `Apartment Type`: "3BHK Luxury"
  - `Location`: "Indiranagar, Bengaluru"

#### Step 2: Data Normalizer & Parser — `Code Node (JavaScript / Python)`
- In real-world forms, users type numbers inconsistently (e.g., `"₹7.5 Lakhs"`, `"5,00,000"`, `"600000"`).
- **Logic:**
  ```javascript
  let rawBudget = $input.item.json['Project Budget'] || '0';
  // Strip non-numeric characters except decimals
  let cleaned = rawBudget.replace(/[^0-9.]/g, '');
  let numericBudget = parseFloat(cleaned) || 0;
  
  // If user entered "7.5" for Lakhs
  if (numericBudget < 100 && rawBudget.toLowerCase().includes('lakh')) {
    numericBudget = numericBudget * 100000;
  }

  return {
    clientName: $input.item.json['Client Name'],
    clientEmail: $input.item.json['Email'],
    cleanPhone: $input.item.json['Phone Number'].replace(/\D/g, '').slice(-10),
    budgetNumber: numericBudget,
    propertyType: $input.item.json['Apartment Type']
  };
  ```

#### Step 3: Create Lead Card in ClickUp — `ClickUp Node`
- **Resource:** `Task` | **Operation:** `Create`
- **Target Space:** `Interior Projects & Operations`
- **Target List:** `Client Inquiries / Leads`
- **Task Title:** `New Inquiry: {{ $json.clientName }} - {{ $json.propertyType }}`
- **Field Mappings:**
  - `Status`: `01. Lead / Initial Inquiry`
  - `Total Project Budget`: `{{ $json.budgetNumber }}`
  - `Phone`: `+91{{ $json.cleanPhone }}`
  - `Due Date`: `{{ $now.plus({ days: 1 }) }}` (SLA: 24h response time)

#### Step 4: Client Automated Confirmation — `Gmail / WhatsApp Cloud API Node`
- **Action:** Send confirmation email / WhatsApp to the prospective client.
- **Message Content:**
  > *"Hi Vikram, thank you for reaching out to Sunrise Interiors! We have received your inquiry for your 3BHK Luxury project. Our design team is reviewing your requirements and will connect with you within 24 hours to schedule a complimentary site consultation."*
- **Why this step is here:** Every client gets immediate feedback regardless of budget.

#### Step 5: Conditional Logic (The ₹5 Lakh Threshold Check) — `IF Node`
- **Condition Configuration:**
  - Field: `{{ $json.budgetNumber }}`
  - Operator: `Larger than or equal to` (Number)
  - Value: `500000`
- **Evaluation:**
  - If **Budget > ₹5,00,000** -> Proceed to **TRUE** branch (High-Value VIP Lead).
  - If **Budget < ₹5,00,000** -> Proceed to **FALSE** branch (Standard Lead).

#### Step 6: Design Team Notification (High-Value Branch) — `Slack / WhatsApp / Email Node`
- **Channel:** `#design-team-alerts` (Slack) or Design Team WhatsApp Group.
- **Message Content:**
  > *"🚨 **HIGH-VALUE INQUIRY RECEIVED (> ₹5 Lakhs)** 🚨*  
  > *• **Client:** Vikram Malhotra*  
  > *• **Budget:** ₹7,50,000*  
  > *• **Type:** 3BHK Luxury, Indiranagar*  
  > *• **ClickUp Lead:** [View Lead in ClickUp]({{ $json.clickupTaskUrl }})*  
  > *• **Action Required:** Lead Designer must contact client within 2 hours."*

---

### 3. What Could Go Wrong & How to Prevent It (Resilience & Error Handling)

#### Failure Mode: Malformed Budget Data & API Rate Limiting
- **The Problem:** 
  1. If a user types text like *"Let's discuss on call"* or `"Depends on design"` in the budget field, the conditional node could fail with `NaN` or incorrectly route a high-value client to the low-priority queue.
  2. If ClickUp or WhatsApp API experiences temporary downtime or rate-limiting (`HTTP 429 / 500`), the lead would be lost silently without reaching the team.

#### How to Handle It (Production-Grade Fallback):
1. **Input Validation & Sanitization in Google Form:**
   - Enforce **Number Only** response validation in the Google Form settings for the budget field (e.g., minimum value: ₹50,000).
2. **Graceful Fallback Logic in n8n:**
   - If the budget string fails to parse into a valid number, assign a fallback flag: `budgetUncertain = true`.
   - Update the `IF Node` condition to: `budgetNumber >= 500000 OR budgetUncertain == true`. This guarantees that if there is any ambiguity, the lead is treated as a priority rather than missed.
3. **Dedicated n8n Error Trigger Workflow:**
   - Attach an **Error Trigger Node** in n8n.
   - If any step in the primary workflow fails, n8n automatically executes the error branch:
     - Saves the raw payload to a fallback Google Sheet (`Failed_Leads_Backup`).
     - Sends an immediate SMS/Telegram alert to the Operations Lead: *"⚠️ Lead processing failed for [Client Name]. Please check n8n error log."*
   - Enable **Retry on Fail** on the ClickUp node with 3 retries (Exponential Backoff: 5s, 15s, 45s).

---

# SUBMISSION CHECKLIST & EMAIL TEMPLATE

### Checklist Before Sending:
- [x] ClickUp Workspace created with custom fields, at least 1 automation, and Owner 10-Second Dashboard.
- [x] ClickUp guest/public link verified in an incognito window.
- [x] Python script executed, tested, and verified clean (`cleaned_leads.csv` matches expectations).
- [x] n8n automation write-up covers Trigger, Step Sequence, Conditional Logic, and Edge-Case Handling.
- [x] Created Google Doc titled: `[Your Name]_AgileAutomate_tech` and set sharing permission to **"Anyone with the link can comment / edit"**.

### Email Submission Template

**To:** `amit12@agileautomate.co`  
**CC:** `aryansh@agileautomate.co`  
**Subject:** `Technical Implementation Specialist Assignment - [Your Name]`

> Dear Amit and Aryansh,
>
> I hope you are having a productive week.
>
> Please find below my submission for the **Technical Implementation Specialist (Intern)** take-home assignment for Agile Automate.
>
> 📄 **Complete Assignment Document (Google Doc):**  
> `[PASTE YOUR GOOGLE DOC LINK HERE - Ensure view/edit access is enabled]`
>
> 📌 **Key Highlights of the Submission:**
> 1. **Task 1 (ClickUp System):**  
>    - Designed a full workspace for Sunrise Interiors tackling their core pain points: project stage bottlenecks, task allocation across the 3 designers, and a dedicated **Vendor & Procurement Tracker** with balance calculation to permanently prevent duplicate vendor payouts.
>    - Built automations for stage handoffs and double-payment safeguards.
>    - Designed an **Owner 10-Second Health Dashboard** with 4 instant-read executive widgets.
>    - **ClickUp Workspace Guest Link:** `[PASTE YOUR CLICKUP GUEST LINK HERE]`
>
> 2. **Task 2 (Python Data Cleaning):**  
>    - Developed `clean_leads.py` standardizing raw phone inputs into `+91XXXXXXXXXX`, handling leading zeros, spaces, hyphens, and deduplicating rows (e.g., Sneha Reddy).
>    - Full script and before/after verification table are included in the document.
>
> 3. **Task 3 (n8n Automation Architecture):**  
>    - Detailed architectural blueprint for Google Forms -> ClickUp Lead -> Client Auto-confirmation -> Conditional Logic (₹5 Lakh filter) -> High-Priority Design Team Alert.
>    - Provided complete failure mode analysis (data parsing edge cases, API rate limiting, and automated error-handling workflows).
>
> I would love the opportunity to walk you through the system and discuss how I can contribute to Agile Automate. Looking forward to your feedback and the next steps!
>
> Warm regards,  
> **[Your Name]**  
> [Your Phone Number]  
> [Your LinkedIn Profile]
