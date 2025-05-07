
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def authors(request):
    team = [
        {"name": "Team Member 1", "code": "12345"},
        {"name": "Team Member 2", "code": "67890"},
        # Add your team members' names and codes here
    ]
    return Response({"authors": team})