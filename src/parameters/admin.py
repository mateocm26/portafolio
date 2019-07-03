from django.contrib import admin

from .models import Etnic
from .models import TypeAchievements
from .models import TypePosition
from .models import TypeUser
from .models import DocumentType
from .models import StatusMarital
from .models import TypeStudies
# Register your models here.

admin.site.register(Etnic)
admin.site.register(TypeAchievements)
admin.site.register(TypePosition)
admin.site.register(TypeStudies)
admin.site.register(TypeUser)
admin.site.register(StatusMarital)
admin.site.register(DocumentType)
