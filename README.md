[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/n4D8CCZk)
# Python Project -- TA Grading System

Suppose you are a TA for a class. You would like to automatically grade students assignment and send back the feedbacks through e-mails.

# Grading
The student assignments are included in the [submissions](submissions) folder named as
```
submission_student_123,
submission_student_234,
submission_student_456,
.....
```
The last 3 digits are student's ID number.

The grading rubic is listed [here](grading_rubic.md).

# Report
1. Create a report_student_i.html (replacing i with the student ID number) file for each student, which contains (in reasonably formatted, valid HTML):
   - the name of the student's submission(linked to the file itself)
   - the different integers, decimals, email addresses, prices, phone numbers in the student's submission (list each category  separately)
   - the total scores of the submission
2. Create a valid HTML web page called index.html with links to each of the summary files;
3. Create a tar.gz file containing the directory [submissions](submissions) and the directory that contains all the HTML files you created above. Be sure the links in the webpages work after extraction.
   
# email the reports

1. Read the students' email addresses from the CSV file [Roster](Roster.csv). Send report_student_i.html to the correct student.
2. Prompt the user for the email address (professor's email) and send the tar.gz file.
Please note that you need to send 4 emails in total. Three are for students, and they should be sent directly when you run the script. One is for the professor, which requires you to enter the professor's email address. You can use your own email for testing purposes.
 

# Important Note
Don't hard-code students' email addresses in the script. The student's email should be read from the roster.

You must run your project on Altair and send mail from your @cs.oswego.edu account. You must send mail from the terminal using the mutt command. A little Googling and looking at the man pages should tell you how to use it. The mutt command should not prompt the user for any input. Sender's email password should not appear in your script.

A successful demo will involve sending the emails.
As a student in the class, I can receive the HTML file containing my summary and grade.
As a professor in the class, I can receive the zipped file, extract it, and view students' submissions and reports by following the links on your page.


# Dev Environment / Useful Resources
- [PyCharm](https://www.jetbrains.com/pycharm/)
- [Regular Expressions in Python 3.6](https://docs.python.org/3/howto/regex.html)
- [Regular Expression Debugger / Tester](https://regex101.com/)





