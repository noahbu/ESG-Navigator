import streamlit as st
from esg_navigator.backend.helper import add_logo


st.set_page_config(
    page_title="Education and FAQs",
    page_icon="👋",
    layout="wide"
)
#Add logo to the sidebar
add_logo()  
#Add signature to the sidebar
st.sidebar.markdown('''
        ---
        Created with ❤️ by UComply.
        ''')


def load_assets():
    # Load CSS
    css_file_path = os.path.join(os.path.dirname(__file__), "styles.css")
    with open(css_file_path, "r") as f:
        css = f.read()

    # Load JavaScript
    js_file_path = os.path.join(os.path.dirname(__file__), "fixes.js")
    with open(js_file_path, "r") as f:
        js = f.read()


st.title('Education and FAQs')


st.markdown(""" 

### Overview
            """)


width = max(80, 0.01)
side = max((100 - width) / 2, 0.01)

_, container, _ = st.columns([side, width, side])
container.video(data="https://www.youtube.com/watch?v=raNpbPBNyhI")

            

st.markdown(""" 

### Table of Contents

1. [What is Unlawful Harassment?](#1-what-is-unlawful-harassment)
2. [So What is Workplace Harassment?](#2-so-what-is-workplace-harassment)
3. [What are Protected Grounds?](#3-what-are-protected-grounds)
4. [Types of Assessment](#4-types-of-assessment)
5. [Bullying and Aggressive Behavior](#5-bullying-and-aggressive-behavior)
6. [Forms of Harassment](#6-forms-of-harassment)
7. [What Is Retaliation/Victimization?](#7-what-is-retaliation-victimization)




## 1. What is Unlawful Harassment?

Unlawful harassment is defined by laws that identify specific conduct and situations. If bad behavior meets the legal definition, it's "harassment." If it doesn't, it's still an issue requiring attention—just probably not legal attention. There's a big difference between:

"That person is being rude to me" *and* "That person is harassing me"

The way you describe and label conduct influences the response and remedy you'll receive. Be thoughtful in your description and make it easy for management and HR partners to respond in a way that addresses and remedies the situation.

## 2. So What is Workplace Harassment?

Workplace harassment is conduct that is based on, or motivated by, any legally protected ground and several other legal criteria that makes the conduct not tolerated by Celonis.

Some Take-Aways for You:
- "Harassment" is unlawful conduct that meets several legal criteria.
- Even if behavior doesn't meet the legal criteria for "harassment," it can still be a big problem that violates policies.
- Workplace harassment is unlawful conduct that discriminates against someone based on at least one protected characteristic.

## 3. What are Protected Grounds?

"Harassment" involves conduct motivated by, or focused on, protected grounds. But what are "protected grounds" and which ones apply where you work? Protected characteristics are personal characteristics that governments have decided should not influence or factor into workplace actions or decisions.

### Examples of Protected Grounds:
1. Gender, Gender Identity, and Gender Expression: Gender may include a person's sex assigned at birth and also includes gender identity and gender expression. Gender identity is a person's concept of themselves as a man, woman, a blend of both, or neither, regardless of their sex assigned at birth. Gender expression refers to a person's gender-related appearance or behavior, whether or not stereotypically associated with the person's assigned sex at birth, e.g., dress, grooming, mannerisms.

2. Sexual Orientation: Sexual orientation describes a pattern of attraction (emotional, romantic, sexual, or some combination of these) to the opposite sex, the same sex, or both sexes, and the genders that accompany them.

3. Age: Age protections usually apply to people over a certain age (e.g., over 40) but sometimes protection can extend to any age (i.e., being young).

4. National Origin and Ancestry: National origin and ancestry refer to an individual's (or their ancestors') place of origin, nation, tribe, caste, or other identifiable group of people from which a person descends. This also includes having the physical, cultural, or linguistic characteristics of a national origin group.

5. Race and Color: Race is a social tool used to categorize people into distinct populations or groups by heritable characteristics, geographic ancestry, culture, history, language, physical appearance, ethnicity, and social status. Color refers to a person's skin color and can be used to compare skin color between races or within the same race.

6. Religion and Belief: Religion and creed refer to a set of beliefs concerning the cause, nature, and purpose of the universe, usually involving devotional and ritual observances, and often containing a moral code governing the conduct of human affairs.

7. Marital or Family Status: "Marital status" refers to the real or perceived marital status, e.g., married, widowed, divorced, single or unmarried with same-sex or opposite-sex partner. "Family status" refers to all characteristics of a person's family, including the lack of family, the number or ages of family members, etc.

8. Record of Offenses: "Record of offenses" refers to criminal or penal offenses for which a person has been convicted. In most cases, if unrelated to the job requirements, a record of offenses may not be used to bar employment as applicable locally. Also, where an individual has obtained a pardon for the past offense, a record of offenses may usually not be used to bar employment. There may be exceptions to these prohibitions for offenses that are particularly severe, even if they are unrelated to the job requirements.

9. Disability: Disability is broadly defined as a mental or physical impairment, disorder, or condition that limits a major life activity. In some countries, there are legal definitions of levels of impairment or disability.

10. Sex: Sex includes being male, female, intersex, or transgender. It also includes the state of pregnancy and everything encompassing it.

Why Some Traits, But Not Others?
Protected grounds vary from country to country. And many organizations have adopted policies that go beyond the protected grounds defined by law. This makes it critical for you to familiarize yourself with local laws and your organization's harassment policies. Please refer to Celonis's Policy at the end of the course.

Some Take-Aways for You:
- Protected grounds are personal characteristics that country, federal, province, state, or local governments have decided should not influence or factor into our workplace actions or decisions.
- Sexual harassment is unlawful discrimination based on sex, sexual orientation, self-identified or perceived sex, gender expression, gender identity, and/or the status of being transgender.
- There are many other types of harassment to avoid.

## 4. Types of Assessment

So, we know that conduct involves "protected grounds" when it's illegal. But what else is involved? Two types of Harassment:

1. Quid Pro Quo:
"Quid pro quo" is Latin for "this for that"—meaning "you do this for me and I'll do that for you." It's a type of sexual harassment when managers knowingly—or even unknowingly—abuse their power. And because it involves an abuse of power, only managers or supervisors can engage in this kind of harassment. A co-worker doesn't have that kind of power over someone and so can't engage in quid pro quo harassment.

2. Hostile Work Environment:
"Hostile work environment" can be sexual harassment, age harassment, race harassment—or harassment based on any protected ground. A hostile work environment always involves unwelcome conduct that:
- Is directed at someone because of a protected ground and
- Has the effect of interfering with an individual's work performance or creating an intimidating, hostile, or offensive work environment.

Quid Pro Quo Examples:
- Offering or granting better working conditions, promotions, or other favorable opportunities in exchange for a sexual relationship
- Threatening adverse working conditions—like demotions, shift alterations, changes in work locations, or denials of opportunities—if a sexual relationship is refused
- Using pressure, threats, or physical acts to force a sexual relationship
- Retaliating for refusing a sexual relationship

=> An Offer You Can't Refuse:
So even though quid pro quo situations can take many shapes, they all share one thing in common. Someone in a position of authority makes an offer or request that the less powerful person feels they can't say "no" to.

Second Type of Harassment: Hostile Work Environment:
It's a hostile work environment when unwelcome conduct:
- Is directed at someone because of a protected ground, AND
- Has the purpose and effect of interfering with an individual's work performance or creating an intimidating, hostile, or offensive work environment.

Stereotyping:

Sometimes unlawful situations involve "sex stereotyping" or other types of stereotyping. This occurs when conduct or personality traits are judged inappropriate because they don't conform to how other people think someone should act or look. It also involves people with jobs that are, or were in the past, typically performed by a different gender or sex. In these situations, offensive conduct or comments are often aimed at someone's looks, speech, personality, or lifestyle.

Doesn't Matter Who...

Hostile work environment situations are the most common harassment situations because people causing the situation can be:
- Managers
- Co-workers
- Anyone interacting with employees

It's not only limited to managers!

Some Take-Aways for You:
- There are two types of harassment — quid pro quo and hostile work environment.
- Quid pro quo is a "this for that" exchange, involving an abuse of power.
- A hostile work environment is created by unwelcome conduct that is based on any protected ground (not just sex) and which changes the workplace culture.

## 5. Bullying and Aggressive Behavior

Bullying is conduct "with malice that a reasonable person would find hostile, offensive, and unrelated to an employer's legitimate business interests."

Is Bullying Harassment or Illegal?

=> Workplace bullying violates the law in some places around the world. But even in places that don't outlaw bullying, people are protected from conduct motivated by protected grounds. We address bullying through our policies and established norms of behavior.

Some Take-Aways for You:
- No matter the situation, bullying is not the way to handle things.
- Bullying and causing fear erodes team dynamics and creates an unhealthy workplace culture.
- Anyone who feels entitled to bully someone may feel entitled to harass or break other workplace norms.
- Employees should contact their managers or dedicated HRBP if they think they have been bullied.

## 6. Forms of Harassment:

Verbal forms of harassment include:
- Slurs
- Stereotyping
- Comments and jokes based on any protected grounds
- Sexual jokes and comments
- Inappropriate comments about a person's body or clothing
- Telling rumors
- Repeatedly asking someone out
- Requesting sexual favors
- Personal sexual questions

Physical Forms of Conduct:
Physical forms of harassment include:
- Impeding or blocking movement
- Following someone
- Inappropriate touching of a person or their clothing
- Grabbing or leaning on a person
- Kissing, hugging, patting, or massaging
- Staring
- Giving inappropriate gifts
- Assault
- Battery

Visual Forms of Conduct:
Visual forms of harassment include:
- Offensive posters
- Pictures
- Cartoons
- Drawings
- Screensavers
- Memes
- Pornographic images
- Offensive backgrounds in video calls

Some Take-Aways for You:
- Any physical, visual, or verbal conduct that influences the workplace could be a potential form of harassment.
- There will always be new forms of co-worker interaction, and harassment can affect any of them.
- We have different views on what conduct is respectful or not.
- Be intentional and practice your social awareness skills to support the respect needs of your co-workers.

## 7. What Is Retaliation or Victimization?

Retaliation/Victimization occurs when employees experience negative job actions because they engage in a protected activity like:
- Making a formal or informal complaint
- Opposing discrimination or harassment
- Assisting another's complaint of harassment
- Participating in an investigation led by the employer or a governmental agency
- Testifying in a court proceeding

To establish victimization, a person must show:
- They engaged in a "protected activity"
- They suffered a negative job action
- There was a causal link between the protected activity and the negative job action

Complaints are not always packaged neatly and communicated clearly. Managers who are aware of a complaint that does, or even may, involve harassment should contact HRBPs or any of the other ways to report a complaint and make sure not to retaliate or victimize anyone involved in raising or discussing the complaint.

What Does Victimization Look Like?
Victimization includes retaliatory actions, such as:
- Demotions
- Sudden changes in work schedules or work locations
- Poor performance reviews
- Assigning more work or demeaning tasks
- Reducing salary
- Unreasonable nit-picking (fault-finding)
- Ostracism by co-workers
- Anything that would discourage you from making future complaints

Victimization is Never Allowed
You might think the law only protects employees when they submit complaints that are substantiated. But that's wrong. Employees are protected from victimization as long as the complaints were made in good faith (they had good reason to think the information shared in the complaint was true) so they'll feel safe raising concerns. So retaliation is never okay—even if a good faith complaint turns out to be unsubstantiated.

Some Take-Aways for You:
- Everyone has the right to make a complaint and be free from retaliation/victimization.
- Victimization occurs when employees suffer negative job actions because they complained of harassment, participated in an investigation, or engaged in other protected activity.
- Even repeatedly avoiding an employee can feel retaliatory if the avoidance turns into ostracism against the employee.
- Anyone engaging in victimization can be disciplined or terminated.



 """)