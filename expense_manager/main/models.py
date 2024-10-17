from django.db import models

class Worker(models.Model):
    #id has allready added with django
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    work_type = models.CharField(max_length=255)
    act = models.CharField(max_length=20)
    section = models.CharField(max_length=4)
    teta_nr = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.work_type}"


class Card(models.Model):
    #id has allready added with django
    rfid = models.CharField(max_length=8)
    card_nr = models.CharField(max_length=8)
    id_worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='cards')

    def __str__(self):
        return f"Card {self.card_nr} (RFID: {self.rfid})"


class Registration(models.Model):
    #id has allready added with django
    datetime = models.DateTimeField()
    id_worker = models.ForeignKey(Worker, on_delete=models.CASCADE, related_name='registrations')
    id_card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='registrations')

    def __str__(self):
        return f"Registration on {self.datetime} by {self.id_worker}"
