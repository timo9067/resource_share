from .utils import MetaSingleton
from enum import Enum

class LevelEnum(Enum):
    info = "INFO"
    critical = "CRITICAL"
    error = "ERROR"
    warning = "WARNING"
    

class Logging(metaclass=MetaSingleton):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        
    def _write_log(self, level: LevelEnum, msg: str) -> None: 
        """Write to the log file"""
        
        with open(self.file_name, "a") as log_file:
            log_file.write(f"[{level.name}] {msg}\n") # [INFO], [CRITICAL] message goes here
            
    # create level specific methods
    def info(self, msg): 
        self._write_log(LevelEnum.info, msg)
    
    # my part
    def critical(self, msg): 
        self._write_log(LevelEnum.critical, msg)
    def error(self, msg): 
        self._write_log(LevelEnum.error, msg)
    def warning(self, msg): 
        self._write_log(LevelEnum.warning, msg)

    # TODO: Add more level specific methods
    # CRITICAL
    # ERROR
    # WARNING
    
    