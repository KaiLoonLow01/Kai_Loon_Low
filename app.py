from flask import Flask, render_template, request, redirect
learn_data = [
    {
        "title": "What is Americano?",
        "content": "An Americano is made by adding hot water to espresso, creating a drink similar in strength to brewed coffee while keeping espresso’s rich flavor. It offers a smooth balance of intensity and is widely enjoyed.",
        "image": "/static/images/home.jpg"
    },
    {
        "title": "Types of Americano",
        "content": "Americanos vary by preparation. A single shot is lighter, while a double shot is stronger and richer. Bean roast levels, such as light or dark, also influence the flavor and aroma.",
        "image": "/static/images/type1.jpg"
        
    },
    {
        "title": "Bitter Taste",
        "content": "Bitterness in coffee comes from compounds released during brewing. Over-extraction increases bitterness, making the taste sharp and unpleasant. Understanding this helps achieve a balanced flavor.",
        "image": "/static/images/bitter-taste.jpg"
    },
    {
        "title": "Ingredients & Tools",
        "content": "To make an Americano, you need coffee beans, hot water, and an espresso machine. Fresh beans and proper grinding are key to achieving the best flavor.",
        "image": "/static/images/ingredients.jpg"
    },
    {
        "title": "Coffee Beans",
        "content": "Coffee beans greatly affect flavor, ranging from mild to strong and bitter. Trying different beans helps you understand how each type shapes the final taste.",
         "image": "/static/images/coffee-beans.jpg"
    },
    {
        "title": "Best Beans",
        "content": "Arabica beans are ideal for Americanos due to their smooth, balanced, and slightly acidic flavor. They are less bitter than Robusta and generally preferred by most coffee drinkers.",
        "image": "/static/images/beans/arabica.png"
    },
    {
        "title": "Temperature",
        "content": "Temperature is crucial in brewing. The ideal range is 90–96°C. Too hot causes bitterness, while too cold leads to weak and underdeveloped coffee.",
        "image": "/static/images/temparature.jpg"
    },
    {
        "title": "Step-1 Pull a ‘blank shot’",
        "content": "Run hot water through the machine without coffee to warm it up and remove residue. Let it flow for a few seconds, then discard the water before brewing.",
        "image": "/static/images/blank.jpg"
    }
    ,
    {
        "title": "Step-2: Grinding Coffee Beans",
        "content": "Grind beans to a medium-fine texture like table salt. Too coarse makes weak coffee, while too fine causes over-extraction and bitterness.",
        "image": "/static/images/grind.jpg"
    },
    {
        "title": "Step-3 Fill the portafilter",
        "content": "Use about 0.2 oz (1 teaspoon) for a single shot and 0.6 oz (1 tablespoon) for a double shot.",
        "image": "/static/images/fill.jpg"
    }
    ,
    {
        "title": "Step-4: Tamping the Coffee",
        "content": "Press the coffee evenly in the portafilter using a tamper. Proper tamping ensures even extraction and balanced flavor.",
        "video": "/static/videos/temp.mp4"
    },
    {
        "title": "Step-5: Brewing Espresso",
        "content": "Place the portafilter in the machine and brew for 25–30 seconds. Pressurized water extracts a strong and rich espresso.",
        "video": "/static/videos/brew.mp4"
    },
    
    {
        "title": "Step-6: Adding Hot Water And Serve",
        "content": "Add hot water to the espresso to create an Americano. Adjust the ratio to taste, then serve. Enjoy it plain or with milk or sugar.",
        "image": "/static/images/americano.jpg"
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
        "image": "/static/images/beans/robusta.jpg"
    },
    {
        "name": "Light Roast",
        "content": "Light roast coffee beans are roasted for a shorter period of time, which preserves more of the original flavors of the bean. This results in a brighter, more acidic cup with fruity and floral notes. Light roast coffee typically has a higher caffeine content by volume and is preferred by those who enjoy a crisp, complex, and more nuanced coffee experience.",
        "image": "/static/images/beans/light-roast.jpg"
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
        return render_template(
            "quiz.html",
            is_correct=is_correct,
            feedback_msg=question['feedback'][selected],
            q=question,
            next_q=q+1,
            total=len(quiz_data),
            selected=selected,
            index=q-1
        )

    return render_template("quiz.html", q=quiz_data[q-1], index=q-1, total=len(quiz_data))


@app.route("/result")
def result():
    return render_template("result.html", score=session["corrected"], total=len(quiz_data))


if __name__ == "__main__":
    app.run(debug=True)