from rest_framework.decorators import api_view
from rest_framework.response import Response
from StudentApp.serializers import StudentSerializer
from StudentApp.models import Student


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def student_api(request, id=None):
    if request.method == 'GET':
        if id is not None:
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Added successfully"})
        return Response(serializer.errors, status=400)

    elif request.method == 'PUT':
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Updated successfully"})
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        student = Student.objects.get(id=id)
        student.delete()
        return Response({"message": "Deleted successfully"})
