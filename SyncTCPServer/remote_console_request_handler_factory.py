import RequestHandler.unknown_request_handler
import RequestHandler.date_request_handler
import RequestHandler.echo_request_handler
import RequestHandler.exit_request_handler
import RequestHandler.file_download_request_handler
import RequestHandler.file_upload_request_handler
from request_handler_factory_interface import RequestHandlerFactoryInterface


class RemoteConsoleRequestHandlerFactory(RequestHandlerFactoryInterface):

    def get_request_handler(self, request_str):
        command, data = super().parse_request_handler(request_str)
        handlers_dict = {
            "echo": RemoteConsoleRequestHandlerFactory.get_echo_request_handler,
            "date": RemoteConsoleRequestHandlerFactory.get_date_request_handler,
            "exit": RemoteConsoleRequestHandlerFactory.get_exit_request_handler,
            "upload": RemoteConsoleRequestHandlerFactory.get_file_upload_request_handler,
            "download": RemoteConsoleRequestHandlerFactory.get_file_download_request_handler,
            "unknown": RemoteConsoleRequestHandlerFactory.get_unknown_request_handler
        }       
        try:
            request_handler_creator = handlers_dict[command]
        except KeyError:
            request_handler_creator = handlers_dict["unknown"]
        return request_handler_creator(data)

    @staticmethod
    def get_echo_request_handler(params):
        return RequestHandler.echo_request_handler.EchoRequestHandler(params)

    @staticmethod
    def get_date_request_handler(params):
        return RequestHandler.date_request_handler.DateRequestHandler(params)

    @staticmethod
    def get_exit_request_handler(params):
        return RequestHandler.exit_request_handler.ExitRequestHandler(params)

    @staticmethod
    def get_file_upload_request_handler(params):
        return RequestHandler.file_upload_request_handler.FileUploadRequestHandler(params)

    @staticmethod
    def get_file_download_request_handler(params):
        return RequestHandler.file_download_request_handler.FileDownloadRequestHandler(params)

    @staticmethod
    def get_unknown_request_handler(params):
        return RequestHandler.unknown_request_handler.UnknownRequestHandler(params)

