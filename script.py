from googleplaces import GooglePlaces
import xlwt

MAPS_API_KEY = ""  	#Insert Maps API key here
locations = ['Chandigarh','Mohali','Panchkula'] #Add the names of different locations here
google_places = GooglePlaces(MAPS_API_KEY)
workBook = xlwt.Workbook()

for loc in locations:
    query_result = google_places.nearby_search(location= loc, keyword= 'pediatrician', radius= 5000, type= 'health') #In keyword
    row = 1
    if query_result.has_attributions:
        print query_result.html_attributions

    workSheet = wb.add_sheet(loc)
    style = xlwt.easyxf('font: bold on')
    workSheet.write(0, 0, 'NAME', style)
    workSheet.write(0, 1, 'CONTACT NO.', style)
    workSheet.write(0, 2, 'ADDRESS', style)
    for place in query_result.places:
        place.get_details()
        workSheet.write(row, 0, place.name)
        workSheet.write(row, 1, place.local_phone_number)
        workSheet.write(row, 2, place.details.get('vicinity'))
        row += 1
workBook.save('pediatrician.xls')

#additional pages
#if query_result.has_next_page_token:
#    query_result_next_page = google_places.nearby_search(
#            pagetoken=query_result.next_page_token)