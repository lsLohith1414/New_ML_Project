import sys


def error_message_details(error,error_details:sys):
    exc_name,exc_type,exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = f"Error occur in python script name {file_name} in the line {exc_tb.tb_lineno} and error message is {str(error)}"
    return error_message



class custom_exception(Exception):
    def __init__(self, error, error_details:sys):
        super().__init__(error)
        self.error_message = error_message_details(error,error_details) 

    def __str__(self):
        return str(self.error_message)    