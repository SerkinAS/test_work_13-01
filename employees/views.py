from django.db.models import Q
from django.views.generic import DetailView
from django.views.generic import ListView
from employees.helpers import get_letters
from employees.models import Employee


class EmployeeListView(ListView):
    """Представление для получения списка сотрудников."""

    model = Employee
    context_object_name = 'employees'
    paginate_by = 100

    def get_queryset(self):
        """Формирование кверисета."""
        self.queryset = self.model.objects.all()
        # Получим параметр.
        letter_range = self.request.GET.get('filter')
        # Если параметра нет, возвращаем кверисет всех сотрудников.
        if letter_range:
            # Получим строку из букв для формирования фильтра.
            letters = get_letters(letter_range)
            surname_filter = Q()
            # Сформируем фильтр.
            for letter in letters:
                surname_filter |= Q(surname__istartswith=letter)
            self.queryset = self.queryset.filter(
                surname_filter
            ).order_by('surname')
        return self.queryset


class EmployeeDetailView(DetailView):
    """Представление для получения данных конкретного сотрудника."""

    model = Employee
    template_name = 'employees/employee-detail.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'employee'
