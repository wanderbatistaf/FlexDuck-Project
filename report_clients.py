import csv
import time
import model


__all__ = ["ReportClients"]


class ReportClients(object):
    def __init__(self, *args):
        ...


    def getidreport(self, idcliente, filename):
        mydata = model.Usuarios.select().where(model.Usuarios.idcliente == idcliente).tuples()
        print("Writing to csv: {} ...".format(filename))
        print(mydata)
        csvOut = csv.writer(out)
        headers = [x for x in model.Usuarios._meta.sorted_field_names]
        csvOut.writerow(headers)
        for row in mydata:
            csvOut.writerow(row)
            print(row)

    def writeToCsv(data, filename):
        print("Writing to csv: {} ...".format(filename))
        with open(filename, 'w', newline='') as out:
            csvOut = csv.writer(out)
            headers = [x for x in model.Usuarios._meta.sorted_field_names]
            csvOut.writerow(headers)
            for row in data:
                csvOut.writerow(row)
                data.writeToCsv(mydata, f"{filename}".format(time.time_ns()))