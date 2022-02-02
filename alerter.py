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

def network_alert_real(celcius):
    return 200

def farenheit2celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    return celcius

def check_temp_in_farenheit(temp_farenheit, alertFunction=network_alert_real):   # Complain, this function ask for celcius but the parameter is in Farenheit
    celcius = farenheit2celcius(temp_farenheit)
    returnCode = alertFunction(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 1 # Error, this lines adds 0, must add 1.

# insert 3 valid temperatures
check_temp_in_farenheit(250.5, alertFunction=network_alert_stub)
check_temp_in_farenheit(300.6, alertFunction=network_alert_stub)
check_temp_in_farenheit(303.6, alertFunction=network_alert_stub)
# insert 3 invalid temperatures
check_temp_in_farenheit(400.6,alertFunction=network_alert_stub)
check_temp_in_farenheit(401.6, alertFunction=network_alert_stub)
check_temp_in_farenheit(560.6, alertFunction=network_alert_stub)
print(f'{alert_failure_count} alerts failed.')
assert(alert_failure_count == 3)
print('All is well (maybe!)')
