from flask import Flask, render_template, request, redirect
learn_data = [
    {
        "title": "What is Americano?",
        "content": "An Americano is a coffee drink made by adding hot water to a shot of espresso. This process creates a coffee that has a similar strength to regular brewed coffee but retains the rich flavor of espresso. It is popular because it balances intensity and smoothness, making it enjoyable for many coffee drinkers.",
        "image": "/static/images/image.jpg"
    },
    {
        "title": "Types of Americano",
        "content": "There are different types of Americano depending on how it is prepared. A single shot Americano is lighter and less intense, while a double shot creates a stronger and richer flavor. Additionally, the roast level of the beans, such as light or dark roast, also affects the overall taste and aroma of the drink.",
        "image": "/static/images/image.jpg"
    },
    {
        "title": "Bitter Taste",
        "content": "Bitterness in coffee is a common taste characteristic that comes from compounds released during brewing. When coffee is over-extracted, it becomes more bitter and less pleasant. This bitterness can feel strong and sharp on the tongue, and understanding it helps you control the brewing process to achieve a balanced flavor.",
        "image": "/static/images/image.jpg"
    },
    {
        "title": "Ingredients",
        "content": "To make an Americano, you need a few simple ingredients and tools. The main components are freshly ground coffee beans and hot water. An espresso machine is used to extract the coffee properly. The quality of the beans and the freshness of the grind play a major role in the final taste of the drink.",
        "image": "/static/images/image.jpg"
    },
    {
        "title": "Coffee Beans",
        "content": "Coffee beans are one of the most important factors that influence the taste of an Americano. Different types of beans produce different flavor profiles, ranging from smooth and mild to strong and bitter. By exploring different beans, you can understand how each type affects the final taste of your coffee.",
        "action": "/beans"
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
        "title": "Preparation",
        "content": "Preparing an Americano involves several important steps. First, the coffee beans are ground to the correct consistency. Then, the coffee is tamped evenly in the portafilter before brewing the espresso. Finally, hot water is added to the espresso to create the Americano. Each step must be done carefully to achieve the best flavor.",
        "image": "/static/images/preparation.jpg"
    }
    ,
    {
        "title": "Step-1: Grinding Coffee Beans",
        "content": "The first step in preparing an Americano is grinding the coffee beans. The beans should be ground to a medium-fine consistency, similar to table salt. This allows proper extraction during brewing. If the grind is too coarse, the coffee will be weak, and if it is too fine, it may become overly bitter or over-extracted.",
        "image": "/static/images/preparation.jpg"
    },
    {
        "title": "Step-2: Tamping the Coffee",
        "content": "After grinding, the coffee grounds are placed into the portafilter and evenly tamped down using a tamper. This step is important because it ensures uniform pressure during extraction. Uneven tamping can cause water to flow irregularly, leading to poor flavor balance in the espresso shot.",
        "image": "/static/images/preparation.jpg"
    },
    {
        "title": "Step-3: Brewing Espresso",
        "content": "Once the coffee is properly tamped, it is placed into the espresso machine for brewing. Hot pressurized water is forced through the compacted coffee grounds to extract rich espresso. The brewing time usually lasts around 25 to 30 seconds, producing a strong and concentrated coffee base.",
        "image": "/static/images/preparation.jpg"
    },
    {
        "title": "Step-4: Adding Hot Water",
        "content": "After the espresso is brewed, hot water is added to it to create the Americano. The ratio of water to espresso can vary depending on taste preference. This step dilutes the intensity of espresso while preserving its aroma and flavor, resulting in a smoother coffee drink.",
        "image": "/static/images/preparation.jpg"
    },
    {
        "title": "Step-5: Final Americano",
        "content": "The final step is serving the Americano. At this stage, the drink has a balanced flavor that combines the strength of espresso with the smoothness of hot water. It can be enjoyed plain or customized with milk or sugar depending on personal preference.",
        "image": "/static/images/preparation.jpg"
    }
]

quiz_data = [
    {
        "question": "Which bean produces a more bitter taste?",
        "options": ["Arabica", "Robusta", "Dark roast"],
        "answer": "Robusta",
        "feedback": {
            "Arabica": "Arabica is smoother and less bitter.",
            "Robusta": "Correct! Robusta is more bitter due to high caffeine.",
            "Dark roast": "Roast affects taste, but bean type matters more here."
        }
    },
    {
        "question": "Which factor affects bitterness more?",
        "options": ["Water temperature", "Brewing time", "Amount of sugar"],
        "answer": "Water temperature",
        "feedback": {
            "Water temperature": "Correct! Temperature controls extraction.",
            "Brewing time": "Partially correct but less impactful.",
            "Amount of sugar": "Sugar affects sweetness, not bitterness."
        }
    },
    {
        "question": "Which gives stronger coffee?",
        "options": ["Single shot", "Double shot", "Adding more water"],
        "answer": "Double shot",
        "feedback": {
            "Single shot": "Single shot is lighter and less strong.",
            "Double shot": "Correct! More espresso = stronger coffee.",
            "Adding more water": "Water dilutes coffee, making it weaker."
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


app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def home():
    return render_template("home.html")

# Start
session={}
session['answers']=[]
session['progress']=[]
@app.route("/start")
def start():
    return redirect("/learn/0")

# Learning
@app.route("/learn/<int:step>")
def learn(step):
    if step >= len(learn_data):
        return redirect("/quiz/0")

    lesson = learn_data[step]
    session["progress"].append(step)

    return render_template("learn.html", lesson=lesson, step=step)

# Beans entry point
@app.route("/beans")
def beans_intro():
    return redirect("/beans/0")



@app.route("/beans/<int:i>")
def bean_page(i):
    if i >= len(beans):
        return redirect("/learn/5")  # continue learning

    bean = beans[i]
    return render_template("bean.html", bean=bean, index=i, total=len(beans))



@app.route("/select_bean/<int:i>")
def select_bean(i):
    session["selected_bean"] = beans[i]["name"]
    return redirect("/learn/5")  # continue learning


@app.route("/quiz/<int:q>", methods=["GET", "POST"])
def quiz(q):
    if q >= len(quiz_data):
        return redirect("/result")

    if request.method == "POST":
        selected = request.form.get("answer")
        print(selected)
        session['answers'].append(selected)
        print(session)
        return redirect(f"/feedback/{q}/{selected}")

    return render_template("quiz.html", q=quiz_data[q], index=q)

# Feedback
@app.route("/feedback/<int:q>/<option>")
def feedback(q, option):
    question = quiz_data[q]
    # print(question)
    correct = question["answer"]
    # print(correct)
    feedback_text = question["feedback"][option]
    
    return render_template(
        "feedback.html",
        option=option,
        correct=correct,
        feedback=feedback_text,
        next_q=q + 1
    )

# Result
@app.route("/result")
def result():
    score = 0
    for i, ans in enumerate(session["answers"]):
        if ans == quiz_data[i]["answer"]:
            print(ans)
            score += 1
    print(score)
    return render_template("result.html", score=score, total=len(quiz_data))


if __name__ == "__main__":
    app.run(debug=True)