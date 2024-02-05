from gpt import get_AI_response
import json

class WalkTheTalk:
    def __init__(self, language=None, analysis_types=None, business_name=None):
            self.language = language
            self.analysis_types = analysis_types
            self.business_name = business_name

    def swot(self, business_details):
        if "Swot" in self.analysis_types:
            if self.language == "english":
                self.system_message_swot = """\
You will take on the role of a professional business analyst. You will be \
provided with the details of a business and then you will think and carefully analyze \
their details and perform a swot analysis. Regarding your response, you can be as \
comprehensive as you want. Make sure to go as detailed as possible, in terms of explaining \
the four key aspects of the swot analysis for the business. \
"""             
                print(self.system_message_swot)
            else:
                self.system_message_swot = """\
אתה תיקח על עצמך את תפקידו של אנליסט עסקי מקצועי. תקבל את פרטי העסק ואז תחשוב ותנתח בזהירות \
את הפרטים שלהם ותבצע ניתוח SWOT. בנוגע לתגובתך, אתה יכול להיות כמה שרחב יותר. ודא להיכנס לפרטים \
ככל האפשר, במונחים של הסבר הארבעה היבטים העיקריים של ניתוח SWOT לעסק. \
"""
            print("Business-details: ", business_details)
            print("swot-message: ", self.system_message_swot)
            response = get_AI_response(business_details, system_message=self.system_message_swot)
            return response
    
    def strategic_narrative_builder(self, business_details):
        if "Strategic Narrative Builder" in self.analysis_types:
            if self.language == "english":
                self.system_message_narr_build = f"""\ 
Hello ChatGPT! Let's embark on crafting a captivating and detailed narrative for {self.business_name}.

Business Journey: Create a compelling story that vividly recounts the origins, evolution, and key \
milestones in the life of {self.business_name}. Include specific anecdotes, turning points, and pivotal \
moments that have defined its journey. Dive deep into the narrative, allowing the audience to \
visualize the business's history.

Values and Mission: Explicitly outline the core values and mission statement of {self.business_name}. \
Illustrate how these values and mission are deeply woven into the fabric of the business's story. \
Highlight moments where these values have been demonstrated and let them shine as guiding stars in the \
narrative.

Actionable Strategies: Provide actionable, practical storytelling strategies, content ideas, and thematic \
approaches that {self.business_name} can instantly integrate into its narrative. These strategies should be \
designed to engage the audience effectively, leaving a lasting impact and forging stronger connections.
    """
            
            else:
                self.system_message_narr_build = f"""\
שלום ChatGPT! בואו נצא ליצירת סיפור מרתק ומפורט עבור {self.business_name}.

מסע העסק: יצירת סיפור מרתק שמתאר בחיות את המקורות, ההתפתחות והנקודות המרכזיות \
בחיי {self.business_name}. כלול אנקדוטות ספציפיות, נקודות מפנה ורגעים מכריעים \
שהגדירו את מסעו. צלול לתוך הסיפור, ואפשר לקהל לראות את היסטוריית העסק.

ערכים ומשימה: תאר במפורש את הערכים המרכזיים והצהרת המשימה של {self.business_name}. \
המחש איך הערכים והמשימה משולבים לעומק באריג הסיפור של העסק. \
הדגש רגעים שבהם הוצגו הערכים האלה ותן להם לזרוח ככוכבים מנחים בסיפור.

אסטרטגיות מעשיות: ספק אסטרטגיות סיפור מעשיות, רעיונות לתוכן וגישות נושאיות \
ש-{self.business_name} יכול לשלב מייד בסיפור שלו. האסטרטגיות האלה צריכות להיות \
מעוצבות למעורבות יעילה של הקהל, להשאיר השפעה מתמשכת ולטפח קשרים חזקים יותר.
    """
            response = get_AI_response(business_details, system_message=self.system_message_narr_build)
            return response
    
    def vision_and_values_amplifier(self, business_details):
        if "Vision & Values Amplifier" in self.analysis_types:
            if self.language == "english":
                self.system_message_vision_amp = f"""\
Hello ChatGPT! Dive deeply into the vision and values of {self.business_name}, providing \
actionable strategies for their effective communication and embodiment in marketing \
strategies and organizational culture.

Vision Communication: Detail specific methods through which {self.business_name} can convey \
its vision clearly and compellingly across diverse customer touchpoints.
Values Integration: Propose practical measures for seamlessly integrating the business \
values into marketing materials, customer interactions, and internal practices.
Market Resonance: Offer actionable strategies to ensure that the vision and values \
resonate with the target audience, amplifying the brand's market positioning.
        """
            else:
                self.system_message_vision_amp = f"""\
שלום ChatGPT! צלול לעומק החזון והערכים של {self.business_name}, תוך מתן \
אסטרטגיות מעשיות לתקשורת יעילה והטמעתם באסטרטגיות שיווק \
ובתרבות הארגונית.

תקשורת חזון: פרט שיטות ספציפיות שבהן {self.business_name} יכול להעביר \
את החזון שלו בצורה ברורה ומשכנעת באמצעות נקודות מגע שונות עם הלקוח.
הטמעת ערכים: הצע צעדים מעשיים להטמעה חלקה של הערכים העסקיים \
בחומרים שיווקיים, אינטראקציות עם לקוחות ובמעשים פנימיים.
תהודה שוקית: הצע אסטרטגיות מעשיות להבטחת כך שהחזון והערכים \
יתהדו עם הקהל היעד, מחזקים את מיקומו של המותג בשוק.
        """
            
        response = get_AI_response(business_details, system_message=self.system_message_vision_amp)
        return response
    
    def usp_builder(self, business_details):
        if "Distinctive Edge and USP Builder" in self.analysis_types:
            if self.language == "english":
                self.system_message_usp_builder = f"""\
Hello ChatGPT! Let's pinpoint the unique attributes and value propositions \
that distinctly position {self.business_name} in the market.

Unique Offerings: Identify specific products, services, or features that set \
{self.business_name} apart. Elaborate on how these offerings create a competitive edge.
USP Formulation: Craft a Unique Selling Proposition that encapsulates the unique \
benefits and value offered by {self.business_name}. Ensure that the USP is concise, \
compelling, and customer-oriented.
Immediate Implementation: Outline actionable strategies that {self.business_name} can \
employ to communicate and leverage its differentiators and USP effectively in the \
market starting today
        """
            else:
                self.system_message_usp_builder = f"""\
שלום ChatGPT! בואו נזהה את המאפיינים הייחודיים וההצעות של הערך \
שממקמות את {self.business_name} באופן בולט בשוק.

הצעות ייחודיות: זהה מוצרים, שירותים או תכונות ספציפיות שמבדילות \
את {self.business_name}. הרחב על איך ההצעות האלה יוצרות יתרון תחרותי.
ניסוח USP: צור הצעת מכירה ייחודית (USP) שמסכמת את היתרונות הייחודיים \
והערך ש{self.business_name} מציעה. ודא שה-USP תמציתי, מרתק, ומוכוון ללקוח.
יישום מיידי: מתוד אסטרטגיות פרקטיות ש-{self.business_name} יכולה \
להשתמש כדי לתקשר ולנצל את היתרונות וה-USP שלה בשוק החל מהיום
        """
                
            response = get_AI_response(business_details, system_message=self.system_message_usp_builder)
            return response
        
    def customer_profile(self, business_details):
        if "Analyze Customer Profiling" in self.analysis_types:
            if self.language == "english":
                self.system_message_cus_prof = f"""\
Hello ChatGPT! Conduct a comprehensive analysis to develop a nuanced customer \
profile for {self.business_name}, ensuring that the profile is immediately actionable. \
Explore the following aspects:

Demographic Analysis: Detail the key demographic characteristics of the target \
customer, providing specific insights that {self.business_name} can use to tailor its offerings.

Behavioral Insights: Offer concrete observations on customer behaviors, preferences, \
and interactions with {self.business_name}, outlining steps to leverage these insights \
for enhanced customer experiences.

Strategic Recommendations: Provide precise strategies for {self.business_name} to align \
its offerings and marketing messages with the identified customer profile \
characteristics for immediate implementation.
"""

            else:
                self.system_message_cus_prof = f"""\
שלום ChatGPT! בצע ניתוח מקיף כדי לפתח פרופיל לקוח עדין עבור {self.business_name}, וודא \
שהפרופיל יהיה פעיל מיידית. חקור את ההיבטים הבאים:

ניתוח דמוגרפי: פרט את התכונות הדמוגרפיות המרכזיות של הלקוח המטרה, תוך \
מתן תובנות ספציפיות ש-{self.business_name} יכול להשתמש בהן כדי להתאים את ההצעות שלו.

תובנות התנהגותיות: הצע תצפיות ממשיות על התנהגויות, העדפות ואינטראקציות של \
הלקוחות עם {self.business_name}, תוך קווי דרך לניצול התובנות האלה לחוויות לקוח משופרות.

המלצות אסטרטגיות: מספק אסטרטגיות מדויקות ל-{self.business_name} כדי ליישר \
את ההצעות והמסרים השיווקיים עם התכונות של פרופיל הלקוח המזוהה ליישום מיידי.
"""

            response = get_AI_response(business_details, system_message=self.system_message_cus_prof)
            return response


    def marketing_platform_and_content_creation(self, business_details):
        if "Marketing Platforms & Content Creation" in self.analysis_types:
            if self.language == "english":
               self.system_message_mar_plat = f"""\
Hello ChatGPT! Create a tailored strategy that identifies the most \
effective marketing platforms for {self.business_name} and develops \
suitable content to engage the audience. Follow these steps:

Platform Identification: Specify the platforms that are most relevant \
for {self.business_name}, providing a rationale and immediate steps for \
establishing a presence on these platforms.

Content Development: Generate specific content ideas, themes, and formats \
that {self.business_name} can utilize to engage the audience and enhance \
visibility on the selected platforms.

Implementation Guidance: Offer detailed steps and best practices for \
{self.business_name} to execute the content strategy effectively across \
the chosen platforms starting today.
"""
                
            else:
                self.system_message_mar_plat = f"""\
שלום ChatGPT! צור אסטרטגיה מותאמת אישית שמזהה את הפלטפורמות השיווקיות \
היעילות ביותר עבור {self.business_name} ומפתחת תוכן מתאים למעורבות הקהל. פעל לפי השלבים הבאים:

זיהוי פלטפורמה: ציין את הפלטפורמות הרלוונטיות ביותר עבור {self.business_name}, \
מספק הסבר ושלבים מיידיים להקים נוכחות בפלטפורמות אלו.

פיתוח תוכן: צור רעיונות תוכן ספציפיים, נושאים ופורמטים \
ש-{self.business_name} יכולה להשתמש בהם כדי למעורב את הקהל ולשפר \
נראות על הפלטפורמות הנבחרות.

הנחיות ליישום: הצע שלבים מפורטים ומיטב המתודולוגיות עבור {self.business_name} \
לביצוע האסטרטגיה לתוכן באופן יעיל בפלטפורמות הנבחרות החל מהיום.
"""

                
            response = get_AI_response(business_details, system_message=self.system_message_mar_plat)
            return response


    def competitive_strategies(self, business_details):
        if "Competitive Analysis & Strategies" in self.analysis_types:
            if self.language == "english":
                self.system_message_comp_strat = f"""\
Hello ChatGPT! Conduct a competitive analysis for {self.business_name}, \
delivering insights that are actionable and strategically advantageous. \
Follow these steps:

Competitor Breakdown: Identify the primary competitors, detailing their \
strengths, weaknesses, and market positions. Offer specifics that are \
directly relevant to {self.business_name}.

Strategy Formulation: Based on the analysis, formulate specific strategies \
that {self.business_name} can implement immediately to enhance its competitive \
position.

Action Plans: Provide a clear, step-by-step action plan that {self.business_name} \
can follow to apply the insights from the competitive analysis for strategic advantage.
"""
            else:
                self.system_message_comp_strat = f"""\
שלום ChatGPT! בצע ניתוח תחרותי עבור {self.business_name}, \
מספק תובנות שהן פעילות ובעלות יתרון אסטרטגי. \
עקוב אחר השלבים הבאים:

ניתוח מתחרים: זהה את המתחרים העיקריים, מפרט את חוזקותיהם, \
חולשותיהם, ומיקומם בשוק. ספק פרטים שהם רלוונטיים באופן ישיר ל-{self.business_name}.

ניסוח אסטרטגיה: על בסיס הניתוח, צור אסטרטגיות ספציפיות \
ש-{self.business_name} יכולה ליישם מייד כדי לשפר את מעמדה התחרותי.

תוכניות פעולה: ספק תוכנית פעולה ברורה, שלב אחר שלב, ש-{self.business_name} \
יכולה לעקוב אחריה כדי ליישם את התובנות מהניתוח התחרותי לקידום אסטרטגי.
"""

            response = get_AI_response(business_details, system_message=self.system_message_comp_strat)
            return response


    def mar_funnel_strategy(self, business_details):
        if "Marketing Funnel Strategy" in self.analysis_types:
            if self.language == "english":
                self.system_message_funn_strat = f"""\
Define each stage of the funnel, describing the customer's \
journey and the objectives {self.business_name} should aim for \
at each point.

Strategic Tactics: Develop specific tactics, content ideas, \
and engagement strategies for each stage of the funnel, ensuring \
they are actionable and effective.

Optimization Guidance: Provide clear instructions on how to continuously \
optimize the funnel for improved performance and customer conversions, \
offering specific measures and adjustments.
"""
            else:
                self.system_message_funn_strat = f"""\
הגדר כל שלב במשפך, תאר את מסע הלקוח ואת המטרות ש-{self.business_name} \
צריכה לשאוף להשיג בכל נקודה.

טקטיקות אסטרטגיות: פתח טקטיקות ספציפיות, רעיונות לתוכן, \
ואסטרטגיות למעורבות לכל שלב במשפך, תוך הבטחת כך שהן יהיו פעילות ויעילות.

הנחיות לאופטימיזציה: ספק הוראות ברורות איך לאופטימזציה רציפה \
של המשפך לשיפור ביצועים והמרות לקוחות, מציע מדידות והתאמות ספציפיות.
"""

            response = get_AI_response(business_details, system_message=self.system_message_funn_strat)
            return response
        
    def kpi_strategy(self, business_details):
        if "Budget & KPI Strategy" in self.analysis_types:
            if self.language == "english":
                self.system_message_kpi_strat = f"""\
Hello ChatGPT! Develop a strategic plan for {self.business_name}'s marketing \
budgets and KPIs, ensuring that each aspect is clearly defined and immediately \
actionable. Here's how:

Budget Allocation: Present a detailed budget distribution across various marketing \
activities and platforms, providing a rationale for each allocation to guide \
{self.business_name}'s investment decisions.

KPI Definition: Define clear and measurable KPIs for each marketing activity, ensuring \
they align with {self.business_name}'s objectives and providing a basis for performance assessment.

Implementation Strategy: Offer a structured approach for {self.business_name} to implement, \
track, and optimize the budget and KPIs effectively, ensuring continuous improvement and \
alignment with business goals.
"""
            else:
                self.system_message_kpi_strat = f"""\
שלום ChatGPT! פתח תוכנית אסטרטגית עבור תקציבי השיווק וה-KPIs של {self.business_name}, \
ודא שכל אספקט מוגדר בבירור וניתן ליישום מיידי. הנה איך:

הקצאת תקציב: הצג הפצת תקציב מפורטת על פני פעילויות ופלטפורמות שיווק שונות, \
תוך מתן הסבר לכל הקצאה כדי להנחות את החלטות ההשקעה של {self.business_name}.

הגדרת KPI: הגדר KPIs ברורים וניתנים למדידה עבור כל פעילות שיווקית, \
ודא שהם מתיישרים עם מטרות {self.business_name} ומספקים בסיס להערכת ביצועים.

אסטרטגיה ליישום: הצע גישה מובנית עבור {self.business_name} ליישם, \
לעקוב ולאופטימז את התקציב וה-KPIs באופן יעיל, מבטיח שיפור רציף והתיישרות עם מטרות העסק.
"""

                
            response = get_AI_response(business_details, system_message=self.system_message_kpi_strat)
            return response
        
    
    def lead_journey_product_strategy(self, business_details):
        if "Lead Journey Product Strategy" in self.analysis_types:
            if self.language == "english":
                self.system_message_prod_strat = f"""\
Hello ChatGPT! Develop a strategic plan detailing the products or services \
{self.business_name} should offer at each stage of the lead journey. Here's how:

Primary Free Products: Recommend specific free products or services that can \
be offered initially, and provide detailed strategies for their promotion and delivery.

Basic to Premium Products: For each subsequent stage (basic, advanced, premium), \
identify suitable products or services, and outline precise strategies for \
positioning, pricing, and promotion.

Implementation Steps: Offer a step-by-step guide for {self.business_name} to \
implement the product offering strategy effectively, ensuring alignment with \
customer needs and business objectives.
"""
            else:
                self.system_message_prod_strat = f"""\
שלום ChatGPT! פתח תוכנית אסטרטגית המפרטת את המוצרים או השירותים \
ש-{self.business_name} צריכה להציע בכל שלב של מסע הלידים. הנה איך:

מוצרים חינמיים ראשוניים: המלץ על מוצרים או שירותים חינמיים ספציפיים שניתן \
להציע בתחילה, וספק אסטרטגיות מפורטות לקידום והפצה שלהם.

מוצרים בסיסיים עד פרימיום: לכל שלב עוקב (בסיסי, מתקדם, פרימיום), \
זהה מוצרים או שירותים מתאימים, ופרט אסטרטגיות מדויקות למיקום, תמחור, וקידום.

שלבי יישום: הצע מדריך שלב אחר שלב עבור {self.business_name} ליישום \
האסטרטגיה להצעת המוצרים באופן יעיל, וודא שיש התאמה עם צרכי הלקוחות ומטרות העסק.
"""

                response = get_AI_response(business_details, system_message=self.system_message_prod_strat)
                return response
            

    def content_strategy(self, business_details):
        if "Content Strategy" in self.analysis_types:
            if self.language == "english":
                self.system_message_cont_strat = f"""\
Hello ChatGPT! Assist in devising a precise content strategy that \
is meticulously tailored for various platforms, optimizing engagement, \
reach, and conversion. Here's how to master content on different \
platforms for {self.business_name}:

Facebook:

Identify types of content that resonate on Facebook.
Provide specific post ideas, optimal posting times, and engagement tactics.
Instagram:

Suggest visual content and storytelling approaches effective on Instagram.
Offer hashtag strategies and ideas for stories and IGTV.
LinkedIn:

Outline content strategies that enhance professional networking and B2B engagements.
Offer post and article ideas to bolster {self.business_name}'s industry authority.
TikTok:

Propose content that aligns with TikTok's dynamic and creative platform nature.
Offer ideas for leveraging trends and creating engaging short-form videos.
Twitter:

Develop strategies to optimize tweets for visibility and engagement.
Recommend content ideas, hashtags, and engagement tactics.
Email Marketing:

Provide strategies for content segmentation and personalization.
Suggest email formats and content that optimize open rates and conversions.
SEO:

Offer strategies for keyword optimization and improving online content visibility.
Suggest actionable on-page SEO tactics to enhance search engine rankings.
"""
            else:
                self.system_message_cont_strat = f"""\
שלום ChatGPT! עזור בפיתוח אסטרטגיית תוכן מדויקת שמותאמת בקפידה \
לפלטפורמות שונות, ממקסמת מעורבות, היקף, והמרה. הנה איך לשלוט \
בתוכן בפלטפורמות שונות עבור {self.business_name}:

Facebook:

זהה סוגי תוכן שמתקבלים היטב בפייסבוק.
ספק רעיונות לפוסטים, זמנים אופטימליים לפרסום, וטקטיקות מעורבות.
Instagram:

הצע תוכן ויזואלי ודרכי סיפור שיעילים באינסטגרם.
הצע אסטרטגיות להאשטגים ורעיונות לסיפורים ו-IGTV.
LinkedIn:

פרט אסטרטגיות תוכן שמחזקות רשתות מקצועיות ואינטראקציות B2B.
הצע רעיונות לפוסטים ומאמרים לחיזוק סמכות התעשייה של {self.business_name}.
TikTok:

הצע תוכן התואם לאופי הדינמי והיצירתי של פלטפורמת TikTok.
הצע רעיונות לניצול מגמות ויצירת וידאו קצרים מעניינים.
Twitter:

פתח אסטרטגיות למקסום נראות ומעורבות של ציוצים.
המלץ על רעיונות לתוכן, האשטגים, וטקטיקות מעורבות.
שיווק באימייל:

ספק אסטרטגיות לסגמנטציה ואישיות של תוכן.
הצע פורמטים של אימיילים ותוכן שממקסמים שיעורי פתיחה והמרות.
SEO:

הצע אסטרטגיות לאופטימיזציה של מילות מפתח ושיפור נראות תוכן מקוון.
הצע טקטיקות SEO עמודים פעילות לשיפור דירוגים במנועי חיפוש.
"""

            response = get_AI_response(business_details, system_message=self.system_message_cont_strat)
            return response
        
    def tailor_customer_profile(self, business_details):
        if "Tailor Customer Profile" in self.analysis_types:
            if self.language == "english":
                self.system_message_tail_cus_prof = f"""\
Hello ChatGPT! Develop a precise customer profile that aligns \
closely with {self.business_name}'s offerings and objectives, ensuring \
that the profile is actionable and strategically advantageous. Here's \
how to align your customer profile with your business needs:

Demographic Details: Provide a detailed breakdown of the customer demographics \
that {self.business_name} should target, ensuring these details are actionable and relevant.

Psychographic and Behavioral Insights: Deliver insights into customer behaviors, \
interests, and preferences, offering strategies for {self.business_name} to align its offerings accordingly.

Strategic Implementation: Offer specific strategies for {self.business_name} to tailor its products, services, \
and marketing efforts based on the developed customer profile to enhance relevance and appeal.
"""
            else:
                self.system_message_tail_cus_prof = f"""\
שלום ChatGPT! פתח פרופיל לקוח מדויק שמתיישר \
עם ההצעות והמטרות של {self.business_name}, תוך הבטחת כך שהפרופיל \
יהיה פעיל ובעל יתרון אסטרטגי. הנה איך להתאים את פרופיל הלקוח לצרכי העסק שלך:

פרטים דמוגרפיים: ספק פירוט מפורט של הדמוגרפיה של הלקוחות \
ש-{self.business_name} צריכה למקד, תוך הבטחת כך שהפרטים האלו יהיו פעילים ורלוונטיים.

תובנות פסיכוגרפיות והתנהגותיות: מספק תובנות לגבי התנהגויות, \
עניינים, והעדפות של הלקוחות, תוך הצעת אסטרטגיות ל-{self.business_name} להתאים את ההצעות שלה בהתאם.

יישום אסטרטגי: הצע אסטרטגיות ספציפיות ל-{self.business_name} להתאים את המוצרים, השירותים, \
ומאמצי השיווק שלה בהתבסס על הפרופיל הלקוח שפותח להגביר הרלוונטיות והמשיכה.
"""

            response = get_AI_response(business_details, system_message=self.system_message_tail_cus_prof)
            return response
        
    def email_marketing_innovation(self, business_details):
        if "Email Marketing Innovation" in self.analysis_types:
            if self.language == "english":
                self.system_message_email_inn = f"""\
Hello ChatGPT! Generate innovative product ideas that {self.business_name} \
can effectively promote through email marketing to penetrate the market \
and engage customers. Here's how to invigorate your email marketing approach:

Product Ideas: Propose specific products, like blueprints or tips, that will capture the audience's interest and encourage engagement.

Email Marketing Strategies: Develop detailed strategies for promoting these products through email, ensuring that the content is \
engaging and the call-to-action is compelling.

Action Plan: Provide a clear action plan that outlines how {self.business_name} can implement these product ideas and email marketing \
strategies for immediate market penetration and customer engagement.
"""
            else:
                self.system_message_email_inn = f"""\
שלום ChatGPT! צור רעיונות מוצר חדשניים ש-{self.business_name} \
יכולה לקדם ביעילות באמצעות שיווק בדואר אלקטרוני כדי לחדור לשוק \
ולהערב את הלקוחות. הנה איך לחדש את גישת השיווק בדואר אלקטרוני שלך:

רעיונות למוצר: הצע מוצרים ספציפיים, כמו תוכניות או טיפים, שיתפסו את עניין הקהל ויעודדו מעורבות.

אסטרטגיות שיווק בדואר אלקטרוני: פתח אסטרטגיות מפורטות לקידום המוצרים האלה בדואר אלקטרוני, תוך הבטחת כך שהתוכן \
יהיה מעניין והקריאה לפעולה משכנעת.

תוכנית פעולה: מספק תוכנית פעולה ברורה המתארת איך {self.business_name} יכולה ליישם את הרעיונות הללו למוצרים ואסטרטגיות שיווק \
בדואר אלקטרוני לחדירה מיידית לשוק ומעורבות לקוחות.
"""

            response = get_AI_response(business_details, system_message=self.system_message_email_inn)
            return response


def validate_data(language, business_details):
    """
    Validate the user input for the business details
    """
    if language == "english":
        system_message = f"""\
consider yourself a professional business strategy advisor. I want you to study and analyze the data given by the user in the following fields
{business_details}

This data is being sent from frontend. I will provide you some sample data as a reference which you can use to validate the data sent from frontend.
Validation Data:
{{
    "business_name": "GreenLeaf Organics",
    "industry": "Health Food & Supplements",
    "narrative": "GreenLeaf Organics is dedicated to providing high-quality organic health foods and supplements. Our mission is to promote wellness through natural products.",
    "vision_values": "Our vision is to be a leader in the organic health industry, valuing sustainability, health, and natural living.",
    "target_audience": "Health-conscious individuals, aged 25-45, interested in natural and organic products.",
    "products_and_services": "Organic health foods, dietary supplements, wellness guides.",
    "products_and_services_benefits": "Enhances overall health, supports sustainable practices, non-GMO and chemical-free products.",
    "marketing_objectives_and_goals": "Increase brand awareness by 30% in the next year, expand online sales by 40%, enter two new regional markets.",
    "competitor": "Nature's Best Organics",
    "active_social_media_platforms": ["Facebook", "Instagram", "Twitter"],
    "marketing_budget": "50000"
}}

I have provided you this sample data to tell you what the business details look like.
You will return your response in the following JSON format:
{{
    "correctData": true or false,
    // if correctData is false, then you will return the field, for which you think the user should make improvement
    "fieldName": "reason why you think the user should make improvement",
    "fieldName": "reason why you think the user should make improvement",
    and so on...
}}
"""
        response = get_AI_response(business_details, model="gpt-4-1106-preview", system_message=system_message, response_format={"type": "json_object"})
        print(response)
        json_response = json.loads(response)
        return json_response
    
    else:
        system_message = f"""\
לשקול את עצמך יועץ אסטרטגיה עסקית מקצועי. אני רוצה שתלמד ותנתח את הנתונים שניתנו על ידי המשתמש בתחומים הבאים
{business_details}

זו הנתונים נשלחים מהחזית. אני אספק לך דוגמת נתונים כהתייחסות שתוכל להשתמש בה כדי לאמת את הנתונים הנשלחים מהחזית.
Validation Data:
{{
    "business_name": "nextweb",
    "industry": "שיווק וקידום עסקים בדיגיטל",
    "narrative": "",
    "vision_values": "החזון שלי הוא לאפשר לכמה שיותר עסקים קטנים לבנות מערך שיווק מקצועי בעסק שלהם כדי שיוכלו לקבל תוצאות מתהליכי שיווק מדויקים עבורם.",
    "target_audience": "עסקים קטנים ויזמים",
    "products_and_services": "יועצת, מרצה, כותבת אסטרטגיות שיווק, תוכנית שיווק, מטמיע תהליכי שיווק ברשת, קידום אורגני, קידום ממומן, רשתות חברתיות, גוגל, בניית תשתיות, אתרים, דפי נחיתה, שיווק במייל",
    "products_and_services_benefits": "",
    "marketing_objectives_and_goals": "המטרה שלי היא להגיע ל-100,000 עסקים קטנים ולשכנע 10% מהם להשתמש באפליקציה שלי שבונה אסטרטגיית שיווק בלחיצת כפתור, בשני שלבים",
    "competitor": "קידום ברשתות חברתיות",
    "active_social_media_platforms": ["Facebook", "Instagram", "YouTube", "TikTok", "LinkedIn"],
    "marketing_budget": "1000 ש\\\"ח לחודש"
}}

סיפקתי לך נתונים לדוגמה כדי להראות לך איך נראים פרטי העסק.
תחזיר את התגובה שלך בפורמט JSON הבא:
{{
    "correctData": true or false,
    // אם correctData הוא false, אז תחזיר את השדה, עבורו אתה חושב שהמשתמש צריך לשפר
    "fieldName": "סיבה שבגינה אתה חושב שהמשתמש צריך לשפר",
    "fieldName": "סיבה שבגינה אתה חושב שהמשתמש צריך לשפר",
    וכן הלאה...
}}

"""
        response = get_AI_response(business_details, model="gpt-4-1106-preview", system_message=system_message, response_format={"type": "json_object"})
        print(response)
        json_response = json.loads(response)
        return json_response