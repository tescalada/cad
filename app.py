from flask import Flask, jsonify, request, send_from_directory
import cadquery as cq

import logging

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)


@app.route('/')
def hello_world():
    return 'Hello, World!2'


@app.route('/block')
def block():
    
    height = 60.0
    width = 80.0
    thickness = 10.0

    # make the base
    result = cq.Workplane("XY").box(height, width, thickness)

    # Render the solid
    #show_object(result)
    cq.exporters.export(result, 'webresult.stl')

    # app.config['UPLOAD_FOLDER']
    return send_from_directory(
        '.',
        'webresult.stl', 
        as_attachment=True
    )


if __name__ == '__main__':
    app.run()
