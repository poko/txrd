#stlib
import datetime
#from datetime import timedelta

#Django
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BaseModel(models.Model):
    created_date = models.DateTimeField(default=datetime.datetime.utcnow)
    last_modified = models.DateTimeField(default=datetime.datetime.utcnow)

    class Meta:
        abstract = True

    @property
    def dict(self):
        ret = self.__dict__
        return dict((k,v) for k,v in ret.items() if not k.startswith('_'))
    
class Division(models.Model):
#     BUS = "business"
#     OPS = "ops"
#     HR = "hr"
#     PERF = "performance"
#     MKTG = "mktg"
#     DIVISION_TYPES = (
#         (BUS,'Business'),
#         (OPS, 'Operations'),
#         (HR, 'Human Resourses'),
#         (PERF, 'Performance'),
#         (MKTG, 'Marketing')
#     )
    division =  models.CharField('Division', max_length=64)
    
    def __init__(self, div_name):
        self.division = div_name
    
    def __unicode__(self):
        return self.division
    
#Division definitions
DIV_BUS = Division('Business')   
DIV_OPS = Division('Operations')   
DIV_HR = Division('Human Resources')   
DIV_PERF = Division('Performace')   
DIV_MKTG = Division('Marketing')  

#Depts
#business
DEPT_BUS_BUS = 'bus'
DEPT_BUS_ACCT = "acct"
DEPT_BUS_FAC = "fac"
DEPT_BUS_SPONS = "spons"
DEPT_BUS_ARCH = "archives"
#ops
DEPT_OPS_OPS = "ops"
DEPT_OPS_MEDIA = "media"
DEPT_OPS_MERCH = "merch"
DEPT_OPS_PROD = "prod"
DEPT_OPS_TIX = "tix"
#hr
DEPT_HR_HR = "hr"
DEPT_HR_CAPS = "captains"

#performance
DEPT_PERF_PERF = "perf"
DEPT_PERF_TR = "training"

#marketing
DEPT_MKTG_MK = "marketing"
DEPT_MKTG_WEB = "web"
DEPT_MKTG_PR = "pr"
DEPT_MKTG_ART = "art"
    

DEPT_PARAMS = {
    DEPT_BUS_BUS:   {'division': DIV_BUS},
    DEPT_BUS_ACCT:  {'division': DIV_BUS},
    DEPT_BUS_FAC:   {'division': DIV_BUS},
    DEPT_BUS_SPONS: {'division': DIV_BUS},
    DEPT_BUS_ARCH:  {'division': DIV_BUS},
    DEPT_OPS_OPS:   {'division': DIV_OPS},
    DEPT_OPS_PROD:  {'division': DIV_OPS},
    DEPT_OPS_TIX:   {'division': DIV_OPS},
    DEPT_OPS_MERCH: {'division': DIV_OPS},
    DEPT_OPS_MEDIA: {'division': DIV_OPS},
    DEPT_HR_HR:     {'division': DIV_HR},
    DEPT_HR_CAPS:   {'division': DIV_HR},
    DEPT_PERF_PERF: {'division': DIV_PERF},
    DEPT_PERF_TR:   {'division': DIV_PERF},
    DEPT_MKTG_MK:   {'division': DIV_MKTG},
    DEPT_MKTG_ART:  {'division': DIV_MKTG},
    DEPT_MKTG_PR:   {'division': DIV_MKTG},
    DEPT_MKTG_WEB:  {'division': DIV_MKTG},
}
    
class LeagueJob(models.Model):
   
    DEPT_TYPES = (
                  (DIV_BUS, (
                         (DEPT_BUS_BUS, 'Business'),
                         (DEPT_BUS_ACCT, 'Accounting'),
                         (DEPT_BUS_FAC, 'Facilities'),
                         (DEPT_BUS_SPONS, 'Sponsorship'),
                         (DEPT_BUS_ARCH, 'Archives'),
                         )
                   ),
                  (DIV_OPS, (
                         (DEPT_OPS_OPS, 'Operations'),
                         (DEPT_OPS_PROD, 'Production'),
                         (DEPT_OPS_TIX, 'Tickets'),
                         (DEPT_OPS_MERCH, 'Merch'),
                         (DEPT_OPS_MEDIA, 'Media'),
                         )
                   ),
                  (DIV_HR, (
                         (DEPT_HR_HR, 'HR'),
                         (DEPT_HR_CAPS, 'Captains'),
                         )
                   ),
                (DIV_PERF, (
                       (DEPT_PERF_PERF, 'Performance'),
                       (DEPT_PERF_TR, 'Training'),
                       )
                 ),
                (DIV_MKTG, (
                       (DEPT_MKTG_MK, 'Marketing'),
                       (DEPT_MKTG_ART, 'Art'),
                       (DEPT_MKTG_PR, 'PR'),
                       (DEPT_MKTG_WEB, 'Web'),
                       )
                 ),
    )
    title = models.CharField(max_length=512)
    department = models.CharField('Department', max_length=64, choices=DEPT_TYPES)
    monthly_points = models.DecimalField('Points per month', max_digits=5, decimal_places=2)
    
    def job_division(self):
        return DEPT_PARAMS[self.department]['division']
    division = property(job_division)

    def __unicode__(self):
        return self.title
    
    
class MemberProfile(models.Model):
    SKATER = "skater"
    NSM = "nsm"
    PRODUCTION = "production"
    MEMBERSHIP_TYPES = (
        (SKATER,'Skater'),
        (NSM, 'Non-Skating Member'),
        (PRODUCTION, 'Production')
    )
    user = models.OneToOneField(User)
    membership_type = models.CharField('Membership Type', max_length=64, choices=MEMBERSHIP_TYPES, default=SKATER, blank=False)
    given_first_name = models.CharField('First Name', max_length=512, blank=False)
    given_last_name = models.CharField('Last Name', max_length=512, blank=False)
    skate_name = models.CharField('Skate Name', max_length=512, blank=True)
    dob = models.DateField('Date of Birth', blank=False)
    ssn = models.CharField('Social Sec #', max_length=64, blank=False)
    phone = models.CharField('Phone Number', max_length=64, blank=False)
    notes = models.TextField(max_length=500, blank=True)
    txrd_email = models.EmailField('TXRD Email', max_length=512, blank=False)
    personal_email = models.EmailField('Personal Email', max_length=512, blank=False)
    jobs = models.ManyToManyField(LeagueJob, blank=True)
    
    def exactTenure(self):
        dates = TenureDate.objects.filter(member=self.id)
        total_tenure = datetime.timedelta(days=0)
        for date in dates:
            if date.end_date is None:
                date.end_date = datetime.date.today()
            diff = date.end_date - date.start_date
            total_tenure = total_tenure + diff
        return total_tenure
    
    def readableTenure(self):
        total_tenure = self.exactTenure()
        #TODO does leave count against tenure? 
        #military does, iloa does, sabatical does not
        if total_tenure.days > 365:
            return str.format("{0} years, {1} months, {2} days", total_tenure.days / 365, (total_tenure.days % 365) / 30, (total_tenure.days % 365) % 30)
        else:
            if total_tenure.days > 30:
                return str.format("{0} months, {1} days", (total_tenure.days % 365) / 30, (total_tenure.days % 365) % 30)
        return str.format("{0} days", total_tenure.days);
    approx_tenure = property(readableTenure)
    exact_tenure = property(exactTenure)
    
    def points_for_date(self, current_date=datetime.date.today()):
        points = MembershipPoint.objects.filter(member=self.id, date__year=current_date.year, date__month=current_date.month)
        return points;
    
    def display_name(self):
        name = self.skate_name
        if name is None:
            name = self.member.given_first_name + " " + self.given_last_name
        return name
    
    def __unicode__(self):
        if self.skate_name:
            return self.skate_name
        else:
            return self.given_last_name + ", " + self.given_first_name
    
class MemberAddress(models.Model):    
    class Meta:
        verbose_name_plural = "member addresses"
    member = models.ForeignKey(MemberProfile)
    address_line_1 = models.CharField('Address Line 1', max_length=512, blank=False)
    address_line_2 = models.CharField('Address Line 2', max_length=512, blank=True)
    city = models.CharField(max_length=512, blank=False, default="Austin")
    state = models.CharField(max_length=2, blank=False, default="TX")
    zip_code = models.CharField(max_length=15, blank=False)
    
    def __unicode__(self):
        return self.address_line_1 + "\n" + self.address_line_2 + "\n" + self.zip_code
    
class TenureDate(models.Model):
    member = models.ForeignKey(MemberProfile)
    start_date = models.DateField('Tenure Start Date', blank=False)
    end_date = models.DateField('Tenure Retirement Date', blank=True, null=True)
    
    #TODO ensure start date is after end date
    
    def __unicode__(self):
        fmt = "{0}'s tenure starting {1} and ending {2}"
        return str.format(fmt, self.member.display_name(), self.start_date, self.end_date)

    
class MembershipPoint(models.Model):
    member = models.ForeignKey(MemberProfile)
    date = models.DateField('Date', blank=False)
    value = models.DecimalField('Point Value', max_digits=5, decimal_places=2, blank=False)
    note = models.CharField(max_length=512, blank=False)
    
    def __unicode__(self):
        fmt = "{2} Point(s) for {0} on {1}"
        return str.format(fmt, self.member.display_name(), self.date, self.value)
    
class Penalty(models.Model):
    class Meta:
        verbose_name_plural = "penalties"
        
    MAJOR = "major"
    MINOR = "minor"
    PENALTY_TYPES = (
        (MAJOR, 'Major'),
        (MINOR, 'Minor'),
    ) 
    member = models.ForeignKey(MemberProfile)
    type = models.CharField('Penalty Type', max_length=64, choices=PENALTY_TYPES, default=MINOR, blank=False)
    date = models.DateField('Date', blank=False)
    infraction = models.CharField('Infraction', max_length=512, blank=False)
    note = models.CharField('Notes', max_length=1024, blank=False)
    
    def __unicode__(self):
        fmt = "{0}'s {1} Penalty on {2} for {3}"
        return str.format(fmt, self.member.display_name(), self.type, self.date, self.infraction)
    
    
class LeaveOfAbsence(models.Model):
    SAB = "sabbatical"
    ILOA = "iloa"
    MIL = "military"
    NKOTB = "knotb"
    PENALTY_TYPES = (
        (SAB, 'Sabbatical'),
        (ILOA, 'Injured Leave of Absence'),
        (MIL, 'Military'),
        (NKOTB, 'New Kid on the Block'),
    )
    member = models.ForeignKey(MemberProfile)
    type = models.CharField('Leave Type', max_length=64, choices=PENALTY_TYPES, default=SAB, blank=False)
    start_date = models.DateField('Start Date', blank=False)
    end_date = models.DateField('End Date', blank=True, null=True)
    
    def __unicode__(self):
        fmt = "{0}'s {1} leave starting on {2}"
        if self.end_date is not None:
            fmt = "{0}'s {1} leave starting on {2} ending on {3}"
        return str.format(fmt, self.member.display_name(), self.type, self.start_date, self.end_date)

