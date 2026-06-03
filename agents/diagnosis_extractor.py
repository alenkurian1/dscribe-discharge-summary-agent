import re

def extract_diagnoses(text):

    diagnoses = []

    lines = text.splitlines()

    for i, line in enumerate(lines):

        if "DIAGNOSIS:" in line.upper():

            for j in range(i + 1, min(i + 10, len(lines))):

                diagnosis = lines[j].strip()

                if diagnosis:

                    if diagnosis.startswith("1)") or diagnosis.startswith("2)"):
                        diagnoses.append(diagnosis)

            break

    return diagnoses