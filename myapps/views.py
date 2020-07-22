from django.shortcuts import render
from .models import LatestNews
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')


def ourVisionView(request):
    return render(request, 'our_vision.html')


def careersMentorView(request):
    first_job = {
        'title': 'Join Mentor',
        'description': "Here is a description of your company. Morbi tristique senectus et netus et malesuada fames ac turpis egestas."
        + "Nullam tempor dolor sed nulla auctor, nec placerat felis sodales. Etiam et turpis mattis, efficitur mi ut, ultrices diam. Donec consectetur, eget porta varius, orci mauris viverra ante, eget egestas turpis sapien vel orci."
        + " Donec eu ornare augue, ut efficitur velit.",
        'qualifications': 'Benefits',
        'details': '''Vestibulum et magna mattis
                    Sollicitudin ligula ac, facilisis dui
                    Ut blandit lectus neque
                    Sit fringilla nisi mollis eget
                    Sed a nec leo euismod eleifend
                    Sit amet ut nisl blandit''',

        'button_name': "",
        'button_id': "",
    }
    second_job = {
        'title': 'Open Position — Dauphine',
        'description': "Here is a description of your company. Morbi tristique senectus et netus et malesuada fames ac turpis egestas."
        + "Nullam tempor dolor sed nulla auctor, nec placerat felis sodales. Etiam et turpis mattis, efficitur mi ut, ultrices diam. Donec consectetur, eget porta varius, orci mauris viverra ante, eget egestas turpis sapien vel orci."
        + " Donec eu ornare augue, ut efficitur velit.",
        'qualifications': 'Qualifications',
        'details': '''Pellentesque habitant morbi
   					Tristique senectus et malesuada
   					Fames ac turpis egestas
   					Nullam tempor dolor sed nulla
   					Auctor nec placerat felis
   					Sodales. Etiam et turpis mattis
   					Efficitur mi ut, ultrices diam''',

        'button_name': "btn2",
        'button_id': "",
    }
    third_job = {
        'title': 'Open Position — Dauphine',
        'description': "Here is a description of your company. Morbi tristique senectus et netus et malesuada fames ac turpis egestas."
        + "Nullam tempor dolor sed nulla auctor, nec placerat felis sodales. Etiam et turpis mattis, efficitur mi ut, ultrices diam. Donec consectetur, eget porta varius, orci mauris viverra ante, eget egestas turpis sapien vel orci."
        + " Donec eu ornare augue, ut efficitur velit.",
        'qualifications': 'Qualifications',
        'details': '''Pellentesque habitant morbi
   					Tristique senectus et malesuada
   					Fames ac turpis egestas
   					Nullam tempor dolor sed nulla
   					Auctor nec placerat felis
   					Sodales. Etiam et turpis mattis
   					Efficitur mi ut, ultrices diam''',
        'button_name': "btn3",
        'button_id': "",
    }
    fourth_job = {
        'title': 'Open Position — Lafayette',
        'description': "Here is a description of your company. Morbi tristique senectus et netus et malesuada fames ac turpis egestas."
        + "Nullam tempor dolor sed nulla auctor, nec placerat felis sodales. Etiam et turpis mattis, efficitur mi ut, ultrices diam. Donec consectetur, eget porta varius, orci mauris viverra ante, eget egestas turpis sapien vel orci."
        + " Donec eu ornare augue, ut efficitur velit.",
        'qualifications': 'Qualifications',
        'details': '''Pellentesque habitant morbi
   					Tristique senectus et malesuada
   					Fames ac turpis egestas
   					Nullam tempor dolor sed nulla
   					Auctor nec placerat felis
   					Sodales. Etiam et turpis mattis
   					Efficitur mi ut, ultrices diam''',
        'button_name': "btn4",
        'button_id': "",
    }
    fifth_job = {
        'title': 'Open Position — Lafayette',
        'description': "Here is a description of your company. Morbi tristique senectus et netus et malesuada fames ac turpis egestas."
        + "Nullam tempor dolor sed nulla auctor, nec placerat felis sodales. Etiam et turpis mattis, efficitur mi ut, ultrices diam. Donec consectetur, eget porta varius, orci mauris viverra ante, eget egestas turpis sapien vel orci."
        + " Donec eu ornare augue, ut efficitur velit.",
        'qualifications': 'Qualifications',
        'details': '''Pellentesque habitant morbi
   					Tristique senectus et malesuada
   					Fames ac turpis egestas
   					Nullam tempor dolor sed nulla
   					Auctor nec placerat felis
   					Sodales. Etiam et turpis mattis
   					Efficitur mi ut, ultrices diam''',
        'button_name': "btn4",
        'button_id': "",
    }
    lst = []
    lst.append(first_job)
    lst.append(second_job)
    lst.append(third_job)
    lst.append(fourth_job)
    lst.append(fifth_job)
    context = dict()
    context['data'] = lst.copy()
    lst.clear()

    return render(request, 'careers_mentor.html', context)


def mentorTeamView(request):
    return render(request, 'mentor_team.html')


def contactView(request):
    return render(request, 'contact.html')


def donateView(request):
    return render(request, 'donate.html')


def BecomeaSponsorView(request):

    first_job = {
        'title': 'Sponsor a Campaign',
        'image': '',
        'description': '''Here is a description of what sponsorship means for your company. 
        Morbi tristique senectus et netus et malesuada fames ac turpis egestas.
        Nullam tempor dolor sed nulla auctor, nec placerat felis sodales. Etiam et turpis mattis, efficitur mi ut, ultrices diam. 
        Donec consectetur, eget porta varius, orci mauris viverra ante, eget egestas turpis sapien vel orci. 
        Donec eu ornare augue, ut efficitur velit.''',

        'more_text': "",
        'more_href': "",
        'button_name': "",
        'button_id': "",
        'button_title': "MAKE A GENERAL DONATION →",
        'button_href': 'donate'
    }
    second_job = {
        'title': 'School #7',
        'image': 'images.squarespace-cdn.com.jpeg',
        'description': '''Here is a description of your campaign.
         Nullam tempor dolor sed nulla auctor, nec placerat felis sodales.
         Etiam et turpis mattis, efficitur mi ut, ultrices diam.
         Donec consectetur, odio eget porta varius, orci mauris viverra ante, eget egestas turpis sapien vel orci.
         Donec eu ornare augue, ut.''',

        'more_text': "More information →",
        'more_href': "campaign-1",
        'button_name': "1",
        'button_id': "1",
        'button_title': "SPONSOR THIS CAMPAIGN",
        'button_href': "donate"
    }
    third_job = {
        'title': 'STEM Materials',
        'image': 'images.squarespace-cdn.comx.jpeg',
        'description': '''Here is a description of your campaign.
         Nullam tempor dolor sed nulla auctor, nec placerat felis sodales.
         Etiam et turpis mattis, efficitur mi ut, ultrices diam.
         Donec consectetur, odio eget porta varius, orci mauris viverra ante, eget egestas turpis sapien vel orci.
         Donec eu ornare augue, ut.''',

        'more_text': "More information →",
        'more_href': "campaign-2",
        'button_name': "1",
        'button_id': "1",
        'button_title': "SPONSOR THIS CAMPAIGN",
        'button_href': "donate"
    }
    lst = []
    lst.append(first_job)
    lst.append(second_job)
    lst.append(third_job)

    context = dict()
    context['data1'] = lst.copy()
    lst.clear()
    return render(request, 'become_a_sponsor.html', {'output': context})


def UnderConstructionView(request):
    return render(request, 'under_construction.html')


def annualReportView(request):
    return render(request, 'under_construction.html')


def successStoriesView(request):
    row1 = {
        'title': '1. Ut dui quam, dignissim sed nisl.',

        'col1': '''Here is a description of what sponsorship means for your company. 
        Morbi tristique senectus et netus et malesuada fames ac turpis egestas.
        Nullam tempor dolor sed nulla auctor, nec placerat felis sodales. Etiam et turpis mattis, efficitur mi ut, ultrices diam. 
        Donec consectetur, eget porta varius, orci mauris viverra ante, eget egestas turpis sapien vel orci. 
        Donec eu ornare augue, ut efficitur velit.''',

        'col2': '''Sed a eros nec leo euismod eleifend sit amet ut nisl. 
        Sed a eros nec leo euismod eleifend sit amet ut nisl blandit. 
        Nullam tempor dolor sed nulla auctor, nec placerat felis sodales. 
        Etiam et turpis mattis, efficitur mi ut, ultrices diam. Donec consectetur, odio eget porta varius, orci mauris viverra ante, eget egestas turpis sapien vel orci.
        Donec eu ornare augue, ut efficitur velit. Vestibulum et magna mattis, sollicitudin ligula.
        Donec consectetur, odio eget porta varius, orci mauris viverra ante, eget egestas turpis sapien vel orci.
        Donec eu ornare augue, ut efficitur velit. 
        Vestibulum et magna mattis, sollicitudin ligula ac, facilisis dui.''',

        'col3': '''''',

        'quotes': '''“Ut dui quam, dignissim sed nisl sed, viverra tempor ipsum. Sed a eros nec leo euismod eleifend sit.”''',
        'quotes_src': "Quote Source",
        'image': ''

    }
    row2 = {
        'title': '2. Ut dui quam, dignissim sed nisl.',

        'col1': '''Here is a description of what sponsorship means for your company. 
        Morbi tristique senectus et netus et malesuada fames ac turpis egestas.
        Nullam tempor dolor sed nulla auctor, nec placerat felis sodales. Etiam et turpis mattis, efficitur mi ut, ultrices diam. 
        Donec consectetur, eget porta varius, orci mauris viverra ante, eget egestas turpis sapien vel orci. 
        Donec eu ornare augue, ut efficitur velit.''',

        'col2': '''Sed a eros nec leo euismod eleifend sit amet ut nisl. 
        Sed a eros nec leo euismod eleifend sit amet ut nisl blandit. 
        Nullam tempor dolor sed nulla auctor, nec placerat felis sodales. 
        Etiam et turpis mattis, efficitur mi ut, ultrices diam. Donec consectetur, odio eget porta varius, orci mauris viverra ante, eget egestas turpis sapien vel orci.
        Donec eu ornare augue, ut efficitur velit. Vestibulum et magna mattis, sollicitudin ligula.
        Donec consectetur, odio eget porta varius, orci mauris viverra ante, eget egestas turpis sapien vel orci.
        Donec eu ornare augue, ut efficitur velit. 
        Vestibulum et magna mattis, sollicitudin ligula ac, facilisis dui.''',

        'col3': '''''',

        'quotes': '''''',
        'quotes_src': "",
        'image': 'success_stories_1.jpeg'

    }
    row3 = {
        'title': '3. Ut dui quam, dignissim sed nisl.',

        'col1': '''Here is a description of what sponsorship means for your company. 
        Morbi tristique senectus et netus et malesuada fames ac turpis egestas.
        Nullam tempor dolor sed nulla auctor, nec placerat felis sodales. Etiam et turpis mattis, efficitur mi ut, ultrices diam. 
        Donec consectetur, eget porta varius, orci mauris viverra ante, eget egestas turpis sapien vel orci. 
        Donec eu ornare augue, ut efficitur velit.''',

        'col2': '''Sed a eros nec leo euismod eleifend sit amet ut nisl. 
        Sed a eros nec leo euismod eleifend sit amet ut nisl blandit. 
        Nullam tempor dolor sed nulla auctor, nec placerat felis sodales. 
        Etiam et turpis mattis, efficitur mi ut, ultrices diam. Donec consectetur, odio eget porta varius, orci mauris viverra ante, eget egestas turpis sapien vel orci.
        Donec eu ornare augue, ut efficitur velit. Vestibulum et magna mattis, sollicitudin ligula.
        Donec consectetur, odio eget porta varius, orci mauris viverra ante, eget egestas turpis sapien vel orci.
        Donec eu ornare augue, ut efficitur velit. 
        Vestibulum et magna mattis, sollicitudin ligula ac, facilisis dui.''',

        'col3': '''''',

        'quotes': '''''',
        'quotes_src': "",
        'image': ''

    }
    lst = []
    lst.append(row1)
    lst.append(row2)
    lst.append(row3)

    context = dict()
    context['data'] = lst.copy()
    lst.clear()
    return render(request, 'success_stories.html', context)


def campaign1View(request):
    return render(request, 'campaign-1.html')


def campaign2View(request):
    return render(request, 'campaign-2.html')


def campaign3View(request):
    return render(request, 'campaign-3.html')


def campaign4View(request):
    return render(request, 'campaign-4.html')


def latestNewsView(request):

    post = LatestNews.objects.all()
    return render(request, 'latest_news.html', {'data': post})


def latestNewsClickView(request, slug):
    detail = LatestNews.objects.filter(slug=slug)
    print(detail)
    if detail.exists():
        detail = detail.first()
    else:
        return HttpResponse("<h3>Page not found</h3>")
    return render(request, "latest_news_click.html", {'detail': detail})
