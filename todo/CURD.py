# -*- coding: UTF-8 -*-

# http://stackoverflow.com/questions/19962699/flask-restful-cross-domain-issue-with-angular-put-options-methods
# https://pypi.python.org/pypi/Flask-Cors
# use Flask-CORS cross-domain

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
# from flask.ext.cors import CORS



app = Flask(__name__)
# cors = CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)

# use the after_request hook http://tutsbucket.com/tutorials/building-a-blog-using-flask-and-angularjs-part-1/
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response



TODOS = [
    {
        'task': 'build an API'
    },
    {
        'task': 'do something'
    },
    {
        'task': 'profit!'
    }
]

PROJECTS = [
    {
        'name': 'todo app',
        'description': 'Lorem dolor sit amet ipsum dolor sit consectetuer dolore. Lorem dolor sit amet ipsum dolor sit consectetuer dolore.',
        'tasks': '17',
        'members': '16'
    },
    {
        'name': 'note book',
        'description': 'Lorem dolor sit amet ipsum dolor sit consectetuer dolore. Lorem dolor sit amet ipsum dolor sit consectetuer dolore.',
        'tasks': '43',
        'members': '32'
    }
]

# check todo_id is exist
def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')

# check project id is exist
def abort_if_project_doesnt_exist(project_id):
    if project_id not in PROJECTS:
        abort(404, message = "Project {} doesn't exist".format(project_id))


# Todo
# show a single todo item and lets you delete them
# add item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return 'success', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201


# TodoList
#   shows a list of all todos, and lets you POST to add new tasks
class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = 'todo%d' % (len(TODOS) + 1)
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201



class Project(Resource):
    def get(self, project_id):
        abort_if_project_doesnt_exist(project_id)
        return PROJECTS[project_id], 200

    def delete(self, project_id):
        abort_if_project_doesnt_exist(project_id)
        del PROJECTS[project_id]
        return '', 204

    def put(self, project_id):
        args = parser.parse_args()
        project = {
            'name': args['name'],
            'description': args['description']
        }
        PROJECTS[project_id] = project
        return project, 201



class ProjectList(Resource):
    def get(self):
        return PROJECTS, 200

    def post(self):
        args = parser.parse_args()
        project_id = 'project%d' % (len(PROJECTS) + 1)
        PROJECTS[project_id] = {'task': args['task']}
        return PROJECTS[project_id], 201


##
## Actually setup the Api resource routing here
##
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<string:todo_id>')
api.add_resource(ProjectList, '/projects')
api.add_resource(Project, '/projects/<string:project_id>')

if __name__ == '__main__':
    app.run(debug=True)
