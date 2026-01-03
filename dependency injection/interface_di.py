from abc import ABC, abstractmethod
from typing import Dict

class NotificationService(ABC):
    @abstractmethod
    def send(self, data: Dict) -> str:
        pass

class EmailService(NotificationService):
    def send(data: Dict) -> str:
        return "Email send successfully"

class SmsService(NotificationService):
    def send(data: Dict) -> str:
        return "Email send successfully"


type = input("Please select notification type (email / sms ) : ")

data = {
    "message" : "hello"
}

if type == "email":
    notify = EmailService.send(data)
elif type == "sms":
    notify = SmsService.send(data)
else:
    raise ValueError("invalid ttype")

print(notify)