from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    emplyeeIdentficationCode = models.CharField(max_length=50,default='')
    joining_date = models.DateField(default='')
    phone = models.CharField(max_length=15,default='')
    isAdmin = models.BooleanField(default=False)
    casual_leave_days = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(max_digits=10, decimal_places=2,default = 0.00 ,null = True)
    currency = models.CharField(max_length=3, default='INR')
    medical_leave_days = models.PositiveIntegerField(default=0)
    lop_leave_days = models.PositiveIntegerField(default=0)
    department = models.CharField(max_length=255,default='')
    profilePic = models.ImageField(upload_to='profilePic/', null=True)

    # Module-level permissions for Holidays
    can_read_holidays = models.BooleanField(default=False, null = True)
    can_write_holidays = models.BooleanField(default=False, null = True)
    can_create_holidays = models.BooleanField(default=False, null = True)
    can_delete_holidays = models.BooleanField(default=False, null = True)
    can_import_holidays = models.BooleanField(default=False, null = True)
    can_export_holidays = models.BooleanField(default=False, null = True)

    # Module-level permissions for Leaves
    can_read_leaves = models.BooleanField(default=False, null = True)
    can_write_leaves = models.BooleanField(default=False, null = True)
    can_create_leaves = models.BooleanField(default=False, null = True)
    can_delete_leaves = models.BooleanField(default=False, null = True)
    can_import_leaves = models.BooleanField(default=False, null = True)
    can_export_leaves = models.BooleanField(default=False, null = True)

    # Module-level permissions for Clients
    can_read_clients = models.BooleanField(default=False, null = True)
    can_write_clients = models.BooleanField(default=False, null = True)
    can_create_clients = models.BooleanField(default=False, null = True)
    can_delete_clients = models.BooleanField(default=False, null = True)
    can_import_clients = models.BooleanField(default=False, null = True)
    can_export_clients = models.BooleanField(default=False, null = True)

    # Module-level permissions for Projects
    can_read_projects = models.BooleanField(default=False, null = True)
    can_write_projects = models.BooleanField(default=False, null = True)
    can_create_projects = models.BooleanField(default=False, null = True)
    can_delete_projects = models.BooleanField(default=False, null = True)
    can_import_projects = models.BooleanField(default=False, null = True)
    can_export_projects = models.BooleanField(default=False, null = True)

    # Module-level permissions for Tasks
    can_read_tasks = models.BooleanField(default=False, null = True)
    can_write_tasks = models.BooleanField(default=False, null = True)
    can_create_tasks = models.BooleanField(default=False, null = True)
    can_delete_tasks = models.BooleanField(default=False, null = True)
    can_import_tasks = models.BooleanField(default=False, null = True)
    can_export_tasks = models.BooleanField(default=False, null = True)

    # Module-level permissions for Chats
    can_read_chats = models.BooleanField(default=False, null = True)
    can_write_chats = models.BooleanField(default=False, null = True)
    can_create_chats = models.BooleanField(default=False, null = True)
    can_delete_chats = models.BooleanField(default=False, null = True)
    can_import_chats = models.BooleanField(default=False, null = True)
    can_export_chats = models.BooleanField(default=False, null = True)

    # Module-level permissions for Assets
    can_read_assets = models.BooleanField(default=False, null = True)
    can_create_assets = models.BooleanField(default=False, null = True)
    can_write_assets = models.BooleanField(default=False, null = True)
    can_delete_assets = models.BooleanField(default=False, null = True)
    can_import_assets = models.BooleanField(default=False, null = True)
    can_export_assets = models.BooleanField(default=False, null = True)

    # Module-level permissions for Timing Sheets
    can_read_timing_sheets = models.BooleanField(default=False, null = True)
    can_write_timing_sheets = models.BooleanField(default=False, null = True)
    can_create_timing_sheets = models.BooleanField(default=False, null = True)
    can_delete_timing_sheets = models.BooleanField(default=False, null = True)
    can_import_timing_sheets = models.BooleanField(default=False, null = True)
    can_export_timing_sheets = models.BooleanField(default=False, null = True)


    DESIGNATION_CHOICES = [
        ('des1', 'Designation 01'),
        ('des2', 'Designation 02'),
        ('des3', 'Designation 03'),
        ('des3', 'Designation 04'),
        ('des3', 'Designation 05'),
        ('des3', 'Designation 06'),
        ('des3', 'Designation 07'),
        ('des3', 'Designation 08'),
        ('des3', 'Designation 09'),
        ('des10','Designation 10'),
    ]

    designation = models.CharField(
        max_length=255,
        choices=DESIGNATION_CHOICES,
        default='des1'
    )

    def __str__(self):
        return self.username

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
    

class Leave(models.Model):
    LEAVE_TYPES = [
        ('casual', 'Casual'),
        ('medical', 'Medical'),
        ('lop', 'Loss of Pay'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=10, choices=LEAVE_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.user.username} - {self.leave_type} Leave"
    
class Holiday(models.Model):
    date = models.DateField(unique=True)
    name = models.CharField(max_length=255,default='')

    def __str__(self):
        return self.name
    
# Table added by Nageswara, SaiKiran and D Hari
class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)  # Date of the attendance record
    punch_times = models.JSONField(default=list)  # List to store punch-in and punch-out times
    total_punch_time = models.DurationField(default=timezone.timedelta())  # Total time punched in
    is_holiday = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.date}"