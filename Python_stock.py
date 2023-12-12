from nsepython import nse_eq
from time import sleep
import serial 
import json
file = open('market_details.json')
file_data = json.load(file)
arduino = serial.Serial(port=file_data['controller_port'], baudrate=115200, timeout=.1)
while(True):
    share_1_data=nse_eq(file_data["share_1_name"])["priceInfo"]
    share_1_p="{:.2f}".format(share_1_data['lastPrice'])
    share_1_c="{:.2f}".format(share_1_data['change'])
    share_1_pc="{:.2f}".format(share_1_data['pChange'])
    if(float(share_1_c)<0):
        share_1_color="RED"
    else:
        share_1_color="GREEN"

    share_2_data=nse_eq(file_data["share_2_name"])["priceInfo"]
    share_2_p="{:.2f}".format(share_2_data['lastPrice'])
    share_2_c="{:.2f}".format(share_2_data['change'])
    share_2_pc="{:.2f}".format(share_2_data['pChange'])
    if(float(share_2_c)<0):
        share_2_color="RED"
    else:
        share_2_color="GREEN"

    share_3_data=nse_eq(file_data["share_3_name"])["priceInfo"]
    share_3_p="{:.2f}".format(share_3_data['lastPrice'])
    share_3_c="{:.2f}".format(share_3_data['change'])
    share_3_pc="{:.2f}".format(share_3_data['pChange'])
    if(float(share_3_c)<0):
        share_3_color="RED"
    else:
        share_3_color="GREEN"


    share_4_data=nse_eq(file_data["share_4_name"])["priceInfo"]
    share_4_p="{:.2f}".format(share_4_data['lastPrice'])
    share_4_c="{:.2f}".format(share_4_data['change'])
    share_4_pc="{:.2f}".format(share_4_data['pChange'])
    if(float(share_4_c)<0):
        share_4_color="RED"
    else:
        share_4_color="GREEN"

    final_data=f"{file_data['share_1_name']},{share_1_p},{share_1_c},{file_data['share_2_name']},{share_2_p},{share_2_c},{file_data['share_3_name']},{share_3_p},{share_3_c},{file_data['share_4_name']},{share_4_p},{share_4_c},{share_1_color},{share_2_color},{share_3_color},{share_4_color}"
    print(final_data)
    sleep(0.2)
    arduino.write(bytes(final_data, 'utf-8')) 
    sleep(5)