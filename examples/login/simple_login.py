from iqoptionapi.stable_api import IQ_Option
import time

Iq = IQ_Option("email", "password")
status, reason = Iq.connect()

while True:
    if not status:
        print("try reconnect")
        status, reason = Iq.connect()
    else:
        print("reconnect Success")
        break
    time.sleep(1)
print("connected!")

balance = Iq.get_balance()
print("Balance:", balance)
