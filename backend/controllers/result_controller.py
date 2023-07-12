import tornado.web
import json
from models.result import Result
from models.vw_result import VwResult
from models.rodovia import Rodovia
from models.video import Video
import os
from peewee import fn
from models.model import db


root_dir = os.getcwd()


class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        files_request = self.request.files["file"]
        for f in files_request:
            files_path = os.path.join(root_dir, "tmp", f.filename)
            fh = open(f"{files_path}", "wb")
            fh.write(f.body)
            fh.close()
        file_read = open(f"{files_path}", "r")
        data_csv = file_read.read().splitlines()
        file_read.close()

        data_highway = []
        km_inicial = 0
        km_final = 0
        chunk_size = 2000
        for chunk_start in range(0, len(data_csv), chunk_size):
            chunk_end = min(chunk_start + chunk_size, len(data_csv))
            data_highway_chunk = []
            
            for i in range(chunk_start, chunk_end):
                object_highway = {
                    'highway': '',
                    'km': 0,
                    'buraco': 0,
                    'remendo': 0,
                    'trinca': 0,
                    'placa': 0,
                    'drenagem': 0
                }
                result = data_csv[i].split(',')
                name_video = result[0]
                highway = result[3]
                item = result[4].lower()

                if i != chunk_start:
                    object_highway['highway'] = result[3]
                    object_highway['km'] = float(result[1])
                    object_highway[item] = 1
                    data_highway_chunk.append(object_highway)

                    if i == chunk_start + 1:
                        km_inicial = float(result[1])
                        km_final = float(result[1])
                    else:
                        if km_inicial > float(result[1]):
                            km_inicial = float(result[1])
                        if km_final < float(result[1]):
                            km_final = float(result[1])
            Result.insert_many(data_highway_chunk).execute()

        db.execute_sql('DROP VIEW IF EXISTS vwResult;')
        db.execute_sql('CREATE VIEW vwResult AS select id, highway, km, sum(buraco) as buraco, sum(remendo) as remendo, sum(trinca) as trinca, sum(placa) as placa, sum(drenagem) as drenagem from result GROUP by km, highway;')
        Video.insert(
            name=name_video, km_inicial=km_inicial,
            km_final=km_final).execute()
        Rodovia.insert(highway=highway, km_inicial=km_inicial,
            km_final=km_final).execute()
        os.remove(files_path)
        self.write(json.dumps({"message": "The data was added!"}))
        # self.write(json.dumps(data_highway_chunk))
