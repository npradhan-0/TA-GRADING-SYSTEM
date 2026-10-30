import re
import csv
import os
from collections import OrderedDict
import tarfile


def load_roster(path='Roster.csv'):
    roster = {}
    try:
        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                roster[row['Student ID']] = row['Email address']
        return roster
    except FileNotFoundError:
        print(f"Error: Roster file '{path}' not found")
        return {}

def extract_unique_items(text, pattern):
  # top 5 and unique
    matches = re.findall(pattern, text)
    return list(OrderedDict.fromkeys(matches))[:5]

def extract_all_items(text, pattern):
    return list(set(re.findall(pattern, text)))

def remove_overlapping_items(text, patterns):
    for pattern in patterns:
        text = re.sub(pattern, ' ', text)
    return text

def grade_submission(text):
    email_pattern = r'\b[a-zA-Z0-9._%+-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b'
    price_pattern = r'\$(?:\d{1,3}(?:,\d{3})*|\d+)(?:\.\d{2})?\b'
    phone_pattern = r'(?:\(\d{3}\)\s?|\d{3}[-.])\d{3}[-.]\d{4}\b'

    emails = extract_unique_items(text, email_pattern)
    prices = extract_unique_items(text, price_pattern)
    phones = extract_unique_items(text, phone_pattern)

    text_clean = remove_overlapping_items(text, [email_pattern, price_pattern, phone_pattern])

    decimal_pattern = r'(?<=\s)-?\d+\.\d+(?=\b|,)(?!\.\d)'
    integer_pattern = r'\b(?<![\d$.-])\b-?\d+\b(?![\d.])\b'

    decimals = extract_unique_items(text_clean, decimal_pattern)
    integers = extract_unique_items(text_clean, integer_pattern)

    score = 0
    results = {}
    for category, items in [('emails', emails), ('prices', prices),
                            ('phone_numbers', phones), ('decimals', decimals),
                            ('integers', integers)]:
        count = len(items)
        points = min(count, 5) * 4
        score += points
        results[category] = {
            'items': items,
            'count': count,
            'points': points
        }

    return score, results

def process_submissions_and_generate_reports(roster):
    if not os.path.exists('reports'):
        os.mkdir('reports')
    for student_id in roster:
        try:
            with open(f"submissions/submission_student_{student_id}.txt", 'r') as f:
                submission_text = f.read()

            score, details = grade_submission(submission_text)
            create_html_report(student_id, details, score)

        except FileNotFoundError:
            print(f"Warning: Submission not found for student {student_id}")

def create_html_report(student_id, details, score):
    filename = f"reports/report_student_{student_id}.html"
    with open(filename, 'w') as f:
        f.write(f"<html><head><title>Report for Student {student_id}</title></head><body>")
        f.write(f"<h1>Submission Report for Student {student_id}</h1>")
        f.write(f"<p>Score: {score}</p>")
        f.write(f'<p><a href="../submissions/submission_student_{student_id}.txt">View Submission</a></p>')

        for category, data in details.items():
            f.write(f"<h2>{category.capitalize()}</h2>")
            f.write(f"<ul>")
            for item in data['items']:
                f.write(f"<li>{item}</li>")
            f.write(f"</ul>")

        f.write(f"</body></html>")
    print(f"Created HTML report for student {student_id}")

def create_index_html(roster):
    with open('index.html', 'w') as f:
        f.write("<html><head><title>Student Reports</title></head><body>")
        f.write("<h1>Student Reports</h1>")
        for student_id in roster:
            f.write(f"<p><a href='reports/report_student_{student_id}.html'>Student {student_id}</a></p>")
        f.write("</body></html>")
    print("Created index.html")

def create_tarball():
    with tarfile.open('reports_and_submissions.tar.gz', 'w:gz') as tar:
        tar.add('submissions')
        tar.add('index.html')
        tar.add('reports')
    print("Created tarball of reports and submissions")

def send_email(to_email, subject, body, attachment):
    command = f'echo "{body}" | mutt -s "{subject}" -a "{attachment}" -- {to_email}'
    os.system(command)

def email_reports_to_students(roster):
    for student_id, email in roster.items():
        report_path = f"reports/report_student_{student_id}.html"
        if os.path.exists(report_path):
            print(f"Sending report to {email}")
            send_email(
                to_email=email,
                subject=f"Your Submission Report (Student ID: {student_id})",
                body="Please find your submission report attached.",
                attachment=report_path
            )
        else:
            print(f"Report not found for student {student_id}, skipping.")

def email_tarball_to_professor():
    prof_email = "npradhan@oswego.edu"
    if os.path.exists('reports_and_submissions.tar.gz'):
        print(f"Sending tar file to {prof_email}")
        send_email(
            to_email=prof_email,
            subject="All Reports and Submissions",
            body="Attached is the full set of reports and submissions.",
            attachment='reports_and_submissions.tar.gz'
        )
    else:
        print("Tarball not found. Please ensure it has been created.")

if __name__ == '__main__':
    roster = load_roster()
    if not roster:
        exit(1)
    process_submissions_and_generate_reports(roster)
    create_index_html(roster)
    create_tarball()
    email_reports_to_students(roster)
    email_tarball_to_professor()

# scp -r /Users/nivapradhan/PycharmProjects/05-python-project-npradhan-0 npradhan@altair.cs.oswego.edu:~
# ssh
# run main

