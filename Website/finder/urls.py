from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register('api/stats/2018', PlayerStatsViewSets, 'PlayerStatsViewSets')
router.register('api/stats/actual', ActualAllStarsViewSets, 'ActualAllStarsViewSets')
router.register('api/stats/predicted', PredictedAllStarsViewSets, 'PredictedAllStarsViewSets')

urlpatterns = [

]

urlpatterns += router.urls
