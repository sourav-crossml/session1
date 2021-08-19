from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import candidate_data
# Create your views here.
def index(request):
    # a=candidate_data.objects.all().values()
    return render(request,"index.html")
    # return HttpResponse(a)

def save_data(request):
    if request.method == 'POST':
        if request.POST.get('candidate_name') and request.POST.get('resume_portfolio_link') and request.POST.get('primary_skills') and request.POST.get('secondary_skills') and request.POST.get('candidate_experince'):
            post=candidate_data()
            post.candidate_name= request.POST.get('candidate_name')
            post.resume_portfolio_link= request.POST.get('resume_portfolio_link')
            post.primary_skills= request.POST.get('primary_skills')
            post.secondary_skills= request.POST.get('secondary_skills')
            post.candidate_experince= request.POST.get('candidate_experince')
            post.save()            
            return render(request, 'index.html') 
        else:
            return HttpResponse("Invalid data entered.") 
    else:
            return render(request,'index.html')


def show_details(request):
    users=candidate_data.objects.all()
    return render(request, 'all_candidate.html', {'users': users})


def show_individual_data(request,id):
    # user=candidate_data.objects.get(pk=id)
    user=get_object_or_404(candidate_data,pk=id)

    return render(request, 'candidate_data.html', {'user': user})
