from random import gauss, uniform, choice
import datetime

from faker import Faker
import flask

from fuzzy import app

FAKE = Faker()


def random_height(sex):
    """In meters"""
    mu = 1.7
    sigma = 0.3
    if sex == 'Female':
        mu = 1.6
        sigma = 0.2

    return round(gauss(mu, sigma), 3)


def random_weight(sex):
    """In KG"""
    mu = 83
    sigma = 29
    if sex == 'Female':
        mu = 76
        sigma = 29

    return round(gauss(mu, sigma), 3)


def random_dob_no_future(admit_type):
    d = random_dob(admit_type)
    while d > datetime.datetime.now():
        d = random_dob(admit_type)

    return d.isoformat()


def random_dob(admit_type):
    """"""
    mu = -2.1e+08
    sigma = 6.7e+08
    if admit_type == 'Pregnancy':
        mu = 5.5e+08
        sigma = 1.87e+08

    d = datetime.date.fromtimestamp(gauss(mu, sigma))
    d = datetime.datetime(d.year, d.month, d.day)
    return d


def random_admit_source(admit_type):
    rand = uniform(0, 1)

    if admit_type == 'Pregnancy':
        if rand < 0.12:
            return 'ROUTINE'
        else:
            return 'TRANSFER'
    else:
        if rand < 0.5:
            return 'EMERGENCY'
        elif rand < 0.83:
            return 'ROUTINE'
        else:
            return 'TRANSFER'


def random_admit_type(sex):
    rand = uniform(0, 1)
    if sex == 'Female':
        if rand < 0.54:
            return 'Emergency'
        elif rand < 0.79:
            return 'Routine elective'
        elif rand < 0.94:
            return 'Pregnancy'
        elif rand < 0.98:
            return 'Urgent'
        else:
            return 'Other'
    else:
        if rand < 0.62:
            return 'Emergency'
        elif rand < 0.93:
            return 'Routine elective'
        elif rand < 0.99:
            return 'Urgent'
        else:
            return 'Other'


def random_provider_name():
    return '{}, {}'.format(FAKE.last_name(), FAKE.first_name())


def random_provider_phone():
    return '{}{:07d}'.format(choice([215, 267]), int(uniform(0, 9999999)))


def random_hospital():
    rand = uniform(0, 1)
    if rand < 0.50:
        return 'HUP'
    elif rand < 0.75:
        return 'PAH'
    else:
        return 'PMC'


def random_first_name(sex):
    if sex == 'Female':
        return FAKE.first_name_female()
    return FAKE.first_name_male()


def random_last_name():
    return FAKE.last_name()


def random_service(admit_type):
    if admit_type == 'Pregnancy':
        return 'OBSTETRICS'
    rand = uniform(0, 1)
    if rand < 0.34:
        return 'EMERGENCY DEPARTMENT'
    elif rand < 0.49:
        return 'HOSPITALIST'
    elif rand < 0.63:
        return 'CARDIOVASCULAR MEDICINE'
    elif rand < 0.7:
        return 'ORTHOPEDICS'
    elif rand < 0.77:
        return 'MEDICINE'
    elif rand < 0.83:
        return 'ONCOLOGY'
    elif rand < 0.89:
        return 'CARDIAC SURGERY'
    elif rand < 0.95:
        return 'PULMONARY'
    else:
        return 'GASTROENTEROLOGY'


def random_race():
    rand = uniform(0, 1)
    if rand < 0.45:
        return 'White'
    elif rand < 0.85:
        return 'Black'
    elif rand < 0.90:
        return 'Unknown'
    elif rand < 0.94:
        return 'Asian'
    elif rand < 0.97:
        return 'Hispanic'
    else:
        return 'Other'


def random_visit_number():
    return int(uniform(1, 999999999999))


def random_sex():
    rand = uniform(0, 1)
    if rand < 0.52:
        return 'Female'
    else:
        return 'Male'


def random_marital_status(admit_type):
    rand = uniform(0, 1)

    if admit_type == 'Pregnancy':
        if rand < 0.6:
            return 'Single'
        else:
            return 'Married'
    else:
        if rand < 0.43:
            return 'Single'
        elif rand < 0.82:
            return 'Married'
        elif rand < 0.89:
            return 'Widowed'
        elif rand < 0.95:
            return 'Divorced'
        else:
            return 'Unknown'


def random_demographic():
    sex = random_sex()
    admit_type = random_admit_type(sex)
    return {
        'height': random_height(sex),
        'weight': random_weight(sex),
        'dob': random_dob_no_future(admit_type),
        'admit_source': random_admit_source(admit_type),
        'admit_type': admit_type,
        'provider_name': random_provider_name(),
        'provider_phone': random_provider_phone(),
        'hospital': random_hospital(),
        'first_name': random_first_name(sex),
        'last_name': random_last_name(),
        'visit_number': random_visit_number(),
        'service': random_service(admit_type),
        'race': random_race(),
        'gender': sex,
        'marital_status': random_marital_status(admit_type),
    }


@app.route('/v1/demographics')
def index():
    return flask.jsonify([random_demographic() for _ in range(20)])
