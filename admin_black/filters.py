from django.contrib.admin.filters import (
    SimpleListFilter,
    AllValuesFieldListFilter,
    ChoicesFieldListFilter,
    RelatedFieldListFilter,
    RelatedOnlyFieldListFilter
)


class SimpleDropdownFilter(SimpleListFilter):
    template = 'listfilter_dropdown/dropdown_filter.html'


class DropdownFilter(AllValuesFieldListFilter):
    template = 'listfilter_dropdown/dropdown_filter.html'


class ChoiceDropdownFilter(ChoicesFieldListFilter):
    template = 'listfilter_dropdown/dropdown_filter.html'


class RelatedDropdownFilter(RelatedFieldListFilter):
    template = 'listfilter_dropdown/dropdown_filter.html'


class RelatedOnlyDropdownFilter(RelatedOnlyFieldListFilter):
    template = 'listfilter_dropdown/dropdown_filter.html'
