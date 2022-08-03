
from flask import jsonify, request, abort

heroes = [{'name': 'steve redgrave', 'nationality': 'british', 'occupation': 'olympian'},
          {'name': 'arthur dent', 'nationality': 'british', 'occupation': 'time traveller'},
          {'name': 'martin luther king', 'nationality': 'american', 'occupation': 'activist'}
          ]


def index():
    return "Hallo Welt"

def db():
    return "Hello DB Grads"

def user_profile(id):
    return f"Profile page of user #{id}"

def hero():
    return jsonify(heroes)

def hero_add():
        try:
            data  = request.get_json(force=True)
            hero = data['name']
            nationality = data['nationality']
            occupation = data['occupation']

            if hero and nationality and occupation:
                heroes.append({'name': hero,
                               'nationality': nationality,
                               'occupation': occupation})
                return jsonify({'Hero' + hero:'Added successfully'})
        except Exception as err:
            print(err)
            abort(400)  # Abort HTTP request with HTTP error 400
        return None


def hero_update():
    try:
        data = request.get_json(force=True)
        hero = data['name']
        nationality = data['nationality']
        occupation = data['occupation']

        hero_to_update = None

        if hero and nationality and occupation:
            for idx, existing_hero in enumerate(heroes):
                print(existing_hero)
                if existing_hero['name'] == hero:
                    hero_to_update = existing_hero

            if hero_to_update:
                hero_to_update['nationality'] = nationality
                hero_to_update['occupation'] = occupation
                return jsonify({'Hero' + hero: 'Updated successfully'})
            else:
                return jsonify({'Hero' + hero: 'Hero not found'})

    except Exception as err:
        print(err)
        abort(400)  # Abort HTTP request with HTTP error 400
    return None