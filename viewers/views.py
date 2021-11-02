from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from  editors.models import registration,news_field,advetiment_field,news_place,news_nation,aboutus,aboutus_content,special_days
from django.contrib.auth.models import User
from datetime import date,datetime

# Create your views here.
def index(request):

    icon = "icon.png"
    temp_img = "tsytemp.jpg"
    news = news_field.objects.order_by('-id')[:14]
    gulf = news_field.objects.filter(news_nation_id=2).order_by('-id')[:10]
    # main_a = news_field.objects.filter(main_news=2).latest('id')
    main_b = news_field.objects.filter(main_news=2).exclude(pk=main_a.pk).order_by('-id')[:2]
    local_tsy = news_field.objects.filter(news_place_id=1).latest('id')
    local_tsy_tbl = news_field.objects.filter(news_place_id=1).exclude(pk=local_tsy.pk).order_by('-id')[:5]
    local_kdly = news_field.objects.filter(news_place_id=2).latest('id')
    local_kdly_tbl = news_field.objects.filter(news_place_id=2).exclude(pk=local_kdly.pk).order_by('-id')[:5]
    local_trvpdi = news_field.objects.filter(news_place_id=5).latest('id')
    local_trvpdi_tbl = news_field.objects.filter(news_place_id=5).exclude(pk=local_trvpdi.pk).order_by('-id')[:5]
    breaking_news = news_field.objects.filter(published_date__gte=date.today(),breaking_news=2).order_by('-id')[:2]


    ad_view_top_full = advetiment_field.objects.filter(ad_position_id=1).order_by('-id')[:1]
    ad_view_top_small = advetiment_field.objects.filter(ad_position_id=2).order_by('-id')[:1]
    ad_view_aftrmain = advetiment_field.objects.order_by('-id')[:2]
    ad_view_aftr_glfnws = advetiment_field.objects.order_by('-id')[3:5]
    ad_view_aftr_ltstns = advetiment_field.objects.filter(ad_position=(1,2)).order_by('-id')[1:2]
    ad_view_in_tsyns = advetiment_field.objects.order_by('-id')[6:7]
    ad_view_in_kdvlyns = advetiment_field.objects.order_by('-id')[8:10]
    ad_view_in_trvmpdy = advetiment_field.objects.order_by('-id')[10:11]
    ad_view_aftr_lclnws = advetiment_field.objects.filter(ad_position=(1,2)).order_by('-id')[1:2]
    adv_view_side = advetiment_field.objects.filter(ad_position_id=3).order_by('-id')

    wish_details = special_days.objects.order_by('-id')[:1]


    all_news = {
        "t_img" : temp_img,
        "icon_img" : icon,
        'latest_news' : news,
        'gulf_news': gulf,
        'main_news_a' : main_a,
        'main_news_b' : main_b,
        'local_tsy_main' : local_tsy,
        'local_tsy_tbl'  : local_tsy_tbl,
        'local_kdly_main': local_kdly,
        'local_kdly_tbl': local_kdly_tbl,
        'local_trvpdi_main': local_trvpdi,
        'local_trvpdi_tbl': local_trvpdi_tbl,
        'breaking' : breaking_news,

        'adv_top_full' : ad_view_top_full,
        'adv_top_small': ad_view_top_small,
        'adv_aftrmain' : ad_view_aftrmain,
        'adv_aftrglf' : ad_view_aftr_glfnws,
        'adv_aftrltst' : ad_view_aftr_ltstns,
        'adv_intsyns' : ad_view_in_tsyns,
        'adv_inkdvly' : ad_view_in_kdvlyns,
        'adv_intrvmpdy' : ad_view_in_trvmpdy,
        'adv_aftr_lclnws' :ad_view_aftr_lclnws,
        'adv_side' : adv_view_side,

        'wish' : wish_details,
    }


    return render(request,'index.html',all_news)



def latest(request):
    n_latest = news_field.objects.order_by('-id')[:150]
    inter = news_field.objects.filter(news_nation_id=3).order_by('-id')[:1]
    n_kerala = news_field.objects.filter(news_nation_id=1).order_by('-id')[:1]
    n_gulf = news_field.objects.filter(news_nation_id=2).order_by('-id')[:1]
    n_local = news_field.objects.filter(news_district_id=11).order_by('-id')[:1]
    n_sports = news_field.objects.filter(news_nation_id=5).order_by('-id')[:1]
    n_more = news_field.objects.filter(news_nation_id=6).order_by('-id')[:1]


    image = news_nation.objects.filter(pk='4')

    adv_view_carousel_active = advetiment_field.objects.filter(ad_position_id=(1,2)).order_by('-id')[:1]
    adv_view_carousel = advetiment_field.objects.filter(ad_position_id=(1,2)).exclude(id=adv_view_carousel_active).order_by('-id')
    adv_view_small_active = advetiment_field.objects.filter(ad_position_id=(1,2)).order_by('-id')[:1]
    adv_view_small = advetiment_field.objects.filter(ad_position_id=(1,2)).exclude(id=adv_view_small_active).order_by('-id')
    adv_view_side = advetiment_field.objects.filter(ad_position_id=3).order_by('-id')[:5]

    page = request.GET.get('page', 1)
    paginator = Paginator(n_latest, 20)
    try:
        n_l_paginator = paginator.page(page)
    except PageNotAnInteger:
        n_l_paginator = paginator.page(1)
    except EmptyPage:
        n_l_paginator = paginator.page(paginator.num_pages)

    t_news ={
        # 'news': n_latest,
        'internation' : inter,
        'kerala_n' : n_kerala,
        'gulf_n' : n_gulf,
        'local_n' : n_local,
        'sports_n' : n_sports,
        'more_n' : n_more,

        'n_l_p' : n_l_paginator,

        'adv_carousel_active' : adv_view_carousel_active,
        'adv_carousel' : adv_view_carousel,
        'adv_small_active' : adv_view_small_active,
        'adv_small' : adv_view_small,
        'adv_side' : adv_view_side,
        'logo_img': image,
    }
    return render(request,'news_types.html',t_news)



def gulf(request):
    gulf = news_field.objects.filter(news_nation_id=2).order_by('-id')[:150]
    inter = news_field.objects.filter(news_nation_id=3).order_by('-id')[:1]
    n_kerala = news_field.objects.filter(news_nation_id=1).order_by('-id')[:1]
    n_gulf = news_field.objects.filter(news_nation_id=2).order_by('-id')[:1]
    n_local = news_field.objects.filter(news_district_id=11).order_by('-id')[:1]
    n_sports = news_field.objects.filter(news_nation_id=5).order_by('-id')[:1]
    n_more = news_field.objects.filter(news_nation_id=6).order_by('-id')[:1]

    image = news_nation.objects.filter(pk='2')

    adv_view_carousel_active = advetiment_field.objects.filter(ad_position_id=(1,2)).order_by('-id')[:1]
    adv_view_carousel = advetiment_field.objects.filter(ad_position_id=(1,2)).exclude(id=adv_view_carousel_active).order_by('-id')
    adv_view_small_active = advetiment_field.objects.filter(ad_position_id=(1,2)).order_by('-id')[:1]
    adv_view_small = advetiment_field.objects.filter(ad_position_id=(1,2)).exclude(id=adv_view_small_active).order_by('-id')
    adv_view_side = advetiment_field.objects.filter(ad_position_id=3).order_by('-id')[:5]

    page = request.GET.get('page', 1)
    paginator = Paginator(gulf, 20)
    try:
        n_l_paginator = paginator.page(page)
    except PageNotAnInteger:
        n_l_paginator = paginator.page(1)
    except EmptyPage:
        n_l_paginator = paginator.page(paginator.num_pages)

    t_news ={
        # 'news': gulf,
        'internation': inter,
        'kerala_n': n_kerala,
        'gulf_n': n_gulf,
        'local_n': n_local,
        'sports_n': n_sports,
        'more_n': n_more,

        'n_l_p': n_l_paginator,

        'adv_carousel_active' : adv_view_carousel_active,
        'adv_carousel' : adv_view_carousel,
        'adv_small_active' : adv_view_small_active,
        'adv_small' : adv_view_small,
        'adv_side' : adv_view_side,
        'logo_img': image,
    }
    return render(request,'news_types.html',t_news)



def internation(request):
    inter = news_field.objects.filter(news_nation_id=3).order_by('-id')[:150]
    m_inter = news_field.objects.filter(news_nation_id=3).order_by('-id')[:1]
    n_kerala = news_field.objects.filter(news_nation_id=1).order_by('-id')[:1]
    n_gulf = news_field.objects.filter(news_nation_id=2).order_by('-id')[:1]
    n_local = news_field.objects.filter(news_district_id=11).order_by('-id')[:1]
    n_sports = news_field.objects.filter(news_nation_id=5).order_by('-id')[:1]
    n_more = news_field.objects.filter(news_nation_id=6).order_by('-id')[:1]

    adv_view_carousel_active = advetiment_field.objects.filter(ad_position_id=(1,2)).order_by('-id')[:1]
    adv_view_carousel = advetiment_field.objects.filter(ad_position_id=(1,2)).exclude(id=adv_view_carousel_active).order_by('-id')
    adv_view_small_active = advetiment_field.objects.filter(ad_position_id=(1,2)).order_by('-id')[:1]
    adv_view_small = advetiment_field.objects.filter(ad_position_id=(1,2)).exclude(id=adv_view_small_active).order_by('-id')
    adv_view_side = advetiment_field.objects.filter(ad_position_id=3).order_by('-id')[:5]

    image = news_nation.objects.filter(pk='3')

    page = request.GET.get('page', 1)
    paginator = Paginator(inter, 20)
    try:
        n_l_paginator = paginator.page(page)
    except PageNotAnInteger:
        n_l_paginator = paginator.page(1)
    except EmptyPage:
        n_l_paginator = paginator.page(paginator.num_pages)

    inter_news ={
        # 'news': inter,
        'internation': m_inter,
        'kerala_n': n_kerala,
        'gulf_n': n_gulf,
        'local_n': n_local,
        'sports_n': n_sports,
        'more_n': n_more,

        'n_l_p': n_l_paginator,


        'adv_carousel_active' : adv_view_carousel_active,
        'adv_carousel' : adv_view_carousel,
        'adv_small_active' : adv_view_small_active,
        'adv_small' : adv_view_small,
        'adv_side' : adv_view_side,
        'logo_img': image,
    }
    return render(request,'news_types.html',inter_news)



def kerala(request):
    kerala = news_field.objects.filter(news_nation_id=1).order_by('-id')[:150]
    inter = news_field.objects.filter(news_nation_id=3).order_by('-id')[:1]
    n_kerala = news_field.objects.filter(news_nation_id=1).order_by('-id')[:1]
    n_gulf = news_field.objects.filter(news_nation_id=2).order_by('-id')[:1]
    n_local = news_field.objects.filter(news_district_id=11).order_by('-id')[:1]
    n_sports = news_field.objects.filter(news_nation_id=5).order_by('-id')[:1]
    n_more = news_field.objects.filter(news_nation_id=6).order_by('-id')[:1]

    adv_view_carousel_active = advetiment_field.objects.filter(ad_position_id=(1,2)).order_by('-id')[:1]
    adv_view_carousel = advetiment_field.objects.filter(ad_position_id=(1,2)).exclude(id=adv_view_carousel_active).order_by('-id')
    adv_view_small_active = advetiment_field.objects.filter(ad_position_id=(1,2)).order_by('-id')[:1]
    adv_view_small = advetiment_field.objects.filter(ad_position_id=(1,2)).exclude(id=adv_view_small_active).order_by('-id')
    adv_view_side = advetiment_field.objects.filter(ad_position_id=3).order_by('-id')[:5]

    image = news_nation.objects.filter(pk='1')

    page = request.GET.get('page', 1)
    paginator = Paginator(kerala, 20)
    try:
        n_l_paginator = paginator.page(page)
    except PageNotAnInteger:
        n_l_paginator = paginator.page(1)
    except EmptyPage:
        n_l_paginator = paginator.page(paginator.num_pages)

    k_news ={
        'news': kerala,
        'internation': inter,
        'kerala_n': n_kerala,
        'gulf_n': n_gulf,
        'local_n': n_local,
        'sports_n': n_sports,
        'more_n': n_more,

        'n_l_p': n_l_paginator,


        'adv_carousel_active' : adv_view_carousel_active,
        'adv_carousel' : adv_view_carousel,
        'adv_small_active' : adv_view_small_active,
        'adv_small' : adv_view_small,
        'adv_side' : adv_view_side,
        'logo_img': image,
    }
    return render(request,'news_types.html',k_news)

def sports(request):
    sports = news_field.objects.filter(news_nation_id=5).order_by('-id')[:150]
    inter = news_field.objects.filter(news_nation_id=3).order_by('-id')[:1]
    n_kerala = news_field.objects.filter(news_nation_id=1).order_by('-id')[:1]
    n_gulf = news_field.objects.filter(news_nation_id=2).order_by('-id')[:1]
    n_local = news_field.objects.filter(news_district_id=11).order_by('-id')[:1]
    n_sports = news_field.objects.filter(news_nation_id=5).order_by('-id')[:1]
    n_more = news_field.objects.filter(news_nation_id=6).order_by('-id')[:1]

    adv_view_carousel_active = advetiment_field.objects.filter(ad_position_id=(1,2)).order_by('-id')[:1]
    adv_view_carousel = advetiment_field.objects.filter(ad_position_id=(1,2)).exclude(id=adv_view_carousel_active).order_by('-id')
    adv_view_small_active = advetiment_field.objects.filter(ad_position_id=(1,2)).order_by('-id')[:1]
    adv_view_small = advetiment_field.objects.filter(ad_position_id=(1,2)).exclude(id=adv_view_small_active).order_by('-id')
    adv_view_side = advetiment_field.objects.filter(ad_position_id=3).order_by('-id')[:5]

    image = news_nation.objects.filter(pk='5')

    page = request.GET.get('page', 1)
    paginator = Paginator(sports, 20)
    try:
        n_l_paginator = paginator.page(page)
    except PageNotAnInteger:
        n_l_paginator = paginator.page(1)
    except EmptyPage:
        n_l_paginator = paginator.page(paginator.num_pages)

    s_news = {
        'news': sports,
        'internation': inter,
        'kerala_n': n_kerala,
        'gulf_n': n_gulf,
        'local_n': n_local,
        'sports_n': n_sports,
        'more_n': n_more,

        'n_l_p': n_l_paginator,

        'adv_carousel_active' : adv_view_carousel_active,
        'adv_carousel' : adv_view_carousel,
        'adv_small_active' : adv_view_small_active,
        'adv_small' : adv_view_small,
        'adv_side': adv_view_side,
        'logo_img': image,
    }

    return render(request, 'news_types.html', s_news)


def more(request):
    more = news_field.objects.filter(news_nation_id=6).order_by('-id')[:150]
    inter = news_field.objects.filter(news_nation_id=3).order_by('-id')[:1]
    n_kerala = news_field.objects.filter(news_nation_id=1).order_by('-id')[:1]
    n_gulf = news_field.objects.filter(news_nation_id=2).order_by('-id')[:1]
    n_local = news_field.objects.filter(news_district_id=11).order_by('-id')[:1]
    n_sports = news_field.objects.filter(news_nation_id=5).order_by('-id')[:1]
    n_more = news_field.objects.filter(news_nation_id=6).order_by('-id')[:1]

    adv_view_carousel_active = advetiment_field.objects.filter(ad_position_id=(1,2)).order_by('-id')[:1]
    adv_view_carousel = advetiment_field.objects.filter(ad_position_id=(1,2)).exclude(id=adv_view_carousel_active).order_by('-id')
    adv_view_small_active = advetiment_field.objects.filter(ad_position_id=(1,2)).order_by('-id')[:1]
    adv_view_small = advetiment_field.objects.filter(ad_position_id=(1,2)).exclude(id=adv_view_small_active).order_by('-id')
    adv_view_side = advetiment_field.objects.filter(ad_position_id=3).order_by('-id')[:5]

    image = news_nation.objects.filter(pk='6')

    page = request.GET.get('page', 1)
    paginator = Paginator(more, 20)
    try:
        n_l_paginator = paginator.page(page)
    except PageNotAnInteger:
        n_l_paginator = paginator.page(1)
    except EmptyPage:
        n_l_paginator = paginator.page(paginator.num_pages)

    s_news = {
        'news': more,
        'internation': inter,
        'kerala_n': n_kerala,
        'gulf_n': n_gulf,
        'local_n': n_local,
        'sports_n': n_sports,
        'more_n': n_more,

        'n_l_p': n_l_paginator,


        'adv_carousel_active' : adv_view_carousel_active,
        'adv_carousel' : adv_view_carousel,
        'adv_small_active' : adv_view_small_active,
        'adv_small' : adv_view_small,
        'adv_side': adv_view_side,
        'logo_img': image,
    }

    return render(request, 'news_types.html', s_news)




def local(request):
    news_page_type = 'Local'
    tsy_news = news_field.objects.filter(news_place_id=1).order_by('-id')[:1]
    tsy_newss = news_field.objects.filter(news_place_id=1).exclude(pk=id(tsy_news)).order_by('-id')[:5]
    kdly_news = news_field.objects.filter(news_place_id=2).order_by('-id')[:1]
    kdly_newss = news_field.objects.filter(news_place_id=2).exclude(pk=id(kdly_news)).order_by('-id')[:5]
    blsry_news = news_field.objects.filter(news_place_id=3).order_by('-id')[:1]
    blsry_newss = news_field.objects.filter(news_place_id=3).exclude(pk=id(blsry_news)).order_by('-id')[:5]
    mukkam_news = news_field.objects.filter(news_place_id=4).order_by('-id')[:1]
    mukkam_newss = news_field.objects.filter(news_place_id=4).exclude(pk=id(mukkam_news)).order_by('-id')[:5]
    thiruvampady_news = news_field.objects.filter(news_place_id=5).order_by('-id')[:1]
    thiruvampady_newss = news_field.objects.filter(news_place_id=5).exclude(pk=id(thiruvampady_news)).order_by('-id')[:5]
    puthuppady_news = news_field.objects.filter(news_place_id=6).order_by('-id')[:1]
    puthuppady_newss = news_field.objects.filter(news_place_id=6).exclude(pk=id(puthuppady_news)).order_by('-id')[:5]
    kattippara_news = news_field.objects.filter(news_place_id=7).order_by('-id')[:1]
    kattippara_newss = news_field.objects.filter(news_place_id=7).exclude(pk=id(kattippara_news)).order_by('-id')[:5]
    inter = news_field.objects.filter(news_nation_id=3).order_by('-id')[:1]
    n_kerala = news_field.objects.filter(news_nation_id=1).order_by('-id')[:1]
    n_gulf = news_field.objects.filter(news_nation_id=2).order_by('-id')[:1]
    n_local = news_field.objects.filter(news_district_id=11).order_by('-id')[:1]
    n_sports = news_field.objects.filter(news_nation_id=5).order_by('-id')[:1]
    n_more = news_field.objects.filter(news_nation_id=6).order_by('-id')[:1]

    adv_view_carousel_active = advetiment_field.objects.filter(ad_position_id=(1,2)).order_by('-id')[:1]
    adv_view_carousel = advetiment_field.objects.filter(ad_position_id=(1,2)).exclude(id=adv_view_carousel_active).order_by('-id')
    adv_view_small_active = advetiment_field.objects.filter(ad_position_id=(1,2)).order_by('-id')[:1]
    adv_view_small = advetiment_field.objects.filter(ad_position_id=(1,2)).exclude(id=adv_view_small_active).order_by('-id')
    adv_view_side = advetiment_field.objects.filter(ad_position_id=3).order_by('-id')[:5]

    ad_view_aftr_tsy_n = advetiment_field.objects.order_by('-id')[:1]
    ad_view_aftr_kdvly = advetiment_field.objects.order_by('-id')[2:3]
    ad_view_aftr_blssry = advetiment_field.objects.order_by('-id')[4:5]
    ad_view_aftr_mukkam = advetiment_field.objects.order_by('-id')[6:7]
    ad_view_aftr_trvmpdy = advetiment_field.objects.order_by('-id')[8:9]
    ad_view_aftr_pdppdy = advetiment_field.objects.order_by('-id')[10:11]
    ad_view_aftr_ktpra = advetiment_field.objects.order_by('-id')[12:13]




    l_news ={
        'm_tsy_news' : tsy_news,
        't_tsy_news' : tsy_newss,
        'm_kdly_news': kdly_news,
        't_kdly_news': kdly_newss,
        'm_blsry_news': blsry_news,
        't_blsry_news': blsry_newss,
        'm_mukkam_news': mukkam_news,
        't_mukkam_news': mukkam_newss,
        'm_trvmpdy_news': thiruvampady_news,
        't_trvmpdy_news': thiruvampady_newss,
        'm_puthuppady_news': puthuppady_news,
        't_puthuppady_news': puthuppady_newss,
        'm_kattippara_news': kattippara_news,
        't_kattippara_news': kattippara_newss,
        'internation': inter,
        'kerala_n': n_kerala,
        'gulf_n': n_gulf,
        'local_n': n_local,
        'type_image': news_page_type,
        'sports_n': n_sports,
        'more_n': n_more,


        'adv_carousel_active' : adv_view_carousel_active,
        'adv_carousel' : adv_view_carousel,
        'adv_small_active' : adv_view_small_active,
        'adv_small' : adv_view_small,
        'adv_side': adv_view_side,

        'adv_aftrtsy': ad_view_aftr_tsy_n,
        'adv_aftrkdly': ad_view_aftr_kdvly,
        'adv_aftrblsy': ad_view_aftr_blssry,
        'adv_aftrmukkam': ad_view_aftr_mukkam,
        'adv_aftrtrvmpdy': ad_view_aftr_trvmpdy,
        'adv_aftrpdppy': ad_view_aftr_pdppdy,
        'adv_aftrktpra': ad_view_aftr_ktpra,



    }
    return render(request,'local_news.html',l_news)




def news_view(request,id):
    news = news_field.objects.get(pk=id)
    n_latest = news_field.objects.exclude(pk=id).order_by('-id')[:50]
    inter = news_field.objects.filter(news_nation_id=3).order_by('-id')[:1]
    n_kerala = news_field.objects.filter(news_nation_id=1).order_by('-id')[:1]
    n_gulf = news_field.objects.filter(news_nation_id=2).order_by('-id')[:1]
    n_local = news_field.objects.filter(news_district_id=11).order_by('-id')[:1]
    n_sports = news_field.objects.filter(news_nation_id=5).order_by('-id')[:1]
    n_more = news_field.objects.filter(news_nation_id=6).order_by('-id')[:1]

    adv_view_carousel_active = advetiment_field.objects.filter(ad_position_id=(1,2)).order_by('-id')[:1]
    adv_view_carousel = advetiment_field.objects.filter(ad_position_id=(1,2)).exclude(id=adv_view_carousel_active).order_by('-id')
    adv_view_small_active = advetiment_field.objects.filter(ad_position_id=(1,2)).order_by('-id')[:1]
    adv_view_small = advetiment_field.objects.filter(ad_position_id=(1,2)).exclude(id=adv_view_small_active).order_by('-id')
    adv_view_side = advetiment_field.objects.filter(ad_position_id=3).order_by('-id')[:5]


    data = {
        'n_view':news,
        'l_news':n_latest,
        'internation': inter,
        'kerala_n': n_kerala,
        'gulf_n': n_gulf,
        'local_n': n_local,
        'sports_n': n_sports,
        'more_n': n_more,


        'adv_carousel_active' : adv_view_carousel_active,
        'adv_carousel' : adv_view_carousel,
        'adv_small_active' : adv_view_small_active,
        'adv_small' : adv_view_small,
        'adv_side': adv_view_side,

    }
    return render(request,'news_view.html',data)



def about (request):
    contents = aboutus_content.objects.order_by('-id')
    user_details = aboutus.objects.all()
    adv_view_carousel_active = advetiment_field.objects.filter(ad_position_id=1).order_by('-id')[:1]
    adv_view_carousel = advetiment_field.objects.filter(ad_position_id=1).exclude(id=adv_view_carousel_active).order_by('-id')
    adv_view_small_active = advetiment_field.objects.filter(ad_position_id=1).order_by('-id')[:1]
    adv_view_small = advetiment_field.objects.filter(ad_position_id=1).exclude(id=adv_view_small_active).order_by('-id')

    context = {
        'content': contents,
        'about_details': user_details,
        'adv_carousel_active': adv_view_carousel_active,
        'adv_carousel': adv_view_carousel,
        'adv_small_active': adv_view_small_active,
        'adv_small': adv_view_small,
    }
    return render(request,'about.html',context)


