alert_failure_count = 0
MAX_TEMP_ALLOWED_IN_CELCIUS = 200

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    if(celcius <= MAX_TEMP_ALLOWED_IN_CELCIUS):
    # Return 200 for ok
        return 200
    else:
    # Return 500 for not-ok
        return 500

def alert_in_celcius(farenheit):   # Complain, this function ask for celcius but the parameter is in Farenheit
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 0 # Error, this lines adds 0, must add 1.

# insert 3 valid temperatures
alert_in_celcius(250.5)
alert_in_celcius(300.6)
alert_in_celcius(303.6)
# insert 3 invalid temperatures
alert_in_celcius(400.6)
alert_in_celcius(401.6)
alert_in_celcius(560.6)
print(f'{alert_failure_count} alerts failed.')
assert(alert_failure_count == 3)
print('All is well (maybe!)')
