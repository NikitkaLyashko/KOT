"""
Как найти стартовый период?   ---  период записывается в переменную в ручную
    что означает число? --- задержку между появлением капель
"""
import model,view,controller,time

while True:
    controller.controller()
    time.sleep(1/60)
    view.mirror()
    model.ride_cloud()

