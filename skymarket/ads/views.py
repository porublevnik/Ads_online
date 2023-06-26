from rest_framework import pagination, viewsets
from .models import Ad
from .serializers import AdSerializer, AdDetailSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 5



class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all().order_by('id')
    default_serializer = AdSerializer
    serializers = {
        'list': AdSerializer,
        'retrieve': AdDetailSerializer
    }
    pagination_class = AdPagination



class CommentViewSet(viewsets.ModelViewSet):
    pass

# @api_view(['GET'])
# def user_vacancies(request):
#     user_qs = User.objects.annotate(vacancies=Count('vacancy'))
#
#     paginator = Paginator(user_qs, settings.TOTAL_ON_PAGE)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#
#     users = []
#     for user in page_obj:
#         users.append({
#             'id': user.id,
#             'name': user.username,
#             'vacancies': user.vacancies
#         })
#
#     response = {
#         'items': users,
#         'total': paginator.count,
#         'num_pages': paginator.num_pages,
#         'avg': user_qs.aggregate(avg=Avg('vacancies'))['avg']
#     }
#
#     return JsonResponse(response)