from django.db.models.functions import Lower

from wagtail.api.v2.endpoints import BaseAPIEndpoint
from wagtail.api.v2.filters import FieldsFilter, OrderingFilter, SearchFilter

from hra.glossary.filters import GlossaryTermsStartsWithFilter
from hra.glossary.models import GlossaryTerm
from hra.glossary.pagination import GlossaryTermsPagination
from hra.glossary.serializers import GlossaryTermSerializer


class GlossaryTermsAPIEndpoint(BaseAPIEndpoint):
    base_serializer_class = GlossaryTermSerializer
    filter_backends = [FieldsFilter, OrderingFilter, SearchFilter, GlossaryTermsStartsWithFilter]
    body_fields = BaseAPIEndpoint.body_fields + ['name', 'description', 'is_noun']
    listing_default_fields = BaseAPIEndpoint.listing_default_fields + ['name', 'description', 'is_noun']
    nested_default_fields = BaseAPIEndpoint.nested_default_fields + ['name']
    name = 'glossary_terms'
    model = GlossaryTerm
    pagination_class = GlossaryTermsPagination

    known_query_parameters = BaseAPIEndpoint.known_query_parameters.union([
        GlossaryTermsStartsWithFilter.query_parameter
    ])

    def get_queryset(self):
        return super().get_queryset().order_by(Lower('name'))
