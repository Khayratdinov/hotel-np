from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import  Paginator


from room.models import CommentForm, Comment, Room, RoomServices, Room_Image, Order
from blog.models import Blog
from home.forms import OrderForm






# ---------------------------------------------------------------------------- #
#                                   ROOM PAGE                                  #
# ---------------------------------------------------------------------------- #


def rooms(request):
    
    rooms = Room.objects.all()
    paginator = Paginator(rooms, 1)
    page = request.GET.get('page')
    paged_rooms = paginator.get_page(page)
    room_services = RoomServices.objects.all()
    comments = Comment.objects.all()

    context = {
        'rooms': paged_rooms,
        'room_services': room_services,
        'comments': comments,
    }

    return render(request, 'room/rooms.html', context)


def room_detail(request, room_id):
    room_page = Room.objects.get(pk=room_id)
    images = Room_Image.objects.filter(room_id=room_id)
    room_services = RoomServices.objects.filter(room_id=room_id)
    services = RoomServices.objects.all()
    blogs = Blog.objects.all().order_by('?')[:4]
    room_picked = Room.objects.all().order_by('?')[:3]
    comments = Comment.objects.filter(room_id=room_id, status='True')
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.name = form.cleaned_data['name']
            data.surname = form.cleaned_data['surname']
            data.phone = form.cleaned_data['phone']
            data.citizenship = form.cleaned_data['citizenship']
            data.pay = form.cleaned_data['pay']
            data.email = form.cleaned_data['email']
            data.guest = form.cleaned_data['guest']
            data.arrival = form.cleaned_data['arrival']
            data.departure = form.cleaned_data['departure']
            data.room = form.cleaned_data['room']
            data.category = form.cleaned_data['category']
            data.select = form.cleaned_data['select']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Siz xonani bro'n qildiz aperato'r siz bilan bog'lanadi")
            return HttpResponseRedirect(url)
        return HttpResponseRedirect(url)
    form = OrderForm
    
    
    
    context = {
        'room_page': room_page,
        'images': images,
        'room_services' : room_services,
        'blogs' : blogs,
        'room_picked': room_picked,
        'comments': comments,
        'form':form,
        'services':services,

        
    }
    return render(request, 'room/room_detail.html', context)


def addcomment(request,room_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.room_id = room_id
            current_user= request.user
            data.user_id = current_user.id
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Sizning kommentariyangiz qabul qilindi!")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)



# ---------------------------------------------------------------------------- #