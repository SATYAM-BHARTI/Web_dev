from django.shortcuts import render
from .models import Review

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        rating = request.POST.get('rating')
        review_text = request.POST.get('review_text')
        review = Review(name=name, email=email, rating=rating, review_text=review_text)
        review.save()
        return render(request, 'reviews/thanks.html')
        return render(request, 'reviews/index.html')

    else:
        # retrieve all the reviews from the database
        reviews = Review.objects.all()
        context = {'reviews': reviews}
        return render(request, 'reviews/index.html', context)