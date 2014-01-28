from django.contrib import admin
from txrd.models import MemberProfile, MemberAddress, TenureDate, MembershipPoint, LeagueJob, Penalty, LeaveOfAbsence

#Inlines
class AddressInline(admin.StackedInline):
    model = MemberAddress
    extra = 1

class TenureInline(admin.StackedInline):
    model = TenureDate
    extra = 1

#Admins
class MemberProfileAdmin(admin.ModelAdmin):
    list_display = ('skate_name', 'given_first_name', 'given_last_name', 'approx_tenure', 'exact_tenure', 'ssn', 'phone')
    search_fields = ('given_first_name', 'given_last_name', 'skate_name')
    inlines = [AddressInline, TenureInline]
    list_filter = ('skate_name', 'given_first_name')
    
class LeagueJobAdmin(admin.ModelAdmin):
    list_display = ('title', 'division', 'department', 'monthly_points')
    search_fields = ('department', 'title')
    list_filter = ('department', 'title')
    
class LeaveAdmin(admin.ModelAdmin):
    list_display = ('member', 'type', 'start_date', 'end_date')
    search_fields = ('member', 'type')
    list_filter = ('member', 'type', 'start_date', 'end_date')
    
class AddressAdmin(admin.ModelAdmin):
    list_display = ('member', 'address_line_1', 'address_line_2', 'city', 'state', 'zip_code')
    search_fields = ('member', 'address_line_1', 'city')
    list_filter = ('member', 'city')
    
class MembershipPointAdmin(admin.ModelAdmin):
    list_display = ('member', 'date', 'value', 'note')
    search_fields = ('member', )
    list_filter = ('member', 'date')
    
#Registrations
admin.site.register(MemberProfile, MemberProfileAdmin)
admin.site.register(MemberAddress, AddressAdmin)
admin.site.register(TenureDate)
admin.site.register(MembershipPoint, MembershipPointAdmin)
admin.site.register(LeagueJob, LeagueJobAdmin)
admin.site.register(Penalty)
admin.site.register(LeaveOfAbsence, LeaveAdmin)

