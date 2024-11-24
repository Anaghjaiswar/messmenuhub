from django.shortcuts import render

# Dashboard view
def dashboard(request):
    return render(request, 'owners/MessOwners_dashboard.html')


# Manage menu view
def manage_menu(request):
    return render(request, 'owners/manage-menu.html')

# Signup page view
def signup(request):
    return render(request, 'owners/signuppage.html')

# Login page view
def login(request):
    return render(request, 'owners/loginpage.html')

# Menu posting view
def menu_posting(request):
    return render(request, 'owners/menu_posting.html')

# Resources view
def resources(request):
    return render(request, 'owners/resources.html')


def special_offers_promotions(request):
    return render(request, 'owners/special_offers_promotions.html')

def help_guidelines(request):
    return render(request, 'owners/help_guidelines.html')


def contact_support(request):
    return render(request, 'owners/contact_support.html')

def announcements(request):
    return render(request, 'owners/announcements.html')
