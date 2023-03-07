from flask import Flask, render_template, jsonify, abort, request

app = Flask (__name__)
uri = '/api/tasks/'
persona = {'name': 'Rafael', 'matricula': '123456'}

tasks = [
  {
    'id': 1,
    'name': "Cocinar algo bien sabroso",
    'status': False
   },
    {
    'id': 2,
     'name': "Limpiar la casa",
    'status': False
    },
]

@app. route("/")
def hello_world():
  return render_template('index.html', data = persona)

# API
@app. route(uri, methods= ['GET'])
def get_tasks():
  return jsonify({'tasks': tasks})

@app. route(uri+'/<int:id>', methods = ['GET']) 
def get_task(id):
  this_task = 0
  for task in tasks:
    if task['id'] == id:
      this_task = task
  if this_task == 0:
    abort (404)
  return jsonify({'task': this_task})

@app. route(uri, methods=['POST']) 
def create_task():
  if request.json:
    task = {
    'id': len(tasks)+1,
    'name': request. json ['name'],
    'status': False
    }
    tasks.append(task)
    return jsonify({'tasks': tasks}), 201
  else:
    abort (404)

@app. route(uri+'/<int:id>', methods=['PUT']) 
def update_task(id) :
  if request.json:
    this_task = [task for task in tasks if task['id'] == id]
    if this_task:
      if request. json.get ('name'):
        this_task[0] ['name'] = request.json [' name ']

    if request.json.get ('status'):
     this_task[0] ['status'] = request.json ['status']
     return jsonify({'task': this_task[0]}), 201

    else:
      abort (404)
  else:
    abort (404)

@app. route(uri+"/<int:id>", methods= ['DELETE']) 
def delete_task(id):
  this_task = (task for task in tasks if task['id'] == id)
  if this_task:
    tasks.remove(this_task[0])
    return jsonify({'tasks': tasks})
  else:
    abort(404)

if __name__=='__main__':
  app. run(debug=True)