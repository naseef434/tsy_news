from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . models import registration,news_field,advetiment_field,adv_position,news_place,\
    news_nation,news_district,aboutus_content,aboutus,special_days
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib import messages
import datetime
import re


# Create your views here.
def reg(request):
    return render(request,'registration.html')

def signup(request):
    first_name = request.POST['fname']
    last_name = request.POST['lname']

    phone_regex = '[6-9]{1}[0-9]{9}'
    phone = request.POST['phone']
    if (re.search(phone_regex, phone)) is None:
        messages.success(request, 'Invalid Phone Number Pattern...!\nFirst digit 6-9')
        return render(request, 'registration.html')

    email_regex = '[a-z0-9._%+-]{3,}@[a-z]{3,}([.]{1}[a-z]{2,}|[.]{1}[a-z]{2,}[.]{1}[a-z]{2,})'
    email = request.POST['email']
    if (re.search(email_regex, email)) is None:
        messages.success(request, 'Invalid Email Pattern...!\nexample@mail.com')
        return render(request, 'registration.html')

    password = request.POST['password']
    c_password = request.POST['cpassword']

    # image = request.FILES['image']
    # fs = FileSystemStorage()
    # fs.save(image.name, image)

    if password == c_password:
        user = User.objects.create_user(username=email, password=password, first_name=first_name, last_name=last_name, email=email)
        user.save()
        reg = registration(id=user, phone=phone, user_type="pending")
        reg.save()
        messages.success(request, 'Registration Successfully Completed, Contact Your Admin...')
        return render(request, 'login.html')

    else:
        return '''
                        <script>
                            alert('Password not matching...!!!')
                        </script>

            '''
        return redirect('/writer/registration/')

def login(request):
    return render(request,'login.html')

def signin(request):
    if request.method == 'GET':
        messages.success(request, 'Login Timeout, Please Login...')
        return render(request, 'login.html')


    username = request.POST['u_name']
    passwrd = request.POST['password']


    user = authenticate(request, username=username, password=passwrd)
    if user is None:
        messages.success(request, 'You are not in Records Please Register First...!')
        return render(request, 'registration.html')
    else:
        user_type = registration.objects.get(id=user)
        if (user_type.user_type == "editor"):
            request.session['id'] = user.pk
            user = User.objects.get(pk=request.session['id'])

            n_district = news_district.objects.all()
            n_nation = news_nation.objects.all()
            n_palce = news_place.objects.all()


            news = {
                'editor': user,
                'n_district': n_district,
                'n_place' : n_palce,
                'n_nation': n_nation,
                'usertype' : user_type,
            }
            return render(request, 'admin_page.html', news)

        elif (user_type.user_type == "admin"):
            request.session['id'] = user.pk

            user = User.objects.get(pk=request.session['id'])

            n_district = news_district.objects.all()
            n_nation = news_nation.objects.all()
            n_palce = news_place.objects.all()


            news = {
                'editor': user,
                'n_district': n_district,
                'n_place' : n_palce,
                'n_nation': n_nation,
                'usertype': user_type,
            }
            return render(request, 'admin_page.html', news)
        else:
            if (user_type.user_type == "pending"):
                messages.success(request, 'Your Membership is not Accepted Contact Your Admin...!')
                return redirect('/writer/')

def edit_corner(request):
    user = User.objects.get(pk=request.session['id'])
    user_type = registration.objects.get(id=user)

    if user is None:
        messages.success(request, 'Login Timeout, Please Login...')
        return render(request, 'login.html')
    else:
        n_district = news_district.objects.all()
        n_nation = news_nation.objects.all()
        n_palce = news_place.objects.all()

        news = {
            'editor': user,
            'n_district': n_district,
            'n_place': n_palce,
            'n_nation': n_nation,
            'usertype': user_type,
        }

        return render(request,'admin_page.html',news)

def post_news(request):
    editor = User.objects.get(pk=request.session['id'])

    if editor is None:
        messages.success(request, 'Login Timeout, Please Login...')
        return render(request, 'login.html')
    else:
        x = datetime.datetime.now()
        headding = request.POST['n_head']
        content = request.POST['n_content']
        region = request.POST['region']
        y_link = request.POST['y_link_radio']

        if (region == '1'):
            district = request.POST['district']
        else:
            district = request.POST['d_district']

        if (district == '11'):
            place = request.POST['place']
        else:
            place = request.POST['d_place']

        if (y_link == 'No'):
            image = request.FILES['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)

            video ='NULL'
        else:
            image = 'NULL'
            video = request.POST['y_id']



        main_news = request.POST['main_news']

        breaking_news = request.POST['breaking_news']

        news = news_field(editor_id_id=editor.pk, published_date=x, news_title=headding, news_content=content,
                          news_nation_id=region,
                          news_district_id=district, news_place_id=place, news_image=image,video_link=video, main_news=main_news,
                          breaking_news=breaking_news)
        news.save()
        return redirect('/writer/edit_corner/')

def adv_page(request):
        user = User.objects.get(pk=request.session['id'])
        user_type = registration.objects.get(id=user)
        ad_position = adv_position.objects.all()

        if user is None:
            messages.success(request, 'Login Timeout, Please Login...')
            return render(request, 'login.html')
        else:
            u_type = {
                'usertype': user_type,
                'ad_position': ad_position,
            }
            return render(request, 'advetisement.html', u_type)

def ad_post(request):
    user = User.objects.get(pk=request.session['id'])

    if user is None:
        messages.success(request, 'Login Timeout, Please Login...')
        return render(request, 'login.html')
    else:
        d = datetime.datetime.now()
        head = request.POST['headding']
        position = request.POST['ad_position']
        img = request.FILES['image']
        fs = FileSystemStorage()
        fs.save(img.name, img)

        adv = advetiment_field(user_id_id=user.pk, date_of_publish=d, adv_content=head,ad_position_id=position,adv_images=img)
        adv.save()
        return redirect('/writer/adv_page/')

def ad_remove(request,id):
    user = User.objects.get(pk=request.session['id'])

    if user is None:
        messages.success(request, 'Login Timeout, Please Login...')
        return render(request, 'login.html')
    else:
        d_ad = advetiment_field.objects.get(pk=id)
        d_ad.delete()

        return redirect('/writer/ad_view/')

def view_adv(request):
    user = User.objects.get(pk=request.session['id'])
    user_type = registration.objects.get(id=user)
    adv = advetiment_field.objects.order_by('-id')

    if user is None:
        messages.success(request, 'Login Timeout, Please Login...')
        return render(request, 'login.html')
    else:

        advs ={
            'usertype': user_type,
            'ads' : adv,
        }
        return render(request, 'ad_view.html',advs)

def my_record(request):
    user = User.objects.get(pk=request.session['id'])
    user_type = registration.objects.get(id=user)

    if user is None:
        messages.success(request, 'Login Timeout, Please Login...')
        return render(request, 'login.html')
    else:
        date = datetime.date.today()
        day = datetime.date.today().weekday()
        days = ['തിങ്കള്‍', 'ചൊവ്വ', 'ബുധന്‍', 'വ്യാഴം', 'വെള്ളി', 'ശനി', 'ഞായര്‍']
        user = User.objects.get(pk=request.session['id'])
        data = news_field.objects.filter(editor_id=user.pk).order_by('-id')
        nation = news_nation.objects.all()

        page = request.GET.get('page', 1)
        paginator = Paginator(data, 20)
        try:
            m_r_paginator = paginator.page(page)
        except PageNotAnInteger:
            m_r_paginator = paginator.page(1)
        except EmptyPage:
            m_r_paginator = paginator.page(paginator.num_pages)


        record = {
            # 'records': data,
            'records': m_r_paginator,
            'nation': nation,
            'date': date,
            'day': days[day],
            'usertype': user_type,
        }

        return render(request, 'my_records.html', record)

def all_members(request):
    user = User.objects.get(pk=request.session['id'])
    user_type = registration.objects.get(id=user)

    if user is None:
        messages.success(request, 'Login Timeout, Please Login...')
        return render(request, 'login.html')
    else:
        users = User.objects.all().exclude(registration__user_type="pending")
        reg = registration.objects.all()
        members = {
            'users': users,
            'reg': reg,

            'usertype': user_type,
        }

        return render(request, 'all_members.html', members)

def update_u_type(request,id):
    type = request.POST['user_type']
    registration.objects.filter(pk=id).update(user_type=type)
    return redirect('/writer/all_members/')

def pending_members(request):
    user = User.objects.get(pk=request.session['id'])
    user_type = registration.objects.get(id=user)

    if user is None:
        messages.success(request, 'Login Timeout, Please Login...')
        return render(request, 'login.html')
    else:
        users = User.objects.filter(registration__user_type='pending')
        reg = registration.objects.filter(user_type='pending')

        p_members = {
            'user': users,
            'reg': reg,
            'usertype': user_type,
        }

        return render(request, 'pending editors.html', p_members)

def editabout(request):
    user = User.objects.get(pk=request.session['id'])
    user_type = registration.objects.get(id=user)
    contents = aboutus_content.objects.order_by('-id')[:1]
    user_details = aboutus.objects.all()

    context = {
        'content' : contents,
        'about_details' : user_details,
        'usertype': user_type,
    }
    return render(request,'Edit_About.html',context)

def add_user_about(request):
    user = User.objects.get(pk=request.session['id'])

    if user is None:
        messages.success(request, 'Login Timeout, Please Login...')
        return render(request, 'login.html')
    else:
        u_name = request.POST['users_name']

        img = request.FILES['image']
        fs = FileSystemStorage()
        fs.save(img.name, img)

        add = aboutus(editor_id=user,user_image=img,user_name=u_name)
        add.save()

        return redirect('/writer/edit_about/')

def delete_about_editors(request,id):
    d_editors = aboutus.objects.get(pk=id)
    d_editors.delete()
    return redirect('/writer/edit_about/')

def add_about_content(request):
    user = User.objects.get(pk=request.session['id'])
    if user is None:
        messages.success(request, 'Login Timeout, Please Login...')
        return render(request, 'login.html')
    else:
        content = request.POST['content']

        add_content = aboutus_content(contant=content,editor_id=user)
        add_content.save()
    return redirect('/writer/edit_about/')

def spl_img_page(request):
    user = User.objects.get(pk=request.session['id'])
    user_type = registration.objects.get(id=user)
    spl_img = special_days.objects.order_by('-id')

    context = {
        'spl' :spl_img,
        'usertype': user_type,
    }
    return render(request,'special_wishes.html',context)

def upload_spl_img(request):
    user = User.objects.get(pk=request.session['id'])
    if user is None:
        messages.success(request, 'Login Timeout, Please Login...')
        return render(request, 'login.html')
    else:

        x = datetime.datetime.now()
        wish_name = request.POST['w_name']

        img = request.FILES['image']
        fs = FileSystemStorage()
        fs.save(img.name, img)

        spl_post = special_days(editor_id=user,whish_head=wish_name,wishing_image=img,date_of_publish=x)
        spl_post.save()
        return redirect('/writer/spl_img/')

def spl_img_delete(request,id):
    user = User.objects.get(pk=request.session['id'])
    if user is None:
        messages.success(request, 'Login Timeout, Please Login...')
        return render(request, 'login.html')
    else:
        d_spl_img = special_days.objects.get(pk=id)
        d_spl_img.delete()
        return redirect('/writer/spl_img/')

def delete_about_content(request,id):
    d_contents = aboutus_content.objects.get(pk=id)
    d_contents.delete()
    return redirect('/writer/edit_about/')

def u_approve(request,id):
    user = User.objects.get(pk=request.session['id'])
    if user is None:
        messages.success(request, 'Login Timeout, Please Login...')
        return render(request, 'login.html')
    else:
        type = request.POST['user_type']

        registration.objects.filter(pk=id).update(user_type=type)
        return redirect('/writer/pending_members/')

def all_reject(request,id):
    user = User.objects.get(pk=request.session['id'])
    if user is None:
        messages.success(request, 'Login Timeout, Please Login...')
        return render(request, 'login.html')
    else:
        u_d = User.objects.get(pk=id)
        u_d.delete()
        return redirect('/writer/all_members/')

def u_reject(request,id):
    user = User.objects.get(pk=request.session['id'])
    if user is None:
        messages.success(request, 'Login Timeout, Please Login...')
        return render(request, 'login.html')
    else:
        u_d = User.objects.get(pk=id)
        u_d.delete()
        return redirect('/writer/pending_members/')

def n_reject(request,id):
    user = User.objects.get(pk=request.session['id'])
    if user is None:
        messages.success(request, 'Login Timeout, Please Login...')
        return render(request, 'login.html')
    else:
        n_d = news_field.objects.get(pk=id)
        n_d.delete()
        return redirect('/writer/my_record/')

def news_update(request,id):
    user = User.objects.get(pk=request.session['id'])
    user_type = registration.objects.get(id=user)
    if user is None:
        messages.success(request, 'Login Timeout, Please Login...')
        return render(request, 'login.html')
    else:
        n_d = news_field.objects.get(pk=id)

        id_news = {
            'usertype': user_type,
            'news': n_d,
        }

        return render(request, 'update_news.html', id_news)

def news_head_update(request,id):
    user = User.objects.get(pk=request.session['id'])
    if user is None:
        messages.success(request, 'Login Timeout, Please Login...')
        return render(request, 'login.html')
    else:
        n_d = news_field.objects.get(pk=id)
        n_d_id = str(n_d.pk)

        headding = request.POST['n_head']

        news_field.objects.filter(pk=n_d_id).update(news_title=headding)

        return redirect('/writer/update_news/'+ n_d_id + '/')

def news_content_update(request,id):
    user = User.objects.get(pk=request.session['id'])
    if user is None:
        messages.success(request, 'Login Timeout, Please Login...')
        return render(request, 'login.html')
    else:
        n_d = news_field.objects.get(pk=id)
        n_d_id = str(n_d.pk)

        content = request.POST['n_content']

        news_field.objects.filter(pk=n_d_id).update(news_content=content)

        return redirect('/writer/update_news/'+ n_d_id +'/')

def logout_view(request):
    logout(request)
    return redirect('/writer/')
