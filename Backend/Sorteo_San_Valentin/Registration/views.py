from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.signing import TimestampSigner, BadSignature, SignatureExpired
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Registration
from .forms import RegistrationForm
from .tasks import verify_email, send_winner_email
from .serializers import SetPasswordSerializer, AdminLoginSerializer


# Create your views here.

class RegistrationView(APIView):
    def post(self,request):

        form = RegistrationForm(request.data)
        print(request.data)
        print(form.errors)
        if form.is_valid():
            regist = form.save()
            email = regist.email
            id = regist.id
            verify_email.delay(email,id)

            return Response(
                {"message":"¡Gracias por registrarte! Revisa tu correo para verificar tu cuenta."}
            )
        else:
            return Response(
                form.errors, status =status.HTTP_400_BAD_REQUEST
            )
        
class VerifyView(APIView):
    def post(token,request):

        signer = TimestampSigner()
        User = get_user_model()

        try:
            user_id = signer.unsign(token, max_age=60*60*24) 
        except SignatureExpired:
            return Response({"error":"El enlace ha expirado."},status=status.HTTP_400_BAD_REQUEST)
        except BadSignature:
            return Response({"Token inválido."},status=status.HTTP_400_BAD_REQUEST)
        
        user = get_object_or_404(User,id=user_id)

        serializer = SetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user)
            return Response({"mensaje":"Tu cuenta ha sido activada. Ya estás participando en el sorteo."}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(APIView):
    def post(self,request):
        serializer = AdminLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response({
                "message":"login exitoso",
                "refresh":str(refresh),
                "access":str(refresh.access_token)           
                })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class SelectWinnerview(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        participant= Registration.objects.filter(is_verified=True)
        if participant.exists():
            winner = participant.order_by('?').first()
            send_winner_email.delay(winner.email, winner.full_name)
            return Response({
                "message":"Ganador seleccionado",
                "winner": {
                    "full_name": winner.full_name,
                    "email": winner.email,
                }
            }, status=status.HTTP_200_OK)
        return Response({"error":"No hay participantes verificados."}, status=status.HTTP_400_BAD_REQUEST)


class ParticipantListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        participants = Registration.objects.all()
        data = [
            {
                "full_name": participant.full_name,
                "email": participant.email,
                "is_verified": participant.is_verified
            }
            for participant in participants
        ]
        return Response(data, status=status.HTTP_200_OK)
            
            





                
            
            


        
        



        
