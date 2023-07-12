import tornado.ioloop
import tornado.web
from controllers.result_controller import UploadHandler
from controllers.result_report_controller import ResultReportController
from controllers.result_item_controller import ResultItemController
from models.result import Result


if __name__ == "__main__":    
    app = tornado.web.Application([
        (r"/result", UploadHandler),
        (r"/result/report", ResultReportController),
        (r"/result/item", ResultItemController)
    ])
    port = 8882
    app.listen(port)
    print(f"Aplication is ready and listening on port {port}")
    tornado.ioloop.IOLoop.current().start()