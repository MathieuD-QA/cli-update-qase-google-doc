import pygsheets

service_file = "/Users/mathieu/Desktop/cli-qa/cli-update-qase-google-doc/sheet/python-json-307219-1e14b0ea3f8f.json"
gc = pygsheets.authorize(service_file=service_file)
sh = gc.open('PYTHON TEST')
wks = sh.sheet1




class Sheet:
    def __int__(self):
        pass



    def updata_multiple_value(self,payload):
        pourcentage = int(payload['passed']*100/payload['total'])
        print(pourcentage)

        wks.insert_rows(row=1, number=1, values=[payload['id'],payload['title'],payload['description'],payload['status_text'], payload['total'],payload['passed'],payload['failed'],payload['blocked'],payload['in_progress'],pourcentage], inherit=True)  # here wks is the worksheet object


a = Sheet()

