from django import forms
from .models import candidate_data
 
class MyForm(forms.ModelForm):
  class Meta:
    model = candidate_data
    fields = ["candidate_name", "resume_portfolio_link","primary_skills","secondary_skills","candidate_experince"]
    labels = {'candidate_name': "Name", "resume_portfolio_link": "drop link of your resume",'primar_skills': "enter your primary skills",'secondary_skills': "enter your secondary sklls",'candidate_experince': "enter you experience in years",}