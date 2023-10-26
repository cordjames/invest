# import uuid
# from django.db import models
# from django.contrib.auth import get_user_model

# User = get_user_model()

# # Create your models here.

# class Account(models.Model):
#     user = models.OneToOneField(
#         User, 
#         related_name="account",
#         on_delete=models.CASCADE
#         )
#     profit = models.FloatField(default=0.0)
#     id = models.UUIDField(
#         default=uuid.uuid4,
#         editable=False,
#         primary_key=False
#     )
#     account_type = models.CharField(default="standard 500")
#     invested = models.FloatField(default=0.0)



# class Trade(models.Model):
#     id = models.UUIDField(
#         default=uuid.uuid4,
#         editable=False,
#         primary_key=False
#     )
#     account = models.OneToOneField(
#         Account,
#         related_name="trade",
#         on_delete=models.DO_NOTHING
#     ) 
#     amount = models.FloatField(default=0.0)
#     profit = models.FloatField(default=0.0)
#     loss = models.FloatField(default=0.0)
    


