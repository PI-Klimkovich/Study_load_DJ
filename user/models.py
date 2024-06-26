from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils import timezone


def upload_to(instance: "User", filename: str) -> str:
    """Путь для файла относительно корня медиа хранилища."""
    return f"{instance.username}/{filename}"


class User(AbstractUser):
    """
    Наследуем все поля из `AbstractUser`
    Добавляем новые поля
    """
    # email = models.EmailField(verbose_name="email")
    # last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    # first_name = models.CharField(max_length=255, verbose_name="Имя")

    middle_name = models.CharField(max_length=255, null=True, blank=True, default='', verbose_name="Отчество")
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name="Телефон")
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name="Адрес")
    birthday = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    photo = models.ImageField(upload_to=upload_to, null=True, blank=True, verbose_name="Превью")
    description = models.TextField(null=True, blank=True, verbose_name="Краткие сведения")
    is_member = models.BooleanField(default=False, verbose_name="Сотрудник")

    # surname_f_m = models.CharField(max_length=255, verbose_name="Фамилия И.О.")
    # job_title = models.ForeignKey(JobTitle, on_delete=models.PROTECT, verbose_name="Должность")
    # academic_degree = models.ForeignKey(AcademicDegree, on_delete=models.PROTECT, verbose_name="Степень")
    # academic_title = models.ForeignKey(AcademicTitle, on_delete=models.PROTECT, verbose_name="Звание")

    class Meta:
        db_table = "users"
        # ordering = ("-created_at",)

    def __str__(self):
        return self.last_name + ' ' + self.first_name


class Titles(models.Model):
    assignment_date = models.DateField(verbose_name="Дата назначения")
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name="Преподаватель")

    class JobTitle(models.TextChoices):
        head_of_department = ('HD', 'Заведующий кафедрой')
        professor = ('P', 'Профессор')
        docent = ('D', 'Доцент')
        senior_lecturer = ('SL', 'Старший преподаватель')
        teacher = ('T', 'Преподаватель')
        assistant = ('A', 'Ассистент')
        trainee_teacher = ('TT', 'Преподаватель-стажер')
        engineer = ('En', 'Инженер')
        technician = ('Te', 'Техник')
        default = ('-', '-')

    job_title = models.CharField(
        max_length=2,
        choices=JobTitle.choices,
        verbose_name="Должность",
        default='-'
    )

    class AcademicDegree(models.TextChoices):
        doctor = ('D', 'Доктор')
        candidate_of_sciences = ('C', 'Кандидат')
        master = ('M', 'Магистр')
        default = ('-', '-')

    academic_degree = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        choices=AcademicDegree.choices,
        verbose_name="Степень",
        default='-')

    class AcademicTitle(models.TextChoices):
        professor = ('P', 'Профессор')
        docent = ('D', 'Доцент')
        default = ('-', '-')

    academic_title = models.CharField(
        max_length=1,
        null=True,
        blank=True,
        choices=AcademicTitle.choices,
        verbose_name="Звание",
        default='-'
    )

    class Meta:
        db_table = "titles"
        ordering = ("-assignment_date",)

    @property
    def verbose_job_title(self) -> str:
        for value, label in self.JobTitle.choices:
            if value == self.job_title:
                return label
        return "Unknown job title"

    @property
    def verbose_academic_degree(self) -> str:
        for value, label in self.AcademicDegree.choices:
            if value == self.academic_degree:
                return label
        return "Unknown academic degree"

    @property
    def verbose_academic_title(self) -> str:
        for value, label in self.AcademicTitle.choices:
            if value == self.academic_title:
                return label
        return "Unknown academic title"
