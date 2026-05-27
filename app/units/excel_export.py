import pandas as pd

def export_excel(data):

    df = pd.DataFrame(data)

    df.to_excel(
        'students.xlsx',
        index=False
    )