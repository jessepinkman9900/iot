from OneM2M import *

##################
table = "38"
##################

server = "http://192.168.1.233:8080"
cse = "/~/in-cse/in-name/"
led_num = "1"  # 1,2,3,4
ae = "tapEvent-" + table
led1="led-" + table +"-1"
led2="led-" + table +"-2"
led3="led-" + table +"-3"
led4="led-" + table +"-4"
# ------------------------------------------
# Write code to get the latest instance of
# tappingEvent
# ------------------------------------------
while True:
    x=get_data(server+cse+ae+"/DATA/la")
    print(x)


# ----------
# --------------------------------


# post_data(server+cse+led1,1)

# ------------------------------------------
# Based on the event, actuate odd/even numbered filtered_uri_list
# ------------------------------------------

# ------------------------------------------


# ------------------------------------------
# Post values to tree to switch on/switch off filtered_uri_list
# ------------------------------------------

# ------------------------------------------
