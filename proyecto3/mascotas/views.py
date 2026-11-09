from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Responsable, Mascota
from .serializers import ResponsableSerializer, MascotaSerializer

# --- CRUD RESPONSABLE ---

@api_view(['POST', 'PUT'])
def crear_responsable(request):
    serializer = ResponsableSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listar_responsable(request):
    responsables = Responsable.objects.all()
    serializer = ResponsableSerializer(responsables, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PATCH'])
def modificar_responsable(request, pk):
    try:
        responsable = Responsable.objects.get(pk=pk)
    except Responsable.DoesNotExist:
        return Response({'error': 'Responsable no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ResponsableSerializer(responsable, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def eliminar_responsable(request, pk):
    try:
        responsable = Responsable.objects.get(pk=pk)
    except Responsable.DoesNotExist:
        return Response({'error': 'Responsable no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    responsable.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


# --- CRUD MASCOTA ---

@api_view(['POST', 'PUT'])
def crear_mascota(request):
    serializer = MascotaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listar_mascotas(request):
    mascotas = Mascota.objects.all()
    serializer = MascotaSerializer(mascotas, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PATCH'])
def modificar_mascota(request, pk):
    try:
        mascota = Mascota.objects.get(pk=pk)
    except Mascota.DoesNotExist:
        return Response({'error': 'Mascota no encontrada'}, status=status.HTTP_404_NOT_FOUND)

    serializer = MascotaSerializer(mascota, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def eliminar_mascota(request, pk):
    try:
        mascota = Mascota.objects.get(pk=pk)
    except Mascota.DoesNotExist:
        return Response({'error': 'Mascota no encontrada'}, status=status.HTTP_404_NOT_FOUND)

    mascota.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)