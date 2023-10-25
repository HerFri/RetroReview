from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Game, Review, Comment
from .forms import CommentForm

# Create your views here.

class GameList(generic.ListView):
    model = Game
    queryset = Game.objects.all()   # .order_by('-rating')
    template_name = 'index.html'
    paginate_by = 6


class GameReviews(generic.ListView):    # Site, where all Reviews are listed
    model = Review
    #slug = Game.slug                      # --> TO BE EDITED!
    queryset = Review.objects.all()        #(slug=slug)      # filter() #all() # Review.objects.filter(slug=game.title)
    template_name = 'reviews.html'       #for every game there is a different slug (URL)
    paginate_by = 6



class GameDetail(View):   #Früher: ReviewDetail
    
    def get(self, request, slug, *args, **kwargs):
        #review = Review,
        queryset = Review.objects.filter(status=1)     #  
        game = get_object_or_404(Game, slug=slug)
        reviews = game.review_set.filter(status=1).order_by('-created_on') # Get all reviews related to the game
        #comments = review.comments.filter(approved=True).order_by('created_on') # in walktrough: comments.filter(approved=True).order_by
        liked = False
        if request.user.is_authenticated:
            if reviews.filter(likes=request.user).exists():
                liked = True
        #if review.likes.filter(id=self.request.user.id).exists():
        #    liked = True

        return render(
            request,
            "game_detail.html",
            {   
                "game": game,
                "reviews": reviews,     # Pass the reviews related to the game to the context
                #"comments": comments,
                #"commented": True,
                "liked": liked,
                #"review_form": ReviewForm()

                #"comment_form": CommentForm(),
            },
        )
    
class ReviewDetail(View):
    def get(self, request, game, review, *args, **kwargs):
        queryset = Review.objects.filter(status=1)
        game = get_object_or_404(Game, slug=game)
        review = get_object_or_404(queryset, slug=review)
        #reviews = game.review_set.filter(status=1).order_by('-created_on') # Get all reviews related to the game
        comments = review.comments.filter(approved=True).order_by('created_on') # in walktrough: comments.filter(approved=True).order_by
        liked = False
        if review.likes.filter(id=self.request.user.id).exists():
            liked = True
        #if review.likes.filter(id=self.request.user.id).exists():
        #    liked = True

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
    
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('review_detail', game = comment.review.game.slug, review=comment.review.slug,)
    else:
        form = CommentForm(instance=comment)

    return render(request, 'edit_comment.html', {'form': form, 'comment': comment})

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    # Überprüfen, ob der Benutzer ein Administrator ist oder der Autor des Kommentars
    if request.user.is_superuser or request.user == comment.name:
        if request.method == 'POST':
            # Löschlogik hier einfügen
            comment.delete()
            return redirect('review_detail', game = comment.review.game.slug, review=comment.review.slug,)
        return render(request, 'delete_comment.html', {'comment': comment})
    else:
        # Hier können Sie eine Weiterleitung oder eine Fehlermeldung hinzufügen
        return redirect('review_detail', review_id=comment.review.id)