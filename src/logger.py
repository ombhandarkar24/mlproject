import logging 
import os
from datetime import datetime

Log_File = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
Log_Path = os.path.join(os.getcwd(),"Logs",Log_File)
os.makedirs(Log_Path,exist_ok=True)

Log_File_Path = os.path.join(Log_Path,Log_File)

logging.basicConfig(
    
    filename=Log_File_Path,
    format="[ %(asctime)s ] %(lineno)d %(name)s -%(levelname)s -%(message)s",
    level=logging.INFO,
)

