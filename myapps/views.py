from django.shortcuts import render


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

    context = dict()
    context['data1'] = lst.copy()
    #context['data2'] = second_job
    #context['data3'] = third_job
    #context['data4'] = fourth_job
    #context['data5'] = fifth_job
    lst.clear()
    lst.append(fourth_job)
    lst.append(fifth_job)
    context['data2'] = lst.copy()
    lst.clear()

    return render(request, 'careers_mentor.html', {"output": context})


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
        'button_href': '/donate/'
    }
    second_job = {
        'title': 'School #7',
        'image': '/static/images/images.squarespace-cdn.com.jpeg',
        'description': '''Here is a description of your campaign.
         Nullam tempor dolor sed nulla auctor, nec placerat felis sodales.
         Etiam et turpis mattis, efficitur mi ut, ultrices diam.
         Donec consectetur, odio eget porta varius, orci mauris viverra ante, eget egestas turpis sapien vel orci.
         Donec eu ornare augue, ut.''',

        'more_text': "More information →",
        'more_href': "#",
        'button_name': "1",
        'button_id': "1",
        'button_title': "SPONSOR THIS CAMPAIGN",
        'button_href': "#"
    }
    third_job = {
        'title': 'STEM Materials',
        'image': '/static/images/images.squarespace-cdn.comx.jpeg',
        'description': '''Here is a description of your campaign.
         Nullam tempor dolor sed nulla auctor, nec placerat felis sodales.
         Etiam et turpis mattis, efficitur mi ut, ultrices diam.
         Donec consectetur, odio eget porta varius, orci mauris viverra ante, eget egestas turpis sapien vel orci.
         Donec eu ornare augue, ut.''',

        'more_text': "More information →",
        'more_href': "#",
        'button_name': "1",
        'button_id': "1",
        'button_title': "SPONSOR THIS CAMPAIGN",
        'button_href': "#"
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
