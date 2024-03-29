from os import getenv

from twilio.rest import Client

"""
https://cd/en-us
"""


def sending_sms(text="Wake up Neo...", receiver="+11100011100"):
    try:
        account_sid = getenv("YOUR_ACCOUNT_SID")
        auth_token = getenv("YOUR_AUTH_TOKEN")

        twilio_ = Client(account_sid, auth_token)

        message = twilio_.messages.create(
            body=text, from_=getenv("SENDER"), to=receiver
        )
        print(
            "The message was successfully sent.",
        )
        return message

    except Exception as ex:
        return print("Something was wrong... :(", ex)


def main():
    text = input("Please enter your message: ")
    receiver = str(getenv("RECEIVER"))
    sending_sms(text=text, receiver=receiver)


if __name__ == "__main__":
    main()
