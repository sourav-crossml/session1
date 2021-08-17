from django.db import models




class candidate_data(models.Model):
    """
    this model stores data from the user or job seeker and store it in SQLite DB
    """
    
    candidate_name = models.CharField(max_length=200)
    resume_portfolio_link = models.URLField(max_length=200)
    primary_skills = models.CharField(max_length=200)
    secondary_skills = models.CharField(max_length=200)
    candidate_experince = models.IntegerField()

    def __str__(self):
        """
        this function will help in displaying candidate name 
        """
        return self.candidate_name