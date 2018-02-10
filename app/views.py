from app import app, models, db, translator
from flask import Flask, render_template, redirect, request, abort
from .forms import LoginForm, RegisterForm, AnswerForm, EmailForm
from flask_login import LoginManager, login_user, login_required, current_user

login_manager = LoginManager()
login_manager.init_app(app)
translator = translator.Translator()

@login_manager.user_loader
def load_user(user_id):
    return models.User.query.filter_by(user_id = user_id).first()

@app.route('/', methods = ['POST', 'GET'])
def login():
    form = LoginForm()
    error = False

    if form.validate_on_submit():
        passkey = form.passkey.data;
        user = models.User.query.filter_by(user_id = passkey).first()

        if user:
            login_user(user)
            return redirect('/main')
        else:
            error = True

    return render_template('login.html', form = form, error = error)

@app.route('/main', methods = ['GET', 'POST'])
@login_required
def main():
    loc = translator.get_localized_dict(current_user.language)
    user = models.User.query.filter_by(user_id = current_user.user_id).first()
    registered = models.Person.query.filter_by(user_id = current_user.user_id)

    accepted = True
    answered = True
    form = None

    if user.answer == None:
        accepted = False
        answered = False
        form = AnswerForm()
        form.answer.choices = [
            ('yes', loc['rsvp_1']),
            ('no', loc['rsvp_2'])
        ]

    elif user.answer:
        accepted = True
        form = RegisterForm()

    else:
        accepted = False

    return render_template('main.html',
                           authenticated = True,
                           invite_text = current_user.invite_text,
                           registered = registered,
                           accepted = accepted,
                           answered = answered,
                           form = form,
                           loc = loc,
                           lang = current_user.language,
                           email_form = EmailForm(),
                           email = user.email)

@app.route('/answer', methods = ['POST'])
@login_required
def answer():
    form = AnswerForm(request.form)
    user = models.User.query.filter_by(user_id = current_user.user_id).first()

    if form.answer.data == 'yes':
        user.answer = True
        db.session.commit()

        loc = translator.get_localized_dict(current_user.language)
        registered = models.Person.query.filter_by(user_id = current_user.user_id)

        return render_template('register.html',
                               email_form = EmailForm(),
                               email = user.email,
                               form = RegisterForm(),
                               loc = loc,
                               registered = registered)

    elif form.answer.data == 'no':
        user.answer = False
        db.session.commit()

        loc = translator.get_localized_dict(current_user.language)
        return '<h1>RSVP</h1><p>' + loc['reg_answer_3'] + '</p>'

    else:
        # none chosen, notify user of error
        return abort(400)

@app.route('/register', methods = ['POST'])
@login_required
def register():
    form = RegisterForm(request.form)

    if form.validate_on_submit():
        participant = models.Person(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            user_id = current_user.user_id
        )

        db.session.add(participant)
        db.session.flush()

        food_choice = models.FoodChoice(
            person = participant.id,
            vegetarian = form.vegetarian.data,
            vegan = form.vegan.data,
            kid_menu = form.kids_menu.data,
            allergy = form.allergies.data
        )

        print("register", participant.first_name, participant.last_name)

        db.session.add(food_choice)
        db.session.commit()

        return str(participant);

    return abort(400)

@app.route('/delete', methods = ['POST'])
@login_required
def delete():
    names = request.data.decode('utf-8').split(', ')
    given_names = names[1]
    family_names = names[0]

    print("delete", given_names, family_names)

    person = models.Person.query.filter_by(user_id = current_user.user_id,
                                           first_name = given_names,
                                           last_name = family_names).first()

    if person:
        food_choice = models.FoodChoice.query.filter_by(person = person.id).first()
        if food_choice:
            db.session.delete(food_choice)
            db.session.commit()

        db.session.delete(person)
        db.session.commit()
        return 'deleted'

    return abort(400)

@app.route('/email', methods=['POST'])
@login_required
def email():
    form = EmailForm(request.form)

    if form.validate_on_submit():
        user = models.User.query.filter_by(user_id = current_user.user_id).first()
        user.email = form.email.data
        db.session.commit()
        return 'successfully added {}'.format(user.email)

    return abort(400)

if __name__ == '__main__':
    app.run(host = '0.0.0.0')
