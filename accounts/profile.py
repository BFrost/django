from models import UserProfile
from forms import UserProfileForm

def retrieve(request):
    ''' that requires an authenticated user before calling'''
    try:
        profile = request.user.get_profile()
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=request.user)
        profile.save()
    return profile

def set(request):
    profile = retrieve(request)
    profile_form = UserProfileForm(request.POST, instance=profile)
    profile_form.save()
