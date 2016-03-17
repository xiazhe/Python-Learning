from wtforms import Form, StringField, validators


class userForm(Form):
    username = StringField('UserName', [validators.Length(min=5)], default=u'Admin')

    # def change_username



# from mini import *
# form = userForm()
# form['username']
# <wtforms.fields.core.StringField object at 0x0280A910>
# form['username'].data or form.username.data
# u'Admin'
# form.validate()
# form.errors()

# https://segmentfault.com/a/1190000002531677


