from django.db import models
from django.urls import reverse


class Group(models.Model):
    """Модель отдел."""

    name = models.CharField(
        verbose_name='Название отдела',
        max_length=30
    )

    def __str__(self):
        return self.name

    class Meta:
        """Метаописание."""

        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class Employee(models.Model):
    """Модель сотрудник."""

    firstname = models.CharField(
        verbose_name='Имя',
        max_length=40,
    )
    surname = models.CharField(
        verbose_name='Фамилия',
        max_length=40,
    )
    patronymic = models.CharField(
        verbose_name='Отчество',
        max_length=40,
        blank=True,
    )
    date_birdth = models.DateTimeField(
        verbose_name='Дата рождения'
    )
    email = models.CharField(
        verbose_name='Электронная почта',
        max_length=30,
    )
    date_job_start = models.DateTimeField(
        verbose_name='Дата начала работы'
    )
    date_job_end = models.DateTimeField(
        verbose_name='Дата окончания работы',
        blank=True,
        null=True,
    )
    position_at_work = models.CharField(
        verbose_name='Должность',
        max_length=50
    )
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def get_fullname(self):
        """Возвращает ФИО."""
        return f'{self.surname} {self.firstname} {self.patronymic}'

    def __str__(self):
        """Представление кверисета."""
        return self.get_fullname()

    @property
    def get_absolute_url(self):
        """Получить абсолютный url объекта."""
        return reverse('employee-detail-view', args=[str(self.id)])

    class Meta:
        """Метаописание."""

        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
