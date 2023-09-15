import model,view,controller,time

while True:
    controller.controller()
    time.sleep(1/60)
    view.mirror()
    model.ride_cloud()
    print(model.kapli)