import json
import csv
import os
from datetime import datetime

# ── Load data ──────────────────────────────────────────────────────────────
# Reads clinical language milestones from a JSON file and child data from a CSV file.
def load_milestones(path="milestones.json"):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def load_children(path="children_data.csv"):
    children = []
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            children.append(row)
    return children

# ── Match child age to milestone stage ─────────────────────────────────────
# Converts child age in years and months to a key that matches the milestones stages.
def get_stage_key(age_years, age_months):
    total_months = age_years * 12 + age_months
    if total_months <= 3:
        return "0_3m"
    elif total_months <= 6:
        return "3_6m"
    elif total_months <= 9:
        return "6_9m"
    elif total_months <= 12:
        return "9_12m"
    elif total_months <= 18:
        return "12_18m"
    elif total_months <= 24:
        return "18_24m"
    elif total_months <= 36:
        return "2_3y"
    elif total_months <= 48:
        return "3_4y"
    elif total_months <= 60:
        return "4_5y"
    elif total_months <= 72:
        return "5_6y"
    else:
        return "6_7y"

# ── Generate report ─────────────────────────────────────────────────────────
# Cross-references the child's profile with their developmental milestones and builds the report text.
def generate_report(child, milestones):
    age_years = int(child["age_years"])
    age_months = int(child["age_months"])
    stage_key = get_stage_key(age_years, age_months)
    stage = milestones["stages"].get(stage_key, {})

    report = []
    report.append("=" * 60)
    report.append(f"CLINICAL LANGUAGE MILESTONE REPORT")
    report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    report.append("=" * 60)
    report.append(f"Child:        {child['name']}")
    report.append(f"Age:          {age_years} years {age_months} months")
    report.append(f"Gender:       {child['gender']}")
    report.append(f"Referred by:  {child['referring_agent']}")
    report.append(f"Reason:       {child['referral_reason']}")
    report.append("-" * 60)
    report.append(f"Caregiver description:")
    report.append(f"  '{child['caregiver_description']}'")
    report.append("-" * 60)
    report.append(f"Normative stage: {stage.get('label', 'N/A')} — {stage.get('stage', '')}")
    report.append(f"Framework: {milestones['framework']}")
    report.append("")
    report.append("EXPECTED MILESTONES FOR THIS AGE:")
    report.append("")
    report.append("  FORM (Phonology & Morphosyntax):")
    for item in stage.get("forma", []):
        report.append(f"    · {item}")
    report.append("")
    report.append("  CONTENT (Semantics):")
    for item in stage.get("contenido", []):
        report.append(f"    · {item}")
    report.append("")
    report.append("  USE (Pragmatics):")
    for item in stage.get("uso", []):
        report.append(f"    · {item}")
    report.append("")
    report.append("  ⚠ ALERT SIGNAL:")
    report.append(f"    {stage.get('alert', 'No alert defined for this stage')}")
    report.append("")
    report.append("CLINICAL BACKGROUND:")
    report.append(f"  Birth weight:        {child['birth_weight_kg']} kg")
    report.append(f"  Pregnancy notes:     {child['pregnancy_complications']}")
    report.append(f"  Birth notes:         {child['birth_complications']}")
    report.append(f"  First steps:         {child['first_steps_months']} months")
    report.append(f"  First words:         {child['first_words_months']} months")
    report.append(f"  Sphincter control:   {child['sphincter_control']}")
    report.append(f"  Home play/social:    {child['home_social_play']}")
    report.append(f"  School play/social:  {child['school_social_play']}")
    report.append(f"  Extracurricular:     {child['extracurricular_activities']}")
    report.append("=" * 60)

    return "\n".join(report)

# ── Save report to file ─────────────────────────────────────────────────────
# Saves the generated report text to a .txt file in the output folder, named after the child.
def save_report(report_text, child_name):
    os.makedirs("output", exist_ok=True)
    filename = f"output/report_{child_name.replace(' ', '_').replace('.', '')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report_text)
    print(f"  ✓ Report saved: {filename}")

# ── Main ────────────────────────────────────────────────────────────────────
# Orchestrates the loading of data, generation of reports for each child, and saving the reports to files. 
# Prints progress messages to the console.
def main():
    print("\nLoading data...")
    milestones = load_milestones()
    children = load_children()
    print(f"  ✓ {len(children)} children loaded")
    print(f"  ✓ {len(milestones['stages'])} milestone stages loaded")
    print("\nGenerating reports...")

    for child in children:
        report = generate_report(child, milestones)
        save_report(report, child["name"])

    print(f"\nDone. {len(children)} reports generated in /output folder.")

if __name__ == "__main__":
    main()