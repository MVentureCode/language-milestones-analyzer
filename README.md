# Language Milestones Analyzer

A clinical Python tool that crosses child language profiles with normative 
development milestones and generates structured reports for speech-language 
pathology practice.

## Why this project exists

Most speech-language pathology tools are either too generic or too complex 
for everyday clinical use. This analyzer was built from real practice — 
combining more than 10 years of clinical experience in child language, 
neurodevelopment, and AAC with Python to create something that is both 
clinically meaningful and technically functional.

## What it does

- Loads a child profile from a CSV file (age, referral reason, clinical 
  background, caregiver description)
- Matches the child's age to the corresponding normative milestone stage
- Compares the profile against expected milestones across three domains:
  Form, Content and Use (Bloom & Lahey framework)
- Flags clinical alert signals for each developmental stage
- Generates a structured report saved as a text file

## Clinical framework

Milestones are based on:
- **Bloom & Lahey (1978)** — Form, Content, Use model
- **Bosch (2004)** — Phonetic-phonological acquisition in Spanish
- **Halliday (1975)** — Language functions
- **Piaget** — Cognitive stages as semantic foundation

## Project structure
- language-milestones-analyzer/
- milestones.json       # Normative milestones 0–7 years (11 stages)
- children_data.csv     # Fictional child profiles for testing
- analyzer.py           # Main script
- output/               # Generated clinical reports

## How to run it

```bash
git clone https://github.com/MVentureCode/language-milestones-analyzer.git
cd language-milestones-analyzer
python3 analyzer.py
```

Reports will be generated in the `/output` folder, one per child profile.

## Tech stack

- Python 3
- Standard libraries: json, csv, os, datetime
- No external dependencies required

## About the author

Speech-language pathologist with clinical experience in child language 
disorders, neurodevelopment, AAC, and dysphagia. Currently combining 
clinical knowledge with Python to build tools at the intersection of 
speech-language pathology and health technology.

→ Exploring the intersection of speech language pathology and health technology.