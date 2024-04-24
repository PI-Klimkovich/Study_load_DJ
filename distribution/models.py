from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth import get_user_model
from load.models import Load


class Distribution(models.Model):
    load = models.ForeignKey(Load, on_delete=models.PROTECT, verbose_name="Позиция нагрузки")
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name="Преподаватель")
    lectures = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=0,
        verbose_name="Лекции",
    )
    laboratory = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=0,
        verbose_name="Лабораторные",
    )
    practical = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=0,
        verbose_name="Практические",
    )
    course_work = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=0,
        verbose_name="Курсовые работы (проекты)",
    )
    calculation_and_graphic_works = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=0,
        verbose_name="РГР",
    )
    control = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=0,
        verbose_name="Контрольные",
    )
    consultations = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=0,
        verbose_name="Консультации",
    )
    tests = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=0,
        verbose_name="Зачеты",
    )
    exams = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=0,
        verbose_name="Экзамены",
    )
    diploma = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=0,
        verbose_name="Диплом",
    )
    state_exam = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=0,
        verbose_name="ГЭК",
    )
    practice = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=0,
        verbose_name="Практика",
    )
    postgraduate_studies = models.IntegerField(
        validators=[MinValueValidator(0)],
        default=0,
        verbose_name="Аспирантура",
    )
    total = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=0,
        verbose_name="Итого",
    )
    note = models.CharField(max_length=255, null=True, blank=True, verbose_name="Примечание")

    class Meta:
        db_table = "distribution"
        # ordering = ("-on_date",)

    def save(self):
        self.total = (
                self.lectures
                + self.laboratory
                + self.practical
                + self.course_work
                + self.calculation_and_graphic_works
                + self.control
                + self.consultations
                + self.tests
                + self.exams
                + self.diploma
                + self.state_exam
                + self.practice
                + self.postgraduate_studies
        )
        return super().save()
