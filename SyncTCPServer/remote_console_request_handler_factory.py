from SyncTCPServer.RequestHandler import echo_request_handler, date_request_handler, exit_request_handler, \
    file_upload_request_handler, file_download_request_handler, unknown_request_handler
from SyncTCPServer.request_handler_factory_interface import RequestHandlerFactoryInterface


class RemoteConsoleRequestHandlerFactory(RequestHandlerFactoryInterface):

    def get_request_handler(self, request_str):
        command, params = super().get_request_handler(request_str)
        handlers_dict = {
            "echo": echo_request_handler.EchoRequestHandler,
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
        return request_handler_creator(params)

    @staticmethod
    def get_echo_request_handler(params):
        return echo_request_handler.EchoRequestHandler(params)

    @staticmethod
    def get_date_request_handler(params):
        return date_request_handler.DateRequestHandler(params)

    @staticmethod
    def get_exit_request_handler(params):
        return exit_request_handler.ExitRequestHandler(params)

    @staticmethod
    def get_file_upload_request_handler(params):
        return file_upload_request_handler.FileUploadRequestHandler(params)

    @staticmethod
    def get_file_download_request_handler(params):
        return file_download_request_handler.FileDownloadRequestHandler(params)

    @staticmethod
    def get_unknown_request_handler(params):
        return unknown_request_handler.UnknownRequestHandler(params)

