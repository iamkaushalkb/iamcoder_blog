# django modules
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from home.models import Contact
from blog.models import Post

# Create your views here.
def home(request):
    allPosts= Post.objects.all()
    data = { 'allPosts' : allPosts,}
    return render(request, 'home/home.html', data)

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    # handeling POST requesting
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        msg = request.POST['msg']
        # adding data into backend
        contact = Contact(name=name, email=email, address=address, msg=msg)
        contact.save()
        # flashing success message
        messages.success(request, 'Message Send Sucessfully')
    return render(request, 'home/contact.html')

def search(request):
    query = request.GET['query']
    # not showing results for long keywords
    if len(query) > 40:
        allPosts = Post.objects.none()
    # showing results for searched keywords
    else:
        allPostsTitle = Post.objects.filter(title__icontains = query)
        allPostsContent = Post.objects.filter(content__icontains = query)
        allPostsAuthor = Post.objects.filter(author__icontains = query)
        allPosts = allPostsTitle|allPostsAuthor|allPostsContent
    # if search is blank
    if allPosts.count() == 0:
        messages.error(request, 'No result Found')
    params = { 'allPosts' : allPosts, 'query' : query}
    return render(request, 'home/search.html', params)

def signup(request):
    # handeling POST requesting
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # Validation Checking
        if len(username) > 10 :
            # flashing error message
            messages.error(request, 'Username must be  More than 1 and less than 10 characters')  
            return redirect('home')
        if len(username) < 1 :
            # flashing error message
            messages.error(request, 'Username must be  More than 1 and less than 10 characters')  
            return redirect('home')
        if password != password2 :
            # flashing error message
            messages.error(request, 'Passwords must be matched')  
            return redirect('home')
        # Creating User
        myuser = User.objects.create_user(username,email,password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        return redirect('home')
        # flashing success message
        messages.success(request, 'User Created Sucessfully')
        messages.success(request, 'To get access function if iamcoder please signin')
    else:
        return HttpResponse('404 - Not Found')
    
def signin(request):
    # handeling POST requesting
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        # authenticating user
        user = authenticate(username = loginusername, password= loginpassword)
        # if user is matched then giving accesss
        if user is not None:
            login(request,user)
            messages.success(request, 'Loggedin Sucessfully')
            return redirect('home')
        # if user is not matched then acced denied 
        else:
            messages.error(request, 'Invalid Information')
            return redirect('home')
    return HttpResponse('404 - Not Found')

def signout(request):
    logout(request)
    messages.success(request, 'Loggedout Sucessfully')
    return redirect('home')