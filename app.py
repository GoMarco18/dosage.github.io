from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    weight = float(data['weight'])
    dosage = float(data['dosage'])
    strength = float(data['strength'])
    
    # Get unit conversion factors
    weight_uom = float(data['weight_uom'])
    dosage_uom = float(data['dosage_uom'])
    strength_uom = float(data['strength_uom'])

    # Convert weight to grams if necessary
    weight_in_grams = weight * weight_uom

    # Adjust dosage and concentration if necessary
    dosage_adjusted = dosage * dosage_uom
    strength_adjusted = strength * strength_uom

    # Calculate dosage amount
    weight_ratio = weight_in_grams / 1000  # Convert grams to kg for the ratio
    part_of_ml = dosage_adjusted / strength_adjusted
    result = round(weight_ratio * part_of_ml, 2)

    return jsonify({"result": f"{result} cc"})

if __name__ == '__main__':
    app.run(debug=True)