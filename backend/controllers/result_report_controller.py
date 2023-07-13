import tornado.web
from models.vw_result import VwResult
import csv
from peewee import fn


class ResultReportController(tornado.web.RequestHandler):
    def get(self):
        highway_value = self.get_argument('highway', default=None)
        results = VwResult.select(
              VwResult.highway, 
              VwResult.km,
              fn.Sum(VwResult.buraco).alias('buraco'),
              fn.Sum(VwResult.remendo).alias('remendo'),
              fn.Sum(VwResult.trinca).alias('trinca'),
              fn.Sum(VwResult.placa).alias('placa'),
              fn.Sum(VwResult.drenagem).alias('drenagem'),
              )
        if highway_value is not None:
            results = results.where(VwResult.highway == highway_value)
            results = results.group_by(VwResult.km, VwResult.highway).execute()

        self.set_header('Content-Type', 'text/csv')
        self.set_header(
            'Content-Disposition', 'attachment; filename="dados.csv"')
        writer = csv.writer(self)
        writer.writerow([
            'highway', 'km', 'buraco', 'remendo', 'trinca', 'placa', 'drenagem'
            ])

        for result in results:
            row = [result.highway, result.km, result.buraco, result
                   .remendo, result.trinca, result.placa, result.drenagem]
            writer.writerow(row)
