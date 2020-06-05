"""django_GuanGuanNFC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from guan import views as GuanViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('DaoUserInfo/insert/',GuanViews.DaoUserInfoInsert),
    path('DaoUserInfo/loadQuery/',GuanViews.DaoUserInfoLoadQuery),
    path('DaoUserInfo/delete/',GuanViews.DaoUserInfoDelete),
    path('DaoUserInfo/update/',GuanViews.DaoUserInfoUpdate),
    path('DaoUserInfo/registrationQuery/',GuanViews.DaoUserInfoRegistrationQuery),
    path('DaoUserInfo/updateLastAct/',GuanViews.DaoUserInfoUpdateLastAct),
    path('DaoUserInfo/queryLastActDate/',GuanViews.DaoUserInfoQueryLastActDate),
    path('DaoUserInfo/updateActiveDay/',GuanViews.DaoUserInfoUpdateActiveDay),
    path('DaoUserInfo/personMessage/',GuanViews.UserInfoAPIView.as_view(),name="UserInfo"),
    path('DaoActivityType/insert/',GuanViews.DaoActivityTypeInsert),
    path('DaoActivityType/delete/',GuanViews.DaoActivityTypeDelete),
    path('DaoActivityType/update/',GuanViews.DaoActivityTypeUpdate),
    path('DaoActivityType/query/',GuanViews.ActivityTypeAPIView.as_view(),name="ActivityType"),
    path('DaoActivityType/queryAllType/',GuanViews.ActivityTypeAllAPIView.as_view(),name="AllActivityType"),
    path('DaoActivityType/queryTypeAndActivity/',GuanViews.ActivityAPIView.as_view(),name="Activity"),
    path('DaoActivity/insert1/',GuanViews.DaoActivityInsert1),
    path('DaoActivity/insert2/',GuanViews.DaoActivityInsert2),
    path('DaoActivity/delete/',GuanViews.DaoActivityDelete),
    path('DaoActivity/update/',GuanViews.DaoActivityUpdate),
    path('DaoActivity/query1/',GuanViews.DaoActivityQuery1),
    path('DaoActivity/query2/',GuanViews.DaoActivityQuery2),
    path('DaoActivity/queryActivityByNFC/',GuanViews.Activity2APIView.as_view(),name="Activity2"),
    path('DaoActSta/insert/',GuanViews.DaoActStaInsert),
    path('DaoActSta/insert2/',GuanViews.DaoActStaInsert2),
    path('DaoActSta/insert3/',GuanViews.DaoActStaInsert3),
    path('DaoActSta/update/',GuanViews.DaoActStaUpdate),
    path('DaoActSta/update2/',GuanViews.DaoActStaUpdate2),
    path('DaoActSta/delete/',GuanViews.DaoActivityDelete),
    path('DaoActSta/queryActType/',GuanViews.DaoActStaQueryActType),
    path('DaoActSta/queryActType2/',GuanViews.DaoActStaQueryActType2),
    path('DaoActSta/queryByLengthDesc/',GuanViews.DaoActStaQueryByLengthDesc),
    path('DaoActSta/queryByLengthAsc/',GuanViews.DaoActStaQueryByLengthAsc),
    path('DaoActSta/queryByTimeDesc/',GuanViews.DaoActStaQueryByTimeDesc),
    path('DaoActSta/queryByTimeAsc/',GuanViews.DaoActStaQueryByTimeAsc),
    path('DaoActSta/queryByLengthDesc2/',GuanViews.DaoActStaQueryByLengthDesc2),
    path('DaoActSta/queryByLengthAsc2/',GuanViews.DaoActStaQueryByLengthAsc2),
    path('DaoActSta/queryByTimeDesc2/',GuanViews.DaoActStaQueryByTimeDesc2),
    path('DaoActSta/queryByTimeAsc2/',GuanViews.DaoActStaQueryByTimeAsc2),
    path('DaoBox/insert/',GuanViews.DaoBoxInsert),
    path('DaoBox/insert2/', GuanViews.DaoBoxInsert2),
    path('DaoBox/delete/',GuanViews.DaoBoxDelete),
    path('DaoBox/updateName/',GuanViews.DaoBoxUpdateName),
    path('DaoBox/updatePos/',GuanViews.DaoBoxUpdatePos),
    path('DaoBox/query/',GuanViews.DaoBoxQuery),
    path('DaoBox/query2/',GuanViews.DaoBoxQueryNFC),
    path('DaoBox/queryBoxByNFC/',GuanViews.DaoBoxQueryBoxByNFC),
    path('DaoBox/queryAllBox/',GuanViews.DaoBoxQueryAllBoxAPIView.as_view(),name="AllBox"),
    path('DaoBox/queryBoxAndContent/',GuanViews.DaoBoxQueryBoxAndContent),
    path('DaoBox/queryBox/',GuanViews.DaoBoxQueryBox),
    path('DaoBoxContent/insert/',GuanViews.DaoBoxContentInsert),
    path('DaoBoxContent/insert2/',GuanViews.DaoBoxContentInsert2),
    path('DaoBoxContent/delete/',GuanViews.DaoBoxContentDelete),
    path('DaoBoxContent/delete2/', GuanViews.DaoBoxContentDelete2),
    path('DaoBoxContent/update/', GuanViews.DaoBoxContentUpdate),
    path('DaoBoxContent/loadQuery/', GuanViews.DaoBoxContentLoadQuery),
    path('DaoFriend/insert/',GuanViews.DaoFriendInsert),
    path('DaoFriend/insert2/',GuanViews.DaoFriendInsert2),
    path('DaoFriend/delete/',GuanViews.DaoFriendDelete),
    path('DaoFriend/query/',GuanViews.DaoFriendQuery),
    path('DaoFriend/queryFriendAct/',GuanViews.DaoFriendQueryFriendAct),
    path('DaoMoment/insert/',GuanViews.DaoMomentInsert),
    path('DaoMoment/insert2/', GuanViews.DaoMomentInsert2),
    path('DaoMoment/delete/', GuanViews.DaoMomentDelete),
    path('DaoMoment/update/', GuanViews.DaoMomentUpdate),
    path('DaoMoment/query/',GuanViews.DaoMomentQueryAPIView.as_view(),name="query"),
    path('DaoPush/insert/',GuanViews.DaoPushInsert),
    path('DaoPush/delete/', GuanViews.DaoPushDelete),
    path('DaoPush/query/',GuanViews.DaoPushAPIView.as_view(),name="query"),
]
