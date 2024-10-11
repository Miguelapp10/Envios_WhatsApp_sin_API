import pywhatkit
import pyautogui
import pandas as pd
import time

def enviar_mensaje(df, operador):
    message = """
    ¡Hola {Tienda}! 
    La cantidad de bultos  a recolectar es {bultos}.

    Te detallamos los datos del operador Logístico: 

    {operador}
   
 
    Quedo atento a su comentario.
    ¡Gracias! 
    Miguel Pazos
    """

    country_code = "+51"

    for i in range(len(df["Nombre_Tienda"])):
        # Ensure the phone number has the country code
        phone_number = f"{country_code}{df['CELULAR'][i]}"

        pywhatkit.sendwhatmsg_instantly(
            phone_number,
            message.format(
                Tienda=df["Nombre_Tienda"][i],
                ID=df["ID Tienda"][i],
                bultos=df["bultos"][i],
                operador=operador,
            )
        )
        time.sleep(15)
        pyautogui.press('enter')


# Enviar mensajes a los operadores
enviar_mensaje(M_df_result, "Inversiones")
enviar_mensaje(S_df_result, "Sedel")
