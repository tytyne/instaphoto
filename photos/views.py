

from django.contrib.auth.decorators import login_required
import datetime as dt
from django.shortcuts import render
from .models import Image
from django.http import HttpResponse,Http404,HttpResponseRedirect
from . forms import PhotosLetterForm,PhotoImageForm
from .models import PhotosLetterRecipients
from .email import send_welcome_email
from django.shortcuts import redirect


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def welcome(request):
    return HttpResponse('Welcome to the Moringa Tribune')
# def photos_of_day(request):
#     date = dt.date.today()
#     html = f'''
#         <html>
#             <body>
#                 <h1> {date.day}-{date.month}-{date.year}</h1>
#             </body>
#         </html>
#             '''
#     # return HttpResponse(html)
#     return render(request, 'all-photos/today-photos.html', {"date": date,})

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day
# def past_days_photos(request,past_date):
#     try:
#         # Converts data from the string Url
#         date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

#     except ValueError:
#         # Raise 404 error when ValueError is thrown
#         raise Http404()
#     day = convert_dates(date)
#     html = f'''
#         <html>
#             <body>
#                 <h1>photos for {day} {date.day}-{date.month}-{date.year}</h1>
#             </body>
#         </html>
#             '''
#     return HttpResponse(html)    
def photos_today(request):
    date = dt.date.today()
    form = PhotosLetterForm()
    photos=Image.todays_photos()
    print(photos)
    if request.method == 'POST':
        form = PhotosLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = PhotosLetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('photos_today')
    else:
        form = PhotosLetterForm()
    return render(request, 'all-photos/index.html', {"date": date,"OK":photos,"letterForm":form})


    
def past_days_photos(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(photos_today)

    photos = Image.days_photos(date)
    return render(request, 'all-photos/past-photos.html',{"date": date,"photos":photos})    
def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-photos/search.html',{"message":message}) 

@login_required(login_url='/accounts/login/')
def image(request, image_id):      

    try:
        image = image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/index.html", {"image":image})        
@login_required(login_url='/accounts/login/')
def photo_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = PhotoImageForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('photosToday')

    else:
        form = PhotoImageForm()
    return render(request, 'photo_image.html', {"form": form})   
@login_required(login_url='/accounts/login/')
def upload_profile(request):
    current_user = request.user 
    title = 'Upload Profile'
    try:
        requested_profile = Profile.objects.get(user_id = current_user.id)
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)

            if form.is_valid():
                requested_profile.profile_pic = form.cleaned_data['profile_pic']
                requested_profile.bio = form.cleaned_data['bio']
                requested_profile.username = form.cleaned_data['username']
                requested_profile.save_profile()
                return redirect( profile )
        else:
            form = ProfileUploadForm()
    except:
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)

            if form.is_valid():
                new_profile = Profile(profile_pic = form.cleaned_data['profile_pic'],bio = form.cleaned_data['bio'],username = form.cleaned_data['username'])
                new_profile.save_profile()
                return redirect( profile )
        else:
            form = ProfileUploadForm() 