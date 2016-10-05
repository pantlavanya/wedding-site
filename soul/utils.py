from django.http import HttpResponse
from django.core import serializers

def export_csv(modeladmin, request, queryset):
    if not request.user.has_perm('polls.export_csv_poll'):
        messages.success(request, 'no permission! to export in csv')
        return 0
    import csv
    from django.utils.encoding import smart_str
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=mymodel.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
        smart_str(u"ID"),
        ])
    for obj in queryset:
        writer.writerow([
        smart_str(obj.pk),
        ])
    return response
    export_csv.short_description = u"Export CSV"

def export_as_json(modeladmin, request, queryset):
    response = HttpResponse(content_type="application/json")
    serializers.serialize("json", queryset, stream=response)
    return response

def export_as_xml(modeladmin, request, queryset):
    response = HttpResponse(content_type="application/xml")
    serializers.serialize("xml", queryset, stream=response)
    return response

def export_as_xlsx(modeladmin, request, queryset):
    import xlsxwriter
    response = HttpResponse(content_type='text/xlsx')
    workbook = xlsxwriter.Workbook('hello_world.xlsx')
    worksheet = workbook.add_worksheet()
    i=1
    for obj in queryset:
        worksheet.write('A'+str(i), obj.pkp)
        i=i+1
    workbook.close()