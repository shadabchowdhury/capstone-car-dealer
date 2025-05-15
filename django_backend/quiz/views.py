from django.shortcuts import render, get_object_or_404
from .models import Question, Submission

def course_detail(request):
    return render(request, 'course_details_bootstrap.html')

def submit_exam(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    selected_choice = request.POST.get('choice')
    return render(request, 'result.html', {'question': question, 'choice': selected_choice})

