# Пугач Елена, 9-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data

def test_get_track_order_info():
    track_number = sender_stand_request.get_track_order_info()
    assert track_number.status_code == 200