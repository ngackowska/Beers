from clips import Environment

env = Environment()
env.load("beers.clp")
env.run()


def start():
    fact = env.assert_string('(beer (question "Are you in Scotland?"))')
    print("ODPALAM CZWARTY REAKTOR")

def add_fact():
    

def get_question():
    for fact in env.facts():
        #print(fact.template.name)
        if fact.template.name == "beer":
            return fact["question"]
