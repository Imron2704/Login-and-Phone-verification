from django.db import models
from django.contrib.auth.models import User
from twilio.rest import Client



class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100 )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Messages(models.Model):
    name = models.CharField(max_length = 100)
    score = models.IntegerField(default = 0)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if self.score >= 70:
            account_sid = 'AC17eea34a7f535805a54439b7d6ce6903'
            auth_token = '4436946c7252ef350e6ae39acced3fad'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"Congratulations {self.name}, your score is {self.score}",
                from_='+19378073893',
                to='+998935772704'
            )
        else:
            account_sid = 'AC17eea34a7f535805a54439b7d6ce6903'
            auth_token = '4436946c7252ef350e6ae39acced3fad'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"Sorry {self.name}, your score is {self.score} and below 70. Try again!",
                from_='+19378073893',
                to='+998935772704'
            )

        print(message.sid)
        return super().save(*args, **kwargs)
