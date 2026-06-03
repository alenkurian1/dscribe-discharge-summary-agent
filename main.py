from tools.pdf_reader import extract_text
from agents.diagnosis_extractor import extract_diagnoses

text = extract_text("patient.pdf")

diagnoses = extract_diagnoses(text)

summary = f"""
DISCHARGE SUMMARY

PRIMARY DIAGNOSIS:
{diagnoses[0] if len(diagnoses) > 0 else "N/A"}

SECONDARY DIAGNOSIS:
{diagnoses[1] if len(diagnoses) > 1 else "N/A"}

PAST HISTORY:
Thyroid Disorder (on treatment)

PENDING RESULTS:
Urine Culture and Sensitivity - Report Awaited

DISCHARGE CONDITION:
Hemodynamically Stable
"""

print(summary)

with open("output_summary.txt", "w", encoding="utf-8") as f:
    f.write(summary)

print("Saved output_summary.txt")