import pandas as pd
import pywhatkit
import time
import pyautogui

message = """
Hola {Tienda}
Soy Miguel Pazos analista de Devoluciones del area de Fullfilment - Postventa


*Tracking*        
{rows}

estoy atento a cualquier incoveniente

"""

row = """{Tracking}         
"""
# Assuming the country code for your numbers is '+51' (change it according to your needs)
country_code = '+51'

data_df = pd.read_excel(r'~\Downloads\Lista_cliente_whastapp.xlsx', dtype={"Celular": str})
cliente_list = data_df["ID"]
unique_cliente_list = list(dict.fromkeys(cliente_list))
for cliente in unique_cliente_list:
    cliente_info = data_df[data_df["ID"] == cliente]
    table_rows = cliente_info[["ID", "cliente", "Tracking"]]
    rows = ""
    for i in range(table_rows.shape[0]):
        rows += row.format(
            ID=table_rows["ID"].iloc[i],
            cliente=table_rows["cliente"].iloc[i],
            Tracking=table_rows["Tracking"].iloc[i]
        )
    formatted_message = message.format(
        ID=cliente_info["ID"].iloc[0],
        cliente=cliente_info["cliente"].iloc[0],
        rows=rows
    )
    # Add the country code to the phone number
    phone_number = country_code + cliente_info["Celular"].iloc[0]
    pywhatkit.sendwhatmsg_instantly(phone_number, formatted_message)
    time.sleep(12)
    pyautogui.press('enter')
