from flask import Flask, render_template, request, redirect
learn_data = [
    {
        "title": "What is Americano?",
        "content": "An Americano is a coffee drink made by adding hot water to a shot of espresso. This process creates a coffee that has a similar strength to regular brewed coffee but retains the rich flavor of espresso. It is popular because it balances intensity and smoothness, making it enjoyable for many coffee drinkers.",
        "image": "/static/images/americano.jpg"
    },
    {
        "title": "Types of Americano",
        "content": "There are different types of Americano depending on how it is prepared. A single shot Americano is lighter and less intense, while a double shot creates a stronger and richer flavor. Additionally, the roast level of the beans, such as light or dark roast, also affects the overall taste and aroma of the drink.",
        "image": "/static/images/americano.jpg"
    },
    {
        "title": "Bitter Taste",
        "content": "Bitterness in coffee is a common taste characteristic that comes from compounds released during brewing. When coffee is over-extracted, it becomes more bitter and less pleasant. This bitterness can feel strong and sharp on the tongue, and understanding it helps you control the brewing process to achieve a balanced flavor.",
        "image": "/static/images/americano.jpg"
    },
    {
        "title": "Ingredients & Tools",
        "content": "To make an Americano, you need a few simple ingredients and tools. The main components are freshly ground coffee beans and hot water. An espresso machine is used to extract the coffee properly. The quality of the beans and the freshness of the grind play a major role in the final taste of the drink.",
        "image": "/static/images/americano.jpg"
    },
    {
        "title": "Coffee Beans",
        "content": "Coffee beans are one of the most important factors that influence the taste of an Americano. Different types of beans produce different flavor profiles, ranging from smooth and mild to strong and bitter. By exploring different beans, you can understand how each type affects the final taste of your coffee.",
        "action": "/learn/6"
    },
    {
        "title": "Best Beans",
        "content": "Arabica beans are often considered the best choice for making an Americano because of their smooth, balanced, and slightly acidic flavor. They are less bitter compared to Robusta beans, making them more enjoyable for most people. Choosing the right beans can significantly improve your overall coffee experience.",
        "image": "/static/images/beans/arabica.png"
    },
    {
        "title": "Temperature",
        "content": "Temperature plays a crucial role in making a good Americano. The ideal temperature for brewing espresso is between 90 to 96 degrees Celsius. If the water is too hot, it can over-extract the coffee and make it bitter. If it is too cold, the coffee may taste weak and underdeveloped.",
        # "image": "/static/images/temperature.jpg"
    },
    {
        "title": "Step-1 Pull a ‘blank shot’",
        "content": "Before brewing espresso, run hot water through the machine with an empty portafilter (no coffee). This quick “blank shot” warms up the group head and portafilter, stabilizes brewing temperature, and rinses away any old coffee residue. Let the water run for about 3–5 seconds (or until it flows smoothly), and if possible, run it into your cup to preheat the cup as well. Discard the water, then proceed to brew your espresso.",
        "image": "/static/images/preparation.jpg"
    }
    ,
    {
        "title": "Step-2: Grinding Coffee Beans",
        "content": "The first step in preparing an Americano is grinding the coffee beans. The beans should be ground to a medium-fine consistency, similar to table salt. This allows proper extraction during brewing. If the grind is too coarse, the coffee will be weak, and if it is too fine, it may become overly bitter or over-extracted.",
        "image": "/static/images/preparation.jpg"
    },
    {
        "title": "Step-3 Fill the portafilter",
        "content": "For a single shot of espresso, use about 0.2 ounces of ground beans (one rounded teaspoon). Use one rounded tablespoon (0.6 ounces) of ground beans for a double espresso.",
        "image": "/static/images/preparation.jpg"
    }
    ,
    {
        "title": "Step-4: Tamping the Coffee",
        "content": "After grinding, the coffee grounds are placed into the portafilter and evenly tamped down using a tamper. This step is important because it ensures uniform pressure during extraction. Uneven tamping can cause water to flow irregularly, leading to poor flavor balance in the espresso shot.",
        "image": "/static/images/preparation.jpg"
    },
    {
        "title": "Step-5: Brewing Espresso",
        "content": "Once the coffee is properly tamped, it is placed into the espresso machine for brewing. Hot pressurized water is forced through the compacted coffee grounds to extract rich espresso. The brewing time usually lasts around 25 to 30 seconds, producing a strong and concentrated coffee base.",
        "image": "/static/images/preparation.jpg"
    },
    
    {
        "title": "Step-6: Adding Hot Water And Serve",
        "content": "After the espresso is brewed, hot water is added to it to create the Americano. The ratio of water to espresso can vary depending on taste preference. This step dilutes the intensity of espresso while preserving its aroma and flavor. The final step is serving the Americano. At this stage, the drink has a balanced flavor that combines the strength of espresso with the smoothness of hot water. It can be enjoyed plain or customized with milk or sugar depending on personal preference.",
        "image": "/static/images/preparation.jpg"
    }
]

quiz_data = [
    {
        "question": "Which bean produces a more bitter taste?",
        "options": ["Arabica", "Robusta", "Dark roast"],
        "answer": "Robusta",
        "tip": "Tip: Bean variety can strongly affect bitterness; Robusta usually has higher caffeine.",
        "feedback": {
            "Arabica": "Arabica is usually smoother and less bitter than Robusta.",
            "Robusta": "Correct! Robusta tends to be more bitter due to higher caffeine and stronger flavor.",
            "Dark roast": "Roast level affects bitterness, but this question is about bean type."
        }
    },
    {
        "question": "Which factor affects bitterness more during extraction?",
        "options": ["Water temperature", "Brewing time", "Amount of sugar"],
        "answer": "Water temperature",
        "tip": "Tip: Extraction depends on brewing variables like temperature and time, not sweetness.",
        "feedback": {
            "Water temperature": "Correct! Temperature influences extraction rate and bitterness.",
            "Brewing time": "Brewing time matters too, but temperature is a major driver of extraction.",
            "Amount of sugar": "Sugar changes sweetness, not extraction bitterness."
        }
    },
    {
        "question": "Which gives a stronger Americano base?",
        "options": ["Single shot", "Double shot", "Adding more water"],
        "answer": "Double shot",
        "tip": "Tip: Strength is primarily determined by how much espresso you extract before diluting.",
        "feedback": {
            "Single shot": "Single shot is lighter and less strong than a double shot.",
            "Double shot": "Correct! More espresso creates a stronger base.",
            "Adding more water": "More water dilutes coffee, making it weaker."
        }
    },

    # New Q4 (from image)
    {
        "question": "Which roast gives a smoky flavor?",
        "options": ["Light roast", "Dark roast", "Medium roast"],
        "answer": "Dark roast",
        "tip": "Tip: Dark roasts are roasted longer, which brings out deeper, smokier flavors and reduces acidity.",
        "feedback": {
            "Light roast": "Light roasts tend to be brighter and more acidic, with less smoky flavor.",
            "Dark roast": "Correct! Dark roast commonly has a smoky, bold flavor due to longer roasting.",
            "Medium roast": "Medium roasts are more balanced and typically less smoky than dark roasts."
        }
    },

    # New Q5 (from image)
    {
        "question": "Which factor mainly controls how strong an Americano tastes?",
        "options": ["Amount of espresso", "Water temperature", "Amount of sugar"],
        "answer": "Amount of espresso",
        "tip": "Tip: Strength mostly depends on how much espresso is used and how much it’s diluted with water.",
        "feedback": {
            "Amount of espresso": "Correct! More espresso (e.g., double shot) generally makes a stronger Americano.",
            "Water temperature": "Temperature affects extraction and bitterness, but it’s not the main control for overall strength.",
            "Amount of sugar": "Sugar changes sweetness, not the coffee’s strength."
        }
    }
]

beans = [
    {
        "name": "Arabica",
        "content": "Arabica coffee is known for its smooth and refined flavor profile. It has a naturally mild taste with subtle sweetness and a slightly higher acidity compared to other coffee beans. Grown mostly at higher altitudes, Arabica beans are considered high quality and are often preferred by coffee enthusiasts who enjoy a less bitter and more aromatic cup with complex flavor notes.",
        "image": "/static/images/beans/arabica.png"
    },
    {
        "name": "Robusta",
        "content": "Robusta coffee is characterized by its strong, bold flavor and higher caffeine content compared to Arabica. It has a more bitter and earthy taste, which makes it popular for espresso blends where a rich crema is desired. Robusta plants are easier to grow and more resistant to disease, making these beans more affordable and widely used in instant coffee products.",
        "image": "https://imgs.search.brave.com/LNJ11fBFLmZYvWFJlUYmXiDhratRvo13TEca7-cmvOk/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9tZWRp/YS5nZXR0eWltYWdl/cy5jb20vaWQvMTI3/OTAwMTgyNy9waG90/by9jb2ZmZWUtYmVh/bnMuanBnP3M9NjEy/eDYxMiZ3PTAmaz0y/MCZjPThuQjVCQV9F/UVpFMWVFZlB1clVs/amNPdEtYcnVCOVJh/OHRHdHhPUVpwRWc9"
    },
    {
        "name": "Light Roast",
        "content": "Light roast coffee beans are roasted for a shorter period of time, which preserves more of the original flavors of the bean. This results in a brighter, more acidic cup with fruity and floral notes. Light roast coffee typically has a higher caffeine content by volume and is preferred by those who enjoy a crisp, complex, and more nuanced coffee experience.",
        "image": "https://imgs.search.brave.com/s7FATi1gtdOaTo03i7b1_nr3AXueGgP3wWkHw1A_f3c/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly93d3cu/d2FrYWNvZmZlZS5j/b20vY2RuL3Nob3Av/YXJ0aWNsZXMvd2hh/dC1pcy1saWdodC1y/b2FzdC1jb2ZmZWVf/MjA0OHgyMDQ4LnBu/Zz92PTE1NjY1MjM0/Nzk"
    },
    {
        "name": "Dark Roast",
        "content": "Dark roast coffee is roasted for a longer time at higher temperatures, giving it a deep, bold flavor with smoky and sometimes slightly bitter undertones. The roasting process reduces acidity and brings out rich, roasted characteristics. These beans are often used for strong espresso-based drinks and are favored by those who prefer a heavier body and intense coffee flavor.",
        "image": "/static/images/beans/dark-roast.jpg"
    }
]

print(len(learn_data)+len(beans))
app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def home():
    return render_template("home.html")

# Start
session={}
session['answers']=[]
session['corrected']=0
session['progress']=0
@app.route("/learn_complete")
def end_learning():
    return render_template("end_learn.html")
@app.route("/learn/<int:step>")
def learn(step):
    if step > len(learn_data)+4:
        return redirect("/learn_complete")
    elif step>=6 and step<=9:
        return render_template("bean.html",bean=beans[step-6],step=step,index=step-6, total=len(beans))
    lesson = {}
    if step>=10:
        lesson=learn_data[step-5]
    else:
        lesson=learn_data[step-1]
        
    session["progress"]=step

    return render_template("learn.html", lesson=lesson, step=step)

@app.route("/quiz/<int:q>", methods=["GET", "POST"])
def quiz(q):
    if q==1:
        session['corrected']=0
        session['answers']=[]
    if q > len(quiz_data):
        return redirect("/result")

    if request.method == "POST":
        question = quiz_data[q-1]
        correct = question["answer"]
        selected = request.form.get("answer")
        print(selected)
        is_correct=False
        if selected==correct :
            if selected not in session['answers']:
                session["corrected"]+=1
                session['answers'].append(selected)
            is_correct=True
        print(session)
        return render_template("quiz.html",is_correct=is_correct,feedback_msg=question['feedback'][selected],q=question,next_q=q+1,total=len(quiz_data))

    return render_template("quiz.html", q=quiz_data[q-1], index=q-1)


@app.route("/result")
def result():
    return render_template("result.html", score=session["corrected"], total=len(quiz_data))


if __name__ == "__main__":
    app.run(debug=True)