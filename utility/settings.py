import os
from pathlib import Path
from utility.extract_json_data import extract_data_from_json_file

BASE_DIR = Path(__file__).resolve().parent
API_COMMON_PREFIX = '/arunangshu_pramanik/portfolio/v1'

HOST = os.getenv('HOST', '0.0.0.0')
PORT = int(os.getenv('PORT', '8080'))
DEBUG_MODE = "True" if os.getenv('DEBUG_MODE', True) in [True, 'True', 1, '1', 'true', 'TRUE'] else False
RECEIVER_EMAIL = os.getenv('RECEIVER_EMAIL')
RECEIVER_PASSWORD = os.getenv('RECEIVER_PASSWORD')
EMAIL_SERVER = os.getenv('EMAIL_SERVER')
EMAIL_PORT = int(os.getenv('EMAIL_PORT'))
EMAIL_STARTTLS = "True" if os.getenv('EMAIL_STARTTLS', True) in [True, 'True', 1, '1', 'true', 'TRUE'] else "False"
EMAIL_SSL_TLS = "True" if os.getenv('EMAIL_SSL_TLS', True) in [True, 'True', 1, '1', 'true', 'TRUE'] else "False"
USE_CREDENTIALS = "True" if os.getenv('USE_CREDENTIALS', True) in [True, 'True', 1, '1', 'true', 'TRUE'] else "False"
VALIDATE_CERTS = "True" if os.getenv('VALIDATE_CERTS', True) in [True, 'True', 1, '1', 'true', 'TRUE'] else "False"


personal_info_file = os.path.join(f'{BASE_DIR.parent}/information', 'personal_info.json')
experience_file = os.path.join(f'{BASE_DIR.parent}/information', 'experience.json')
skills_file = os.path.join(f'{BASE_DIR.parent}/information', 'skills.json')
education_details_file = os.path.join(f'{BASE_DIR.parent}/information', 'education_details.json')
profile_summary_file = os.path.join(f'{BASE_DIR.parent}/information', 'profile_summary.json')
awards_recognitions_file = os.path.join(f'{BASE_DIR.parent}/information', 'awards_recognitions.json')

personal_info_data = extract_data_from_json_file(json_file_path=personal_info_file)
experience_data = extract_data_from_json_file(json_file_path=experience_file)
skills_data = extract_data_from_json_file(json_file_path=skills_file)
education_details_data = extract_data_from_json_file(json_file_path=education_details_file)
profile_summary_data = extract_data_from_json_file(json_file_path=profile_summary_file)
awards_recognitions_data = extract_data_from_json_file(json_file_path=awards_recognitions_file)


