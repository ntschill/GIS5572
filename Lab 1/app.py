import psycopg2
import flask
from flask import Flask, jsonify
from psycopg2 import sql

app = Flask(__name__)

def get_star():
    schiller_database = psycopg2.connect(host = '34.67.63.162',
                    database = 'lab0',
                    user = 'postgres',
                    password = '')
    cursor = schiller_database.cursor()
    cursor.execute("SELECT ST_AsGeoJSON(geom) FROM geometries LIMIT 1;")
    result = cursor.fetchone()
    cursor.close()
    schiller_database.close()
    return result[0]

@app.route('/star', methods=['GET'])
def star():
    geojson = get_star()
    return jsonify(geojson)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
