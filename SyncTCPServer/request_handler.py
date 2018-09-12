from SyncTCPServer.request_handler_factory_interface import RequestHandlerFactoryInterface
import datetime

class request_handler(RequestHandlerFactoryInterface):

    def get_ansver(self, request_str):
        command, params = super().get_request_handler(request_str)
        handlers_dict = {
            "echo": request_handler.get_echo_answer,
            "date": request_handler.get_date_answer,
            "exit": request_handler.get_exit_answer
        }
        try:
            request_handler_creator = handlers_dict[command]
        except KeyError:
            request_handler_creator = handlers_dict['echo']
        return request_handler_creator(params)[0]

    @staticmethod
    def get_echo_answer(param):
        return param

    @staticmethod
    def get_date_answer(param):
        return str(datetime.datetime.now())

    @staticmethod
    def get_exit_answer(param):
        return 'exit'

