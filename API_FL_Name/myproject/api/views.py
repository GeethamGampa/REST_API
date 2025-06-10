from rest_framework.views import APIView
from rest_framework.response import Response

# Provides HTTP status codes like 200 (OK), 400 (Bad Request),
from rest_framework import status

class FullNameAPIView(APIView):
    def post(self, request):
        data = request.data # holds the parsed JSON body

        if not isinstance(data, list):
            return Response({'error': 'Expected a list of names.'}, status=status.HTTP_400_BAD_REQUEST)

        full_names = []
        for person in data:
            first_name = person.get('first_name')
            last_name = person.get('last_name')

            if not first_name or not last_name:
                return Response({'error': 'Each item must include first_name and last_name.'}, status=status.HTTP_400_BAD_REQUEST)

            full_name = f"{first_name.strip().title()} {last_name.strip().title()}"
            full_names.append(full_name)

        return Response({'full_names': full_names}, status=status.HTTP_200_OK)



