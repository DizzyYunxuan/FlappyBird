import os


# cmd_dict: 
#     0 : keep height
#     1 : raise
#     2 : dive

def send_cmd(bird_x, bird_y, h_ob_dict, v_sps_dict):
    left, right = -1, -1
    for key in h_ob_dict:
        left, right = h_ob_dict[key]
        upper, bot = v_sps_dict[key]
        if bird_y < right:
            break
    
    if left < 0 or right < 0:
        return 0
    else:
        if bird_x > (upper + bot) / 2 + 15:
            return 1
        elif bird_x < (upper + bot) / 2 + 15:
            return 2
        else:
            return 0



