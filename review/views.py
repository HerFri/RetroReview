from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django import forms
from .models import Game, Review, Comment
from .forms import CommentForm, GameFilterForm
from .years import YEARS
from .platforms import PLATFORMS



class GameList(generic.ListView):
    """
    Renders all objects of Game model as list
    """
    model = Game
    queryset = Game.objects.all()   
    template_name = 'index.html'
    paginate_by = 6


class GameDetail(View):   
    
    def get(self, request, slug, *args, **kwargs):
        queryset = Review.objects.filter(status=1)       
        game = get_object_or_404(Game, slug=slug)
        reviews = game.review_set.filter(status=1).order_by('-created_on') 
        liked = False
        if request.user.is_authenticated:
            if reviews.filter(likes=request.user).exists():
                liked = True



        return render(
            request,
            "game_detail.html",
            {   
                "game": game,
                "reviews": reviews,     
                "liked": liked,
            },
        )
    
class ReviewDetail(View):
    def get(self, request, game, review, *args, **kwargs):
        queryset = Review.objects.filter(status=1)
        game = get_object_or_404(Game, slug=game)
        review = get_object_or_404(queryset, slug=review)
        comments = review.comments.filter(approved=True).order_by('created_on')
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "review_detail.html",
            {
                "review": review,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "game": game,
                "comment_form": CommentForm()
            }
        )
    
    def post(self, request, game, review, *args, **kwargs):
        queryset = Review.objects.filter(status=1)
        game = get_object_or_404(Game, slug=game)
        review = get_object_or_404(queryset, slug=review)
        comments = review.comments.filter(approved=True).order_by('created_on') 
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.author = request.user
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "review_detail.html",
            {
                "review": review,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "game": game,
                "comment_form": CommentForm()
            }
        )

class ReviewLike(LoginRequiredMixin, View):
    """
    Allows authenticated users to like or unlike a review
    """
    def post(self, request, game, review):
        review = get_object_or_404(Review, slug=review)
        game= get_object_or_404(Game, slug=game)
        
        if review.likes.filter(id=request.user.id).exists():
            review.likes.remove(self.request.user)
        else:
            review.likes.add(request.user)
        return HttpResponseRedirect(reverse('review_detail', args=[game.slug, review.slug]))
    
@login_required        
def edit_comment(request, comment_id):
    """
    Allows authenticated users to edit a comment
    """
    comment = get_object_or_404(Comment, pk=comment_id, author=request.user)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('review_detail', game = comment.review.game.slug, review=comment.review.slug,)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'edit_comment.html', {'form': form, 'comment': comment})


@login_required
def delete_comment(request, comment_id):
    """
    Allows authenticated users to delete a comment
    """
    if (request.user.is_superuser):
        comment = get_object_or_404(Comment, pk=comment_id)
    else:
        comment = get_object_or_404(Comment, pk=comment_id, author=request.user)
    if request.user.is_superuser or request.user == comment.author:
        if request.method == 'POST':
            comment.delete()
            return redirect('review_detail', game = comment.review.game.slug, review=comment.review.slug,)
        return render(request, 'delete_comment.html', {'comment': comment})
    else:

        return redirect('review_detail', review_id=comment.review.id)
    
def filter_games(request):
    """
    Allows users to filter games
    """
    games = Game.objects.all()  
    form = GameFilterForm(request.GET)
    if form.is_valid():
        platform = form.cleaned_data.get("platform")
        year = form.cleaned_data.get("year")
        if platform:
            games = games.filter(platform=platform)
        if year:
            games = games.filter(year=year)
    return render(request, "filtered_games.html", {"games": games, "form": form})