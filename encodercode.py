# from time import sleep
# from motor import Motor
# from encoder import Encoder
#
# V = 100
#
# motor_left = Motor("left", "D6", "D7", "D4")
# motor_right = Motor("right", "D8", "D9", "D5")
#
# ENC_L = "D2"
# ENC_R = "D3"
# enc = Encoder(ENC_L, ENC_R)
#
# while True:
#     motor_left.set_forwards()
#     motor_right.set_forwards()
#     enc.clear_count()
#
#     while (enc.get_left() + enc.get_right())/2 < V:
#         motor_left.duty(80)
#         motor_right.duty(80)
#         motor_right.duty(0)
#         motor_left.duty(0)
#         sleep(1)
#
#         enc.clear_count()
#         motor_left.set_backwards()
#         motor_right.set_backwards()
#
#         while (enc.get_left() + enc.get_right())/2 < V:
#             motor_left.duty(80)
#             motor_right.duty(80)
#         sleep(1)

