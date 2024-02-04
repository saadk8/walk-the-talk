from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
import os
from custom_logger import CustomTimedRotatingFileHandler
from datetime import datetime
from walk_the_talk import WalkTheTalk, validate_data
import threading
import requests
from gpt import get_AI_response


if not os.path.exists('logs'):
    os.makedirs('logs')

date_string = datetime.now().strftime("%Y-%m-%d")

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = CustomTimedRotatingFileHandler('logs', when="midnight", interval=1, backupCount=5)
formatter = logging.Formatter('%(asctime)s - %(levelname)s %(name)s %(threadName)s : %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

app = Flask(__name__)
CORS(app)

type_mapping = {
    "Swot": "sw",
    "Strategic Narrative Builder": "snb",
    "Business Identity - Vision, Values and Differentiation": "vva",
    "Customer Profile": "tcp",
    "Marketing Funnel Strategy": "mfs",
    "Marketing Platforms & Content": "mpcc",
    "Competitors": "cmptit",
    "Budget & KPI Strategy": "bks",
    "Marketing plan - 12 Month": "mp12m",
    # Hebrew mappings (if different, add them here, assuming they're the same for simplicity)
    # "Swot": "sw",
    # "הנחיות לכתיבת נרטיב": "snb",
    # "זהות עסקית": "vva",
    # "קהלי יעד": "tcp",
    # "אסטרטגיית משפך שיווקי": "mfs",
    # "פלטפורמות ותוכן שיווקי": "mpcc",
    # "ניתוח מתחרים בעסק": "cmptit",
    # "תקציבים ונתוני פרסום": "bks",
    # "תוכנית שיווק": "mp12m"
}

@app.route('/api/v1/test', methods=['GET'])
def test():
    return jsonify({'message': 'Hello World. !'}), 200

@app.route('/api/v1/analysis', methods=['POST'])
def analysis():
    try: 
        payload = request.json
        logger.info(f"Received payload: {payload}")
        language = request.json['language']
        analysis_types = request.json['analysis_types']
        business_name = request.json['business_name']
        industry = request.json['industry']
        narrative = request.json['narrative']
        vision_values = request.json['vision_values']
        usp = request.json['usp']
        target_audience = request.json['target_audience']
        products_and_services = request.json['products_and_services']
        marketing_objectives_and_goals = request.json['marketing_objectives_and_goals']
        competitor = request.json['competitor']
        active_social_media_platforms = request.json['active_social_media_platforms']
        marketing_budget = request.json['marketing_budget']

        language_to_snid = {'english': '1', 'hebrew': '2'}
        snid = language_to_snid.get(language)
        prompts = {}

        # Iterate over each analysis type and construct the URL
        for analysis_type in analysis_types:
            type_code = type_mapping.get(analysis_type)  # Get the corresponding type code
            if type_code:
                logger.info(f"Fetching prompts for analysis type: {analysis_type} and type code: {type_code}")
                url = f'https://walkthetalk.marketing/wp-json/custom/v1/ai_prompts/?type={type_code}&snid={snid}'
                # Assuming you want to send a request to each URL and collect the responses
                response = requests.get(url)
                if response.status_code == 200:
                    prompts[analysis_type] = response.json()
                else:
                    logger.error(f"Error fetching prompts for analysis type: {analysis_type}")
            else:
                logger.error(f"Invalid analysis type: {analysis_type}")

        business_details = f"""\
Business Name: {business_name}
Industry: {industry}
Narrative: {narrative}
Vision and Values: {vision_values}
USP: {usp}  
Target Audience: {target_audience}
Products and Services: {products_and_services}
Marketing Objectives and Goals: {marketing_objectives_and_goals}
Competitor: {competitor}
Active Social Media Platforms: {active_social_media_platforms}
Marketing Budget: {marketing_budget} \
        """

        results = {}
        def worker1():
            results['swot_analysis'] = get_AI_response(system_message=prompts['Swot'], prompt=business_details)
        def worker2():
            results['strategic_narrative_builder'] = get_AI_response(system_message=prompts['Strategic Narrative Builder'], prompt=business_details)
        def worker3():
            results['business_identity'] = get_AI_response(system_message=prompts['Business Identity - Vision, Values and Differentiation'], prompt=business_details)
        def worker4():
            results['customer_profile'] = get_AI_response(system_message=prompts['Customer Profile'], prompt=business_details)
        def worker5():
            results['marketing_funnel_strategy'] = get_AI_response(system_message=prompts['Marketing Funnel Strategy'], prompt=business_details)
        def worker6():
            results['marketing_platforms_content'] = get_AI_response(system_message=prompts['Marketing Platforms & Content'], prompt=business_details)
        def worker7():
            results['competitors'] = get_AI_response(system_message=prompts['Competitors'], prompt=business_details)
        def worker8():
            results['budget_kpi_strategy'] = get_AI_response(system_message=prompts['Budget & KPI Strategy'], prompt=business_details)
        def worker9():
            results['marketing_plan_12_month'] = get_AI_response(system_message=prompts['Marketing plan - 12 Month'], prompt=business_details)

        threads = []
        for worker in [worker1, worker2, worker3, worker4, worker5, worker6, worker7, worker8, worker9]:
            thread = threading.Thread(target=worker)
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
        return jsonify({'message': 'Success', 'results': results}), 200
    except Exception as e:
        logger.error(e)
        return jsonify({'message': 'Error'}), 500

@app.route('/api/v1/validate', methods=['POST'])
def validate():
    language = request.json['language']
    analysis_types = request.json['analysis_types']
    business_name = request.json['business_name']
    industry = request.json['industry']
    narrative = request.json['narrative']
    vision_values = request.json['vision_values']
    usp = request.json['usp']
    target_audience = request.json['target_audience']
    products_and_services = request.json['products_and_services']
    marketing_objectives_and_goals = request.json['marketing_objectives_and_goals']
    competitor = request.json['competitor']
    active_social_media_platforms = request.json['active_social_media_platforms']
    marketing_budget = request.json['marketing_budget']

    business_details = f"""\
Business Name: {business_name}
Industry: {industry}
Narrative: {narrative}
Vision and Values: {vision_values}
USP: {usp}  
Target Audience: {target_audience}
Products and Services: {products_and_services}
Marketing Objectives and Goals: {marketing_objectives_and_goals}
Competitor: {competitor}
Active Social Media Platforms: {active_social_media_platforms}
Marketing Budget: {marketing_budget} \
        """
    
    results = validate_data(language, business_details)
    return jsonify({'message': 'Success', 'results': results}), 200



if __name__ == '__main__':
    app.run(debug=True)