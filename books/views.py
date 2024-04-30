from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
  return render(request, 'books/index.html', {
    'title': 'Books',
    'books': [
      'The Great Gatsby',
      'The Catcher in the Rye',
      'To Kill a Mockingbird',
    ]
  })

def about(request):
  return render(request, 'books/about.html', {
    'title': 'About'
  })

# Django also has an expected folder structure for these templates.

# app/templates/app/index.html
# app name / templates, so a template folder / app name again / within that folder, the template file