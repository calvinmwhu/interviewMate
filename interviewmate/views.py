from django.shortcuts import render, render_to_response
from interviewmate.models import Category,Question
from interviewmate.form import CategoryForm, QuestionForm
# Create your views here.

def index(request):
    return render(request, 'interviewmate/index.html')

def dashboard(request):
    category_list = Category.objects.order_by('-likes')[:5]
    questions_list = Question.objects.order_by('-views')[:5]
    context_dict = {'categories':category_list, 'questions':questions_list}
    return render(request, 'interviewmate/dashboard.html', context_dict)

def category(request, category_name_slug):
    context_dict={}

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name

        questions = Question.objects.filter(category=category)
        context_dict['questions']=questions
        context_dict['category']=category
        context_dict['category_name_slug']=category_name_slug
    except Category.DoesNotExist:
        pass
    return render(request, 'interviewmate/category.html', context_dict)


def add_category(request):
    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return dashboard(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = CategoryForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'interviewmate/add_category.html', {'form': form})


def add_question(request, category_name_slug):
    try:
        cat = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        cat = None

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            if cat:
                question = form.save(commit=False)
                question.category = cat
                question.views = 0
                question.save()
                return category(request, category_name_slug)
        else:
            print  form.errors
    else:
        form = QuestionForm()

    return render(request, 'interviewmate/add_question.html', {'form':form, 'category':cat})


