import shutil
from datetime import datetime

def backup_database():

    now = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    shutil.copy(
        'attendance.db',
        f'backup_{now}.db'
    )