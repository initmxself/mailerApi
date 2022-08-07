from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone

# Create your models here.

class Mailing(models.Model):
    
    mail_id = models.TextField(
            
            max_length = 200, 
            
            verbose_name= 'User\'s ID',
            
            unique = True
    )

    message = models.TextField( 
            
            max_length = 3000, 
            
            verbose_name = 'Message'
    )
    
    codes = models.CharField("Mobile operator codes", max_length = 50, blank=True)
    
    tags = models.CharField("Tags", max_length = 50, blank = True)
    
    startingTime = models.DateTimeField(verbose_name = "Starting time")
    
    endingTime = models.DateTimeField(verbose_name = "Ending time")

    @property
    def toSend(self):
        now = timezone.now()

        if self.endingTime >= now >= self.startingTime:
            return True
        else:   return False

    @property
    def sentMsg(self):
        return len(self.messages.filter(status='sent'))

    @property
    def msgToSend(self):
        return len(self.messages.filter(status = 'suceeded'))

    @property
    def failedMsg(self):
        return len(self.messages.fillter(status = 'failed'))

    def __str__(self):
        return f'Message {self.id} at {self.startingTime}'

    class Meta:
        verbose_name = 'mailing'


class Client(models.Model):
    
    client_id = models.TextField(
            
            max_length = 50,
            
            verbose_name = 'Client\'s ID',
            
            unique = True
    )

    phone_regex = RegexValidator(regex=r'^7\w{10}$',
            
            message = 'Phone number in the format 7XXXXXXXXXX (X - digits  0 - 9)')
    
    phone = models.PositiveIntegerField(verbose_name = 'Phone number', validators = [phone_regex])
    
    code = models.PositiveIntegerField(verbose_name = 'Mobile operator code')
     
    tag = models.CharField(verbose_name = 'Search tags', max_length = 50, blank = True)
    
    time_zone = models.CharField(verbose_name = 'Time zone', max_length = 10)

    
    def __str__(self):
        return f'Client {self.id} with the number {self.phone}'

class Meta:
    verbose_name = 'Client'


class Message(models.Model):
    
    SENT = "sent"
    
    SUCCEEDED = "succeeded"
    
    FAILED = "failed"
    
    STATUS_CHOICES = [
           
            (SENT, "Sent"), 
            
            (SUCCEEDED, "Succeeded"),
            
            (FAILED, "Failed"),
    
    ]


    date = models.DateTimeField(verbose_name = 'Date sent', auto_now_add = True)
    
    status = models.CharField(

            verbose_name = 'Status', 

            max_length = 15, 

            choices = STATUS_CHOICES
    )
                        
    message = models.ForeignKey(
            
            Mailing, 
            
            on_delete = models.CASCADE, 
            
            related_name = 'messages')
                    
    client = models.ForeignKey(

            Client, 
            
            on_delete = models.CASCADE, 

            related_name = 'clients'
    )

                                                                            
    def __str__(self):

        return f'Message {self.id} that reads {self.message} for {self.client}'

    class Meta:

        verbose_name = 'Message'




