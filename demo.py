from us_visa.logger import logging
import sys
from us_visa.exception import US_VisaErrorException

try:
    a = 1/"a"
except Exception as e:
    raise US_VisaErrorException(e, sys) from e