GENDER_DEFAULT = [
    {'id': 'https://d-nb.info/standards/vocab/gnd/gender#notKnown'}
]


def fetch_gender(gnd_payload):
    gender_list = gnd_payload.get(
        'gender', GENDER_DEFAULT
    )
    return gender_list[0]['id']
