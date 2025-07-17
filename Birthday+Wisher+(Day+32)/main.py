##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import pandas as pd
import smtplib
import datetime
import random
import os
import dotenv

dotenv.load_dotenv()

# Read CSV file
csv_data=pd.read_csv("birthdays.csv")
# read csv file data
birth_month=csv_data["month"]
birth_date=csv_data["day"]
Name=csv_data["name"]
Email=csv_data["email"]

# convert data into plain text

for i in range(len(csv_data)):
    a=birth_month.iloc[i]
    # print(a)
    b=birth_date.iloc[i]
    # print(b)
    c=Name.iloc[i]
    # print(c)
    d=Email.iloc[i]
    # print(d)


    # Load the current day and month
    current = datetime.datetime.now()
    current_date=current.day
    current_month=current.month


    # Choose random text file
    letter_choice="letter_templates/letter_1.txt","letter_templates/letter_2.txt","letter_templates/letter_3.txt"
    choice_file=random.choice(letter_choice)
    # print(choice_file)

    # Here automatically send message
    with open (choice_file,"r") as file:
            # here use replace method to replace [name] and add Birthman name
            replace_name = file.read()
            fresh_docs = replace_name.replace("[NAME]", c)
            print(fresh_docs)


# Send Email to that user
    if current_date==b and current_month==a:
            my_email = os.getenv("EMAIL")
            password = os.getenv("PASSWORD")

            with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
                connection.starttls()
                connection.login(user=my_email,password=password)

                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=d,
                    msg=f"Subject:Happy Birthday Boy\n\n{fresh_docs} "
)












