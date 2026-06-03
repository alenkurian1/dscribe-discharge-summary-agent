# Discharge Summary Agent

# Discharge Summary Agent

## Overview

This project implements an AI-assisted discharge summary generation workflow from clinical source documents.

## Workflow

1. Read PDF source notes
2. Extract text using OCR
3. Identify diagnoses
4. Detect pending investigations
5. Generate structured discharge summary
6. Save reasoning trace

## Technologies

* Python
* PyMuPDF
* Tesseract OCR
* Pytesseract

## Safety Measures

* No hallucinated information
* Missing information remains blank
* Pending investigations explicitly flagged
* Trace logging for transparency

## Output Files

* raw_text.txt
* output_summary.txt
* trace.json

## Example Diagnosis

* Acute Gastroenteritis with Dehydration
* Urinary Tract Infection
