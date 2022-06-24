from django.contrib import admin

# Register your models here.
from .models import GroupStagePrediction, Top16Prediction, Top8Prediction, Top4Prediction, Top2Prediction

admin.site.register(GroupStagePrediction)
admin.site.register(Top16Prediction)
admin.site.register(Top8Prediction)
admin.site.register(Top4Prediction)
admin.site.register(Top2Prediction)
