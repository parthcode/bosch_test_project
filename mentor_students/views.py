from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from mentor_students.serializer import MyTokenObtainPairSerializer


class StudentViewSet(FlexFieldsModelViewSet):

    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = [IsAuthenticated]


class MentorViewSet(FlexFieldsModelViewSet):

    serializer_class = MentorSerializer
    queryset = Mentor.objects.all()
    permission_classes = [IsAuthenticated]


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer