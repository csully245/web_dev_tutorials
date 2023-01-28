import jinja2

max_score = 100
test_name = "Python Challenge"
students = [
    {"name": "Sandrine", "score": 100},
    {"name": "Gergeley", "score": 87},
    {"name": "Frieda", "score": 92},
    {"name": "Fritz", "score": 40},
    {"name": "Sirius", "score": 75},
]

environment = jinja2.Environment(loader=jinja2.FileSystemLoader("templates/"))
template = environment.get_template("message.txt")

for student in students:
    filename = f"generated/message_{student['name'].lower()}.txt"
    content = template.render(student, max_score=max_score, test_name=test_name)
    with open(filename, mode="w", encoding="utf-8") as message:
        message.write(content)
        print(f"... wrote {filename}")

results_filename = "generated/students_results.html"
results_template = environment.get_template("results.html")
context = {"students": students, "text_name": test_name, "max_score": max_score}
with open(file=results_filename, mode="w", encoding="utf-8") as results:
    results.write(results_template.render(context))
    print(f"... wrote {results_filename}")
