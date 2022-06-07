def make_car(mfg, model, **args):
    
    car = {}
    car['manufacturer'] = mfg
    car['model'] = model
    
    for arg in args.keys():
        car[arg]=args[arg]
    
    return car



car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)
