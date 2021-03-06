from MetroCardMachine import MetroCardBalance, MTATransportation, BalanceFullException


def num_trips_using_base_fare(total_balance, base_fare):
    num_trips = total_balance / base_fare
    remaining_balance = total_balance % base_fare
    return int(num_trips), remaining_balance


def num_info_using_different_transit(metro_card_balance):
    count = 0
    balance = metro_card_balance.show_balance()
    mtaTransportation = MTATransportation()
    transit_data = mtaTransportation.get_all_transit_info()
    transit_fare = []
    transit_count_data = {}

    while balance > 2.75:
        transportation = input("Enter Transit: ")
        if transportation not in transit_data.keys() or transit_data[transportation] > balance:
            print('Invalid Data or Insufficient Fare')
            continue

        balance = metro_card_balance.deduct_balance(transportation)
        print(balance)
        transit_fare.append(mtaTransportation.get_transportation_fare(transportation))
        if transportation in transit_count_data.keys():
            transit_count_data[transportation] += 1
        else:
            transit_count_data[transportation] = 1
        count += 1

    return transit_fare, transit_count_data, count


def transit_usage_log(amount):
    mtaTransportation = MTATransportation()
    metro_card_balance = MetroCardBalance(mtaTransportation)
    metro_card_balance.balance = metro_card_balance.add_balance(amount)
    transit_data = num_info_using_different_transit(metro_card_balance)
    total = 0
    print("Name: Ron Karim")
    print('Public Transportation Fares Paid: ')
    for fare in transit_data[0]:
        print('$' + str(fare))
        total += fare

    print('Total Fares Paid: $' + str(total))
    print('Number Of Trips Made until insufficient balance: ' + str(transit_data[2]))
    print('Number Of Times Commuted on Particular Public Transit: ' + str(transit_data[1]))






