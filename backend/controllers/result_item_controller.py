import tornado.web
from models.vw_result import VwResult
import csv
from peewee import fn
import json


class ResultItemController(tornado.web.RequestHandler):
    def get(self):
        item_value = self.get_argument('item', default=None)
        results = None
        
        switcher = {
          'buraco': 'buraco',
          'remendo': 'remendo',
          'trinca': 'trinca',
          'placa': 'placa',
          'drenagem': 'drenagem'
        }
        max_item_name = switcher.get(item_value, None)
        max_item = getattr(VwResult, max_item_name, None)
        result = VwResult.select(
            VwResult.highway, 
            VwResult.km,
            fn.MAX(max_item),
        ).group_by(VwResult.km).order_by(fn.MAX(max_item).desc()
        ).limit(1).first()
        if result:
            result_dict = {
                'highway': result.highway,
                'km': result.km,
            }
            if max_item_name and max_item:
                max_item_value = getattr(result, max_item_name)
                result_dict[item_value] = max_item_value
            self.write(json.dumps(result_dict))
        else:
            self.write(json.dumps({}))