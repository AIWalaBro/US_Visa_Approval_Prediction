import os
import sys


def error_message_detail(error, error_detail:sys):
    _,_,exc_tab = error_detail.exc_info()
    file_name = exc_tab.tb_frame.f_code.co_filename
    error_message = "Error Occured in Python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tab.tb_lineno, str(error)
    )
    return error_message

    
    
class US_VisaErrorException (Exception):
    def __init__(self, error_message, error_detail):
        """
        parameter error_message: error message in string format
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail = error_detail
        )
    