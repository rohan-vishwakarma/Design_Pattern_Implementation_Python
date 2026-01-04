from typing import Dict

class EmailService:

    def __init__(self, config: Dict):
        self.host = config['host']
        self.port = config['port']
        self.password = config['password']

    def send(self) -> str:
        return "Email send successfully"

class UserService:
    def __init__(self, email_service):
        self.email_service = email_service

    def send_email(self):
        return self.email_service.send()


configuration = {
    'host' : "localhost",
    "port" : 4000,
    "password": "hello"
}
email_service = EmailService(configuration)
user = UserService(email_service)
print(user.send_email())
