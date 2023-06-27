#! python3

###                                                      Using an Assertion in a Traffic Light Simulation

market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
    for key in stoplight.keys():

        if stoplight[key] == 'green':
          stoplight[key] = 'yellow'
        
        elif stoplight[key] == 'yellow':
           stoplight[key] = 'red'

        elif stoplight[key] == 'red':
         stoplight[key] = 'green'

    # Assertion Sanity Check
    assert 'red' in stoplight.values(), 'Neither Light is Red: ' + str(stoplight)

switchLights(market_2nd)