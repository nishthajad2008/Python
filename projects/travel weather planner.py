distance_mi = 0.1

is_raining = True
has_bike = True
has_car = False
has_ride_share_app = True

if bool(distance_mi) == False:
    print("False")
elif distance_mi <= 1 and not is_raining:
    print("True")
elif 1 < distance_mi <= 6 and has_bike and not is_raining:
    print("True")
elif distance_mi > 6 and (has_car or has_ride_share_app):
    print('True')
else:
    print("False")