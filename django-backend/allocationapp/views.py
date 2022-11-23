from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse

def index(request):
    # This might return the login/landing page? Probably will be
    # Right now it just redirects to the login page
    return redirect(reverse('allocationapp:graduate_login'))

def graduate_login(request):
    # Login via code page for the GRADUATE.
    context_dict = {}
    return render(request, 'allocationapp/login.html', context=context_dict) 

def cast_votes(request):
    # View function for the GRADUATE CAST VOTES page.

    # Currently populated with mock data
    # Frontend expects this format.
    #   'teams' will be a list of dictionaries, each with the desired team info
    #   could also potentially have a Class GradTeam, and the 'teams' list will be a list of instances of GradTeam?
    #   will require minor frontend changes if this path is chosen.
    context_dict = {
        'teams': [
            {
                'team_name': 'Team 1',
                'department': 'Data Analytics',
                'technologies': ['Python', 'Java', 'Django'],
                'skills': ['Mathematics', 'Programming'],
                'group_size': 16,
                'description': 'description text here',
                'id': 123,  # unique ID
            },

            {
                'team_name': 'Team 2',
                'department': 'Banking Apps',
                'technologies': ['C++', 'Java', 'C#'],
                'skills': ['Smartness', 'Programming'],
                'group_size': 20,
                'description': 'description text here as well',
                'id': 345,
            }
        ]
    }

    return render(request, 'allocationapp/cast_votes.html', context=context_dict)