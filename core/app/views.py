from django.shortcuts import render
from django.db import transaction
from .models import Account

def conditional_transfer(sender_id, recipient_id, amount, mode="normal"):
    try:
        with transaction.atomic():
            sender = Account.objects.get(id=sender_id)
            recipient = Account.objects.get(id=recipient_id)

            if sender.balance < amount:
                raise ValueError("Недостаточно средств")

            sender.balance -= amount
            sender.save()

            if mode == "error":  
                raise Exception("Принудительная ошибка — транзакция отменена")

            elif mode == "zero_transfer":  
                print("Режим проверки — перевод не выполнен, но транзакция успешна")

            else: 
                recipient.balance += amount
                recipient.save()

        print("Транзакция успешно завершена")
    except Exception as e:
        print("ОШИБКА:", e)

