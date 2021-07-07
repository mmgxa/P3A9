def profile_nt():
    '''
    This function generates profiles for 100 individuals. The profiles are stored
    in named tuples. The most common blood type, oldest age, mean age, and the 
    mean location are printed.
    '''
    #########################################
    ##############  Imports  ################
    #########################################
    from faker import Faker
    from collections import namedtuple
    from collections import Counter
    import datetime
    from time import perf_counter

    #########################################
    ###### Intitializing the Objects ########
    #########################################
    fake = Faker()
    blood_count = Counter()


    #########################################
    ####### Defining the NamedTuple #########
    #########################################
    profile = namedtuple('profile', ['job', 'company', 'ssn', 'residence', 'current_location',
                        'blood_group', 'website', 'username', 'name', 'sex', 'address', 'mail', 'birthdate'])
    profile.__doc__ = 'Fake personnel profile using faker library'

    start = perf_counter()
    #########################################
    ######## Creating the Profiles ##########
    #########################################
    cnt = 10000
    for c in range(cnt):
        globals()['profile' + str(c)] = profile(**fake.profile())


    lat = 0
    lng = 0
    mindob = datetime.date(datetime.datetime.now().year,
                        datetime.datetime.now().month, datetime.datetime.now().day)
    sumdob = datetime.timedelta(0)
    today = datetime.date(datetime.datetime.now().year,
                        datetime.datetime.now().month, datetime.datetime.now().day)
    for c in range(cnt):
        blood_count.update([(globals()['profile' + str(c)]).blood_group])
        lat += (globals()['profile' + str(c)]).current_location[0]
        lng += (globals()['profile' + str(c)]).current_location[1]
        mindob = min(mindob, (globals()['profile' + str(c)]).birthdate)
        sumdob += today - (globals()['profile' + str(c)]).birthdate

    lat = lat/cnt
    lng = lng/cnt

    sumdob = int(sumdob.days / cnt)
    avg_year = sumdob // 365
    avg_mnt = (sumdob - avg_year * 365) // 30
    avg_day = (sumdob - avg_year * 365 - avg_mnt*30)

    max_age = (today - mindob).days
    max_year = max_age // 365
    max_mnt = (max_age - max_year * 365) // 30
    max_day = round((max_age - max_year * 365 - max_mnt*30),0)

    common_bt = blood_count.most_common(1)[0][0]
    common_bt_cnt = blood_count.most_common(1)[0][1]

    print(
        f'The most common blood type is {common_bt} with {common_bt_cnt} counts')
    print(f'Avg. Age is {avg_year} Years, {avg_mnt} Months, and {avg_day} Days')
    print(f'Oldest. Age is {max_year} Years, {max_mnt} Months, and {max_day} Days')
    print(f'Mean location is ({lat}, {lng})')
    end = perf_counter()

    total_elapsed = end - start
    print(f'Time {total_elapsed}')

    return {'count': cnt, 'common_bt_cnt': common_bt_cnt, 'avg_year': avg_year, 'avg_mnt': avg_mnt, 'avg_day': avg_day, 'max_year': max_year, 'max_mnt': max_mnt, 'max_day' : max_day,  'mean_location': (lat, lng) }


def profile_dict():
    '''
    This function generates profiles for 100 individuals. The profiles are stored
    in dictionaries. The most common blood type, oldest age, mean age, and the 
    mean location are printed.
    '''
    #########################################
    ##############  Imports  ################
    #########################################
    from faker import Faker
    from collections import Counter
    import datetime
    from time import perf_counter

    #########################################
    ###### Intitializing the Objects ########
    #########################################
    fake = Faker()
    blood_count = Counter()

    start = perf_counter()
    #########################################
    ######## Creating the Profiles ##########
    #########################################
    cnt = 10000
    for c in range(cnt):
        globals()['profile' + str(c)] = fake.profile()

    lat = 0
    lng = 0
    dob = datetime.date(datetime.datetime.now().year,
                        datetime.datetime.now().month, datetime.datetime.now().day)
    sumdob = datetime.timedelta(0)
    today = datetime.date(2021, 1, 1)

    for c in range(cnt):
        blood_count.update([(globals()['profile' + str(c)]).get('blood_group')])

        lat += (globals()['profile' + str(c)]).get('current_location')[0]
        lng += (globals()['profile' + str(c)]).get('current_location')[1]
        dob = min(dob, (globals()['profile' + str(c)]).get('birthdate'))
        sumdob += today - (globals()['profile' + str(c)]).get('birthdate')

    lat = lat/cnt
    lng = lng/cnt

    sumdob = sumdob.days / cnt
    avg_year = sumdob // 365
    avg_mnt = (sumdob - avg_year * 365) // 30
    avg_day = (sumdob - avg_year * 365 - avg_mnt*30)

    max_age = (today - dob).days
    max_year = max_age // 365
    max_mnt = (max_age - max_year * 365) // 30
    max_day = (max_age - max_year * 365 - max_mnt*30)

    common_bt = blood_count.most_common(1)[0][0]
    common_bt_cnt = blood_count.most_common(1)[0][1]

    print(
        f'The most common blood type is {common_bt} with {common_bt_cnt} counts')
    print(f'Avg. Age is {avg_year} Years, {avg_mnt} Months, and {avg_day} Days')
    print(f'Oldest. Age is {max_year} Years, {max_mnt} Months, and {max_day} Days')
    print(f'Mean location is ({lat}, {lng})')
    end = perf_counter()

    total_elapsed = end - start
    print(f'Time {total_elapsed}')

    return {'count': cnt, 'common_bt_cnt': common_bt_cnt, 'avg_year': avg_year, 'avg_mnt': avg_mnt, 'avg_day': avg_day, 'max_year': max_year, 'max_mnt': max_mnt, 'max_day' : max_day,  'mean_location': (lat, lng) }

def company_fn():
    '''
    A function to generate profiles of 100 companies. The Stock values are
    intialized using random values (and so are the fluctuations). Low was not explicitly
    asked, but was hinted by the instructor while presenting test cases. 
    '''
    #########################################
    ##############  Imports  ################
    #########################################
    from faker import Faker
    from collections import namedtuple
    import random

    #########################################
    ###### Intitializing the Objects ########
    #########################################
    fake = Faker()


    #########################################
    ####### Defining the NamedTuple #########
    #########################################
    company = namedtuple(
        'company', ['name', 'symbol', 'open', 'high', 'low', 'close'])
    company.__doc__ = "Company stock profile with current market trend values"

    #########################################
    ######## Creating the Profiles ##########
    #########################################
    cnt = 100
    for c in range(cnt):
        comp_name = fake.company()
        comp_symb = comp_name
        open = random.randint(80, 950)
        fluctuations = [open * random.uniform(0.5, 1.5) for _ in range(48)]
        close = fluctuations[-1]
        high = max(fluctuations)
        low = min(fluctuations)
        globals()['company' + str(c)] = company(comp_name,
                                                comp_symb, open, high, low, close)

    #########################################
    ######## Analyzing the Profiles #########
    #########################################
    stock_open, stock_high, stock_low, stock_close = 0, 0, 0, 0
    weights = [random.uniform(0.1, 0.9) for _ in range(cnt)]
    norm_wts = [x/sum(weights) for x in weights]
    for c in range(cnt):
        stock_open += (globals()['company' + str(c)]).open * norm_wts[c]
        stock_high += (globals()['company' + str(c)]).high * norm_wts[c]
        stock_low += (globals()['company' + str(c)]).low * norm_wts[c]
        stock_close += (globals()['company' + str(c)]).close * norm_wts[c]

    #########################################
    ####### Determination of High/Low #######
    #########################################
    stock_high = stock_close if stock_close > stock_high else stock_high
    stock_low = stock_close if stock_close < stock_low else stock_low

    stock_open, stock_high, stock_low, stock_close = round(stock_open, 2), round(
        stock_high, 2), round(stock_low, 2), round(stock_close, 2)

    print(f'Stock opened at:{stock_open}')
    print(f'Stock highest:{stock_high}')
    print(f'Stock lowest:{stock_low}')
    print(f'Stock closed at:{stock_close}')

    return {'cmp_cnt': cnt, 'stock_open': stock_open, 'stock_high': stock_high, 'stock_low': stock_low, 'stock_close': stock_close}

