# -*- coding: UTF-8 -*-

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource



app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': 'do something'},
    'todo3': {'task': 'profit!'},
}

PROJECTS = {
    'project1': {
        'name': 'todo app',
        'description': 'Lorem dolor sit amet ipsum dolor sit consectetuer dolore. Lorem dolor sit amet ipsum dolor sit consectetuer dolore.',
        'tasks': '17',
        'members': '16'
    },
    'project2': {
        'name': 'note book',
        'description': 'Lorem dolor sit amet ipsum dolor sit consectetuer dolore. Lorem dolor sit amet ipsum dolor sit consectetuer dolore.',
        'tasks': '43',
        'members': '32'
    }
}

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
        return PROJECTS[project_id]

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
        return PROJECTS

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
