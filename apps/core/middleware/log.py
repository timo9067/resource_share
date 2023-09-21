import logging
from datetime import datetime

# Get the logging instance

logger = logging.getLogger('logging_mw') # __name__ - logging_middle_ware

def simple_logging_middleware(get_response):
    def middleware(request):
        
        # date_time = datetime.now()
        http_method = request.method
        url= request.get_full_path()
        host_port = request.get_host()
        content_type = request.headers["Content-Type"]
        user_agent = request.headers["User-Agent"]
        
        msg = f"{http_method} | {host_port}{url} | {content_type} | {user_agent}"
        
        response = get_response(request)
        
        logger.info(msg)
        #TODO: Investifate the response
        
        
        
        return response
    
    return middleware
