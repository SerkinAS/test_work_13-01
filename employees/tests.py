import datetime
from django.test import TestCase
from employees.models import Employee
from employees.models import Group


class EmployeeModelTest(TestCase):
    """Тесты для модели сотрудника."""

    @classmethod
    def setUpTestData(cls):
        """Тест на создание объекта модели."""
        Group.objects.create(
            name='Технический отдел',
        )
        Employee.objects.create(
            firstname='Алексей',
            surname='Алексеев',
            patronymic='Алексеевич',
            date_birdth=datetime.datetime.now(),
            email='hehehihi@gmail.com',
            date_job_start=datetime.datetime.now(),
            date_job_end=datetime.datetime.now(),
            position_at_work='Младший разработчик',
            group=Group.objects.get(id=1),
        )

    def test_firstname_label(self):
        """Тест для сопоставления verbose_name."""
        employee = Employee.objects.get(id=1)
        field_label = employee._meta.get_field('firstname').verbose_name
        self.assertEquals(field_label, 'Имя')

    def test_firstname_max_length(self):
        """Тест на максимальную длину поля имя."""
        employee = Employee.objects.get(id=1)
        max_length = employee._meta.get_field('firstname').max_length
        self.assertEquals(max_length, 40)

    def test_get_absolute_url(self):
        """Тест на сопоставление абсолютного url объекта."""
        employee = Employee.objects.get(id=1)
        self.assertEquals(employee.get_absolute_url, '/employees/1')
