import configuration
import requests
import data


#Содание нового заказа
def post_new_order(order_body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER,
        json=data.order_body,
        headers=data.headers
    )
#Запоминаем трек-номер заказа
def get_track_order():
    track_response = post_new_order(data.order_body)
    return track_response.json()["track"]
#Выполнение запроса на получение заказа по трек-номеру
def get_track_order_info():
    track = get_track_order()
    par = {"t": track}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFO, params=par)
