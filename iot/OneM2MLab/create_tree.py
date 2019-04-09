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
# Fill code here to create AE
# specified by the URI
# ------------------------------------------
ae_name = "led"+"-"+table+"-"+led_num
lbl = []
register_ae(server+cse ,ae ,["38","tapEvent"])
register_ae(server+cse ,led1 ,["38","led1","odd"])
register_ae(server+cse ,led2 ,["38","led2","even"])
register_ae(server+cse ,led3 ,["38","led3","odd"])
register_ae(server+cse ,led4 ,["38","led4","even"])

# ------------------------------------------


# ------------------------------------------
# Fill code here to create container in the AE
# specified by the URI
# ------------------------------------------
container_name = "DATA"
create_cnt(server+cse+ae,container_name)
create_cnt(server+cse+led1,container_name)
create_cnt(server+cse+led2,container_name)
create_cnt(server+cse+led3,container_name)
create_cnt(server+cse+led4,container_name)
# ------------------------------------------


# ------------------------------------------
# Fill code here to create content_instance
# specified by the URI
# ------------------------------------------
content_instance = 0
create_data_cin(server+cse+ae+"/DATA",content_instance)
# ------------------------------------------
x=get_data(server+cse+ae+"/DATA/la")
# l1=get_data(server+cse+led1+"/DATA/la")
# l2=get_data(server+cse+led2+"/DATA/la")
# l3=get_data(server+cse+led3+"/DATA/la")
# l4=get_data(server+cse+led4+"/DATA/la")
print(x)