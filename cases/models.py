from django.db import models

# Create your models here.
class Case(models.Model):

    case_name = models.CharField(max_length=255)

    officer_name = models.CharField(max_length=255)

    case_loc = models.CharField(max_length=255)

    case_date = models.DateField()

    case_status = models.CharField(
        max_length=100,
        default="Open"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.case_name

class Evidence(models.Model):
    
    #case_id = models.IntegerField()
    case= models.ForeignKey(

        Case,

        on_delete=models.CASCADE,

        related_name="evidences"
    )


    evidence_name = models.CharField(
        max_length=255
    )

    file_name = models.CharField(
        max_length=255
    )

    file_path = models.FileField(
        upload_to='evidence/'
    )

    file_type = models.CharField(
        max_length=100
    )

    class Meta:

        db_table = "evidence" 