from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
import os
from custom_logger import CustomTimedRotatingFileHandler
from datetime import datetime
from walk_the_talk import WalkTheTalk, validate_data
import threading


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

@app.route('/api/v1/test', methods=['GET'])
def test():
    return jsonify({'message': 'Hello World. !'}), 200

@app.route('/api/v1/analysis', methods=['POST'])
def analysis():
    try: 
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
        walk_the_talk = WalkTheTalk(language, analysis_types, business_name)
        results = {}
        def worker1():
            results['swot_analysis'] = walk_the_talk.swot(business_details)
        def worker2():
            results['strategic_narrative_builder'] = walk_the_talk.strategic_narrative_builder(business_details)
        def worker3():
            results['vision_and_values_amplifier'] = walk_the_talk.vision_and_values_amplifier(business_details)
        def worker4():
            results['distinctive_edge_and usp_builder'] = walk_the_talk.usp_builder(business_details)
        def worker5():
            results['analyze_customer_profiling'] = walk_the_talk.customer_profile(business_details)
        def worker6():
            results['marketing_platform_and_content_creation'] = walk_the_talk.marketing_platform_and_content_creation(business_details)
        def worker7():
            results['competitive_analysis_and_strategies'] = walk_the_talk.competitive_strategies(business_details)
        def worker8():
            results['marketing_funnel_strategy'] = walk_the_talk.mar_funnel_strategy(business_details)
        def worker9():
            results['budget_and_kpi_strategy'] = walk_the_talk.kpi_strategy(business_details)
        def worker10():
            results['lead_journey_and_product_strategy'] = walk_the_talk.lead_journey_product_strategy(business_details)
        def worker11():
            results['content_strategy'] = walk_the_talk.content_strategy(business_details)
        def worker12():
            results['tailor_customer_profile'] = walk_the_talk.tailor_customer_profile(business_details)
        def worker13():
            results['email_marketing_innovation'] = walk_the_talk.email_marketing_innovation(business_details)

        threads = []
        for worker in [worker1, worker2, worker3, worker4, worker5, worker6, worker7, worker8, worker9, worker10, worker11, worker12, worker13]:
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