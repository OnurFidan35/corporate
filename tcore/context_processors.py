from .models import Setting

def SettingList(request):
    try:
         context=Setting.objects.first
    except Setting.DoesNotExist:
         context=None

    return {'setting':context}
    