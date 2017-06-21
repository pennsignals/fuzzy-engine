from random import gauss, uniform, choice
import datetime

from faker import Faker
import flask

from fuzzy import app

FAKE = Faker()


def random_height():
    """In meters"""
    mu = 1.6
    sigma = 0.3

    return gauss(mu, sigma)


def random_weight():
    """In KG"""
    mu = 80
    sigma = 30

    return gauss(mu, sigma)


def random_dob():
    """"""
    mu = -1.6e+08
    sigma = 6.8e+08

    d = datetime.date.fromtimestamp(gauss(mu, sigma))
    d = datetime.datetime(d.year, d.month, d.day)
    return d.isoformat()


def random_admit_source():
    rand = uniform(0, 1)
    if rand < 0.5:
        return 'EMERGENCY'
    elif rand < 0.83:
        return 'ROUTINE'
    else:
        return 'TRANSFER'


def random_admit_type():
    rand = uniform(0, 1)
    if rand < 0.55:
        return 'Emergency'
    elif rand < 0.83:
        return 'Routine elective'
    elif rand < 0.93:
        return 'Pregnancy'
    elif rand < 0.98:
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


def random_first_name():
    return FAKE.first_name()


def random_last_name():
    return FAKE.last_name()


def random_service():
    rand = uniform(0, 1)
    if rand < 0.30:
        return 'EMERGENCY DEPARTMENT'
    elif rand < 0.43:
        return 'HOSPITALIST'
    elif rand < 0.56:
        return 'CARDIOVASCULAR MEDICINE'
    elif rand < 0.67:
        return 'OBSTETRICS'
    elif rand < 0.73:
        return 'ORTHOPEDICS'
    elif rand < 0.79:
        return 'MEDICINE'
    elif rand < 0.85:
        return 'ONCOLOGY'
    elif rand < 0.90:
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
    elif rand < 0.99989:
        return 'Male'
    else:
        return 'Unknown'


def random_marital_status():
    rand = uniform(0, 1)
    if rand < 0.45:
        return 'Single'
    elif rand < 0.85:
        return 'Married'
    elif rand < 0.9:
        return 'Widowed'
    elif rand < 0.95:
        return 'Divorced'
    else:
        return 'Unknown'


def random_demographic():
    return {
        'height': random_height(),
        'weight': random_weight(),
        'dob': random_dob(),
        'admit_source': random_admit_source(),
        'admit_type': random_admit_type(),
        'provider_name': random_provider_name(),
        'provider_phone': random_provider_phone(),
        'hospital': random_hospital(),
        'first_name': random_first_name(),
        'last_name': random_last_name(),
        'visit_number': random_visit_number(),
        'service': random_service(),
        'race': random_race(),
        'gender': random_sex(),
        'marital_status': random_marital_status(),
    }


@app.route('/v1/demographics')
def index():
    return flask.jsonify([random_demographic() for i in range(20)])
