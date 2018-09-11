class RequestHandlerFactoryInterface:

    def get_request_handler(self, request_str):
        if ' ' in request_str:
            command, params_str = request_str.split(' ', maxsplit=1)
            params = params_str.split(' ')
        else:
            command = request_str
            params = []

        return command, params
