#!flask/bin/python
from flask import Flask, jsonify, make_response, abort, request, url_for
from SimConnect import *

# creat simconnection and pass used user classes


app = Flask(__name__)

requests = [
	{
		'id': 1,
		'time': 2000,
		'definitions': [
			{'definition': u'Plane Altitude', 'format': u'feet'},
			{'definition': u'Plane Latitude', 'format': u'degrees'},
			{'definition': u'Plane Longitude', 'format': u'degrees'},
			{'definition': u'Kohlsman setting hg', 'format': u'inHg'},
		],
		'haveData': False
	},
	{
		'id': 2,
		'time': 0,
		'definitions': [
			{'definition': u'PRESSURE ALTITUDE', 'format': u'feet'},
			{'definition': u'GEAR HANDLE POSITIO', 'format': u'bool'},

		],
		'haveData': False
	},
	{
		'id': 3,
		'time': 5000,
		'definitions': [
			{'definition': u'AUTOPILOT_MASTER', 'format': u'bool'}
		],
		'haveData': False
	}
]

events = [
	{
		'id': 1,
		'event': u'GEAR_DOWN',
		'value': 0
	},
	{
		'id': 2,
		'event': u'GEAR_UP',
		'value': 0
	},
	{
		'id': 3,
		'event': u'GEAR_TOGGLE',
	},
	{
		'id': 4,
		'event': u'THROTTLE1_SET',
		'value': 0
	}
]


sm = SimConnect()
requests_map = {}
events_map = {}


def mapResuest(_id, _time, _definitions):
	requests_map[_id] = sm.newRequest(_time)
	for deff in _definitions:
		print(deff)
		requests_map[_id].add("request_%d" % (_definitions.index(deff)), (deff['definition'].encode(), deff['format'].encode()))


def mapEvent(_id, _event):
	events_map[_id] = sm.MapToSimEvent(_event.encode())


for rq in requests:
	mapResuest(rq['id'], rq['time'], rq['definitions'])

for ev in events:
	mapEvent(ev['id'], ev['event'])


@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/pysim/api/v0.1/', methods=['GET'])
def get_all():
	return jsonify({'requests': requests, 'events': events})


@app.route('/pysim/api/v0.1/<page>', methods=['GET'])
def get_page(page):
	return jsonify({page: globals()[page]})


@app.route('/pysim/api/v0.1/requests/<int:task_id>', methods=['GET'])
def get_request(task_id):
	request = [request for request in requests if request['id'] == task_id]
	if len(request) == 0:
		abort(404)
	request[0]['haveData'] = False
	sm.RequestData(requests_map[task_id])
	sm.Run()
	data = sm.GetData(requests_map[task_id], True)
	while data is None:
		sm.Run()
		data = sm.GetData(requests_map[task_id], True)
	request[0]['haveData'] = True
	for dd in request[0]['definitions']:
		dd['data'] = data["request_%d" % (request[0]['definitions'].index(dd))]
	request[0]['haveData'] = True
	return jsonify({'request': request[0]})


@app.route('/pysim/api/v0.1/events/<int:task_id>', methods=['GET'])
def get_event(task_id):
	event = [event for event in events if event['id'] == task_id]
	if len(event) == 0:
		abort(404)
	return jsonify({'events': event[0]})


@app.route('/pysim/api/v0.1/requests', methods=['POST'])
def create_request():
	if not request.json:
		abort(400)

	task = None

	if 'definitions' in request.json:
		task = {
			'id': requests[-1]['id'] + 1,
			'time': request.json.get('time', 0),
			'definitions': request.json['definitions'],
			'haveData': False
		}
		mapResuest(task['id'], task['time'], task['definitions'])

	requests.append(task)
	return jsonify({'requests': requests[page]}), 201


@app.route('/pysim/api/v0.1/events', methods=['POST'])
def create_event():
	if 'event' in request.json:
		task = {
			'id': events[-1]['id'] + 1,
			'event': request.json['event'],
			'value': request.json.get('value', 0)
		}
		mapEvent(task['id'], task['event'])
	else:
		abort(400)

	events.append(task)
	return jsonify({'events': events}), 201


@app.route('/pysim/api/v0.1/events/<int:task_id>', methods=['PUT'])
def update_events(task_id):
	task = [task for task in events if task['id'] == task_id]
	val = 0
	if len(task) == 0:
		abort(404)
	if request.json:
		val = request.json.get('value', 0)
	rs = sm.SendData(events_map[task_id], DWORD(val))
	sm.Run()
	return jsonify({'result': rs, 'val': val})


@app.route('/pysim/api/v0.1/<page>/<int:task_id>', methods=['DELETE'])
def delete_task(page, task_id):
	task = [task for task in globals()[page] if task['id'] == task_id]
	if len(task) == 0:
		abort(404)
	pmap = page + "_map"
	del globals()[pmap][task_id]
	globals()[page].remove(task[0])
	return jsonify({'result': True})


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
