# Desc: OCR routes for the API
from flask import Blueprint, request, jsonify,current_app

from app.services import process_ocr

ocr_route = Blueprint('ocr', __name__)

@ocr_route.route('', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return jsonify({"error": "No image part"}), 400

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({"error": "Invalid image"}), 400

    current_app.logger.info(f'ocr filename: {image_file.filename}')
    response, status_code = process_ocr(image_file)  #
    current_app.logger.info(f'ocr response: {response}')
    return jsonify(response), status_code