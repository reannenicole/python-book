current_year = int(input('what year is it? '))
received_year = int(input('What year did you get your passport? '))
if received_year + 10 < current_year:
    print('You should go get a new passport!')
if received_year + 10 == current_year:
    print('You should get a new passport sometime soon')
if received_year + 10 > current_year:
    print('You do not need to get a new passport for now')