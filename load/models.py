from django.db import models
from django.core.validators import MinValueValidator


class Discipline(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Дисциплина")
    objects = models.Manager()  # Он подключается к базе.

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Поток")
    objects = models.Manager()  # Он подключается к базе.

    def __str__(self):
        return self.name


class LoadInfo(models.Model):

    class AcademicYear(models.TextChoices):
        year_23 = ('23/24', '2023/2024')
        year_24 = ('24/25', '2024/2025')
        year_25 = ('25/26', '2025/2026')
        year_26 = ('26/27', '2026/2027')
        year_27 = ('27/28', '2027/2028')
        year_28 = ('28/29', '2028/2029')
        year_29 = ('29/30', '2029/2030')

    academic_year = models.CharField(max_length=5, choices=AcademicYear.choices, verbose_name="Учебный год")

    class Faculty(models.TextChoices):
        faculty_01 = ('ATF', 'АТФ')
        faculty_02 = ('AF', 'АФ')
        faculty_03 = ('WTF', 'ВТФ')
        faculty_04 = ('IPF', 'ИПФ')
        faculty_05 = ('MSF', 'МСФ')
        faculty_06 = ('MTF', 'МТФ')
        faculty_07 = ('PSF', 'ПСФ')
        faculty_08 = ('STF', 'СТФ')
        faculty_09 = ('SF', 'СФ')
        faculty_10 = ('FGDE', 'ФГДЭ')
        faculty_11 = ('FITR', 'ФИТР')
        faculty_12 = ('FMMP', 'ФММП')
        faculty_13 = ('FTUG', 'ФТУГ')
        faculty_14 = ('FTC', 'ФТК')
        faculty_15 = ('FES', 'ФЭС')
        faculty_16 = ('EF', 'ЭФ')
        faculty_17 = ('MIDO', 'МИДО')

    # class Faculty(models.Model):
    #     FACULTY = (
    #         ('ATF', 'АТФ'),
    #         ('AF', 'АФ'),
    #         ('WTF', 'ВТФ'),
    #         ('IPF', 'ИПФ'),
    #         ('MSF', 'МСФ'),
    #         ('MTF', 'МТФ'),
    #         ('PSF', 'ПСФ'),
    #         ('STF', 'СТФ'),
    #         ('SF', 'СФ'),
    #         ('FGDE', 'ФГДЭ'),
    #         ('FITR', 'ФИТР'),
    #         ('FMMP', 'ФММП'),
    #         ('FTUG', 'ФТУГ'),
    #         ('FTC', 'ФТК'),
    #         ('FES', 'ФЭС'),
    #         ('EF', 'ЭФ'),
    #         ('MIDO', 'МИДО'),
    #     )
    #     name = models.CharField(max_length=60)
    #
    #     faculty = models.CharField(max_length=4, choices=FACULTY, verbose_name="Факультет")

    faculty = models.CharField(max_length=4, choices=Faculty.choices, verbose_name="Факультет")

    class Semester(models.TextChoices):
        autumn = ('a', 'осень')
        spring = ('s', 'весна')

    semester = models.CharField(max_length=1, choices=Semester.choices, verbose_name="Семестр")

    class FormStudy(models.TextChoices):
        form_study_01 = ('FT', 'очное')
        form_study_02 = ('C', 'заочное')
        form_study_03 = ('E', 'вечернее')
        form_study_04 = ('MFT', 'магистратура очная')
        form_study_05 = ('MC', 'магистратура заочная')
        form_study_06 = ('PGFT', 'аспирантура очная')
        form_study_07 = ('PGC', 'аспирантура заочная')
        form_study_08 = ('DFT', 'докторантура очная')
        form_study_09 = ('DC', 'докторантура заочная')

    form_study = models.CharField(max_length=4, choices=FormStudy.choices, verbose_name="Форма обучения")

    discipline = models.ForeignKey(Discipline, on_delete=models.PROTECT, verbose_name="Дисциплина")

    class CourseStudy(models.TextChoices):
        course_1 = ('1', '1')
        course_2 = ('2', '2')
        course_3 = ('3', '3')
        course_4 = ('4', '4')
        course_5 = ('5', '5')
        course_6 = ('6', '6')

    course_study = models.CharField(max_length=1, choices=CourseStudy.choices, verbose_name="Курс")

    group = models.ForeignKey(Group, on_delete=models.PROTECT, verbose_name="Поток")

    class Meta:
        db_table = "load_info"
        ordering = ("-academic_year",)

    def __str__(self):
        return f"{self.faculty}_{self.semester}_{self.form_study}= {self.discipline.name}"


class OnDate(models.Model):
    on_date = models.DateField(unique=True, verbose_name="Дата выдачи/уточнения", null=False)
    note = models.CharField(max_length=255, null=True, blank=True, verbose_name="Примечание")
    objects = models.Manager()  # Он подключается к базе.

    def __str__(self):
        date_format = '%d-%m-%Y'
        if not self.on_date:
            str_date = ''
        else:
            str_date = self.on_date.strftime(date_format)
        return str_date


class Load(models.Model):
    load_info = models.ForeignKey(LoadInfo, on_delete=models.PROTECT, verbose_name="Информация о позиции")
    on_date = models.ForeignKey(OnDate, on_delete=models.PROTECT, verbose_name="Дата выдачи/уточнения")
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
        db_table = "load"
        ordering = ("on_date", "id",)
