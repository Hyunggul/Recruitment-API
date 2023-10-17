from django.db import models

class Company(models.Model):
    name = models.CharField(help_text="회사명", max_length=50, primary_key=True)
    country = models.CharField(help_text="국가", max_length=30)
    area = models.CharField(help_text="지역", max_length=30)

    def __str__(self):
        return self.name
    
class Recruitment(models.Model):
    recruitment_id = models.BigAutoField(help_text="채용공고 id", primary_key=True)
    company_name = models.ForeignKey("Company", on_delete=models.CASCADE)
    position = models.CharField(help_text="채용포지션", max_length=50)
    compensation = models.IntegerField(help_text="채용보상금")
    context = models.TextField(help_text="채용내용")
    tech_stack = models.CharField(help_text="사용기술", max_length=100)

    users = models.ManyToManyField(to='User', related_name='recruitments')

    def __str__(self):
        return self.company_name, self.position
    
class User(models.Model):
    recruitment_id = models.ForeignKey("Recruitment", on_delete=models.CASCADE)
    name = models.CharField(help_text="유저명", max_length=50, primary_key=True)
    
    def __str__(self):
        return self.name
