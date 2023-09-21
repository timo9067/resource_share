def printing_middleware(get_response):
    def middleware(request):
        # pre-processing
        print("This is a preprocessing message")
        
        response = get_response(request)
        
        # post-processing
        print("This is a postprocessing message")
        
        return response
    return middleware