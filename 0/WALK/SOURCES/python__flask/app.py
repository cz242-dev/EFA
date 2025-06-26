# app.py

from flask import Flask, request, jsonify

app = Flask(__name__)

class WalkModule:
    def __init__(self):
        self.methods = ['SLOWLY', 'RUN', 'CASUAL', 'QUICKLY']
        self.models = {
            'LEG': ['left', 'right'],
            'FOOT': ['heel', 'toe'],
            'STEP': ['small', 'medium', 'large'],
            'TYPE': ['walk', 'run', 'skip'],
            'ATTRIBUTES': ['speed', 'style', 'energy']
        }
        self.mixes = {
            'FOOTLEG': {'heel': 'left', 'toe': 'right'},
            'LEGTYPE': {'left': 'walk', 'right': 'run'}
        }
        self.maps = {
            'LEGS': ['left', 'right'],
            'STEPS': ['step1', 'step2', 'step3'],
            'FOOTS': ['foot1', 'foot2']
        }
        self.magma = {
            'LEG_ATTRIBUTES': {'strength': 10, 'flexibility': 8},
            'FOOT_ATTRIBUTES': {'arch': 'high', 'size': 42}
        }
        self.meanings = [
            ['TYPE', 'STEP', 'FOOT', 'LEG'],
            ['TYPE', 'FOOT', 'LEG'],
            ['TYPE', 'LEG', 'ATTRIBUTES']
        ]
        self.mantras = [
            "MODULE WALK PROVIDES [&meaning] OF [#model] with [@method]",
            "[&meaning] means [&meaning] with [@method]"
        ]

    def SLOWLY(self):
        return "Walking slowly... (dummy data)"

    def RUN(self):
        return "Running! (dummy data)"

    def CASUAL(self):
        return "Walking casually. (dummy data)"

    def QUICKLY(self):
        return "Walking quickly! (dummy data)"

    def get_model(self, model):
        return self.models.get(model)

    def get_mix(self, mix):
        return self.mixes.get(mix)

    def get_map(self, map_name):
        return self.maps.get(map_name)

    def get_magma(self, magma_name):
        return self.magma.get(magma_name)

    def get_meanings(self):
        return self.meanings

    def get_mantras(self):
        return self.mantras

    def call_method(self, method):
        if method in self.methods and hasattr(self, method):
            return getattr(self, method)()
        return f"Unknown method: {method}"

walk = WalkModule()

# --- ROUTES ---

@app.route('/step')
def step():
    from_ = request.args.get('from')
    to = request.args.get('to')
    return jsonify({
        "action": "step",
        "from": from_,
        "to": to,
        "result": f"Stepping from {from_} to {to} (dummy data)"
    })

@app.route('/foot')
def foot():
    from_ = request.args.get('from')
    to = request.args.get('to')
    size = request.args.get('size')
    return jsonify({
        "action": "foot",
        "from": from_,
        "to": to,
        "size": size,
        "result": f"Foot from {from_} to {to} with size {size} (dummy data)"
    })

@app.route('/method/<method_name>')
def method(method_name):
    result = walk.call_method(method_name.upper())
    return jsonify({"method": method_name, "result": result})

@app.route('/model/<model_name>')
def model(model_name):
    data = walk.get_model(model_name.upper())
    return jsonify({model_name: data})

@app.route('/mix/<mix_name>')
def mix(mix_name):
    data = walk.get_mix(mix_name.upper())
    return jsonify({mix_name: data})

@app.route('/map/<map_name>')
def map_(map_name):
    data = walk.get_map(map_name.upper())
    return jsonify({map_name: data})

@app.route('/magma/<magma_name>')
def magma(magma_name):
    data = walk.get_magma(magma_name.upper())
    return jsonify({magma_name: data})

@app.route('/meanings')
def meanings():
    return jsonify({"meanings": walk.get_meanings()})

@app.route('/mantras')
def mantras():
    return jsonify({"mantras": walk.get_mantras()})

if __name__ == '__main__':
    app.run(debug=True)