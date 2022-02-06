import smtplib

EMAIL_LOGIN = "Login"
PASS= "Password?"
ADDRES = "example@examlpe.com"
TO = "exsamplesendto@example.com"

# with smtplib.SMTP("smtp.gmail.com") as smtp:
#     smtp.starttls()
#     smtp.login(user=ADDRES, password=PASS)
#     smtp.sendmail(from_addr=ADDRES, to_addrs=TO,
#                   msg=f"""hiii""")

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def ocasion_messages(self, ocasions, users):
        # for name in ocasions:
        with smtplib.SMTP("smtp.gmail.com") as smtp:
            smtp.starttls()
            message =''
            for name in ocasions:
                # print(ocasions[name])
                # print(ocasions[name][1])
                # print(ocasions[name][0][0]["price"])
                for key in ocasions[name]:
                    # print(key)
                    for ki in key:
                        # print(ki)
                        message += f"""The nearest ocasional flights to {name}:\n priced: {key[ki]["price"]}\n link: {key[ki]["deep_link"]}\n date: {key[ki]["local_departure"]}\n
                         and : priced: {key[ki]["price"]}\n link: {key[ki]["deep_link"]}\n date: {key[ki]["local_departure"]}\n"""
            smtp.login(user=ADDRES, password=PASS)
            for email in users["Email"]:
                smtp.sendmail(from_addr=ADDRES, to_addrs=users["Email"][email],
                        msg=f"""Subject:Flight ocasions {name}\n\n{message}""")
    pass

















