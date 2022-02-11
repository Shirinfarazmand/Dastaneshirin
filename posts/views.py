from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .forms import Contact
from .forms import CommentForm
from django.core.mail import send_mail, BadHeaderError

# The function to see posts in the main page
def index(request):
    posts = Post.objects.all()
    return render(request,'index.html',{'posts': posts} )


# With this function we can read each post separately
def post(request, pk ):
    posts= Post.objects.get(id=pk)
    return render(request, 'posts.html',{'posts':posts })

# def post_detail(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     comments = post.comments.filter(active=True)
#     new_comment = None
#     # Comment posted
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():

#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.post = post
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()

#     return render(request, 'posts.html', {'post': post,'comments': comments,'new_comment': new_comment, 'comment_form': comment_form})



# registration
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password2 == password:
            if User.objects.filter(email = email).exists():
                messages.info(request,"The email already exists!")
                return redirect('register')
            elif User.objects.filter(username = username).exists():
                messages.info(request,"The username already exists!")   
                return redirect('register')
            else:
                user= User.objects.create_user(username = username , email = email , password = password)
                user.save
                return redirect('login')
        else:
            messages.info(request, "The repeated password is incorrect!")
            return redirect('register')
    
    else:
        return render (request, 'register.html')


# Login function
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST["password"]
        user = auth.authenticate(username= username,password= password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Username and password do not match!")
            return redirect('login') 
    else:
        return render(request, 'login.html')


# Log out function
def logout(request):
    auth.logout(request)
    return redirect("/")


# About the website
def about(request):
    return render(request, 'about.html')


# The user can send an email with this function
def contact(request):
    if request.method =='POST':
        form= Contact(request.POST)
        if form.is_valid():
            subject = "Dastane Shirin" 
        body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
        message = "\n".join(body.values()) 
            
        try:
            send_mail(subject, message, 'shirini6666@gmail.com', ['shirini6666@gmail.com']) 
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect ("index")

    form = Contact()
    return render(request, "contact.html", {'form':form})


