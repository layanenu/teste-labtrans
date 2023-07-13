import tornado.web
import json
from models.result import Result
from models.rodovia import Rodovia
from models.video import Video
import os
from models.model import db
import io

root_dir = os.getcwd()


class UploadHandler(tornado.web.RequestHandler):
    def post(self):
        try:
            files_request = self.request.files["file"]
            data_csv = []
            for f in files_request:
                file_data = io.BytesIO(f.body)
                data_csv.extend(file_data.read().decode().splitlines())
            km_inicial = 0
            km_final = 0
            chunk_size = 2000
            with db.atomic() as transaction:
                for chunk_start in range(0, len(data_csv), chunk_size):
                    chunk_end = min(chunk_start + chunk_size, len(data_csv))
                    data_highway_chunk = []
                    for i in range(chunk_start, chunk_end):
                    
                        result = data_csv[i].split(',')
                        name_video = result[0]
                        highway = result[3]
                    
                        if i != chunk_start:
                            object_result = {
                                'name': result[0],
                                'highway': result[3],
                                'km': result[1],
                                'distance': result[2],
                                'item': result[4].lower(),
                            }
                            data_highway_chunk.append(object_result)

                            if i == chunk_start + 1:
                                km_inicial = float(result[1])
                                km_final = float(result[1])
                            else:
                                km_inicial = min(km_inicial, float(result[1]))
                                km_final = max(km_final, float(result[1]))

                    Result.insert_many(data_highway_chunk).execute()
                db.execute_sql('DROP VIEW IF EXISTS vw_results;')
                db.execute_sql('CREATE VIEW vw_results AS '
                                'SELECT id, highway, km, '
                                'SUM(item = \'buraco\') AS buraco, '
                                'SUM(item = \'remendo\') AS remendo, '
                                'SUM(item = \'trinca\') AS trinca, '
                                'SUM(item = \'placa\') AS placa, '
                                'SUM(item = \'drenagem\') AS drenagem '
                                'FROM results '
                                'GROUP BY km, highway;')
                Video.insert(
                    name=name_video, km_inicial=km_inicial,
                    km_final=km_final).execute()
                Rodovia.insert(highway=highway, km_inicial=km_inicial, 
                               km_final=km_final).execute()
                transaction.commit()

            self.write(json.dumps({"message": "The data was added!"}))
        except Exception as e:
            transaction.rollback()
            print(e)
            self.set_status(500)
            self.write(json.dumps(
                {"erro": "An internal error occurred on the server"}))
