import whois
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def dns_info(request):
    domain = request.query_params.get('domain')
    info = whois.whois(domain)
    if info:
        return Response(info, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)