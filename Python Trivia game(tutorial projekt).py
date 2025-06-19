#list of questions
#store the answers
#randomly pick questions
#ask the questions
#see if they are correct
#keep track of the score
# tell the use their score

import random

questions = {       #ist ein dictionary, welches ein key value store ist, erlaubt dir some kind of key zu haben, question z.b, und die value ist die antwort der frage
    " In welchem Film sagt Tom Hanks die berühmte Zeile: „Life is like a box of chocolates“?": "Forrest Gump",
    "Wer spielte den Joker im Oscar-prämierten Film The Dark Knight?": "Heath Ledger",
    " Welcher Film gewann 2020 den Oscar als „Bester Film“ und ist der erste nicht-englischsprachige Film, der diesen Preis bekam?": "Parasite",
    " In welchem Science-Fiction-Film geht es um Träume in Träumen, die mit Hilfe eines „Totems“ überprüft werden?": "Inception",
    " Wie heißt der berühmte Song aus dem Film Titanic, der von Céline Dion gesungen wurde?": "My Heart Will Go On",
    "Wer führte Regie bei Schindlers Liste?": "Steven Spielberg",
    " In welchem Film kämpft Russell Crowe als General Maximus um seine Freiheit?": "Gladiator",
    " Welcher Animationsfilm von Pixar beginnt mit der traurigen Liebesgeschichte von Carl und Ellie?": "Oben",
    " In welchem Film sagt Meryl Streep als Miranda Priestly den berühmten Satz über „Cerulean Blue“?": "Der Teufel trägt Prada",
    " Wie heißt die Figur von Leonardo DiCaprio im Film The Revenant, für den er seinen ersten Oscar bekam?": "Hugh Glass",
    "Wie heißt der berühmte Mafia-Film aus den 70ern, der mehrere Oscars gewann und auf einem Buch von Mario Puzo basiert?": "Der Pate",
    "Welcher Film gewann 2017 den Oscar für den besten Film, nachdem La La Land fälschlicherweise zuerst genannt wurde?": "Moonlight",
    "In welchem Film tanzt John Travolta mit Uma Thurman in einem Restaurant?": "Pulp Fiction",
    "Wie heißt der Regisseur von The Shape of Water, der 2018 den Oscar für den besten Film gewann?": "Guillermo del Toro",
    "In welchem Musicalfilm spielt Hugh Jackman die Hauptrolle als P.T. Barnum?": "The Greatest Showman",
    "Wie heißt der Planet, auf dem die Avatar-Filme spielen?": "Pandora",
    "In welchem Film sagt Liam Neeson: „Ich habe eine ganz besondere Art von Fähigkeiten…“?":"96 Hours (Taken)",
    "Welcher Film von Bong Joon-ho gewann mehrere Oscars, darunter „Bester Film“?": "Parasite",
    "In welchem Film spielt Julia Roberts eine alleinerziehende Mutter, die gegen einen großen Energiekonzern kämpft?": "Erin Brockovich",
    "Wie heißt der Hobbit, der den Einen Ring tragen muss?": "Frodo Beutlin",
    "In welchem Film spielt Joaquin Phoenix einen einsamen Mann, der sich in ein Betriebssystem verliebt?": "Her",
    "Wie heißt die junge Hexe in dem Studio Ghibli Film von Hayao Miyazaki, die mit einem sprechenden Kater reist?": "Kikis kleiner Lieferservice",
    "In welchem Kriegsfilm von Christopher Nolan wird die Evakuierung von Soldaten am Strand gezeigt?": "Dunkirk",
    "Welcher Schauspieler spielte James Bond im Film Skyfall?": "Daniel Craig"
    
}

def python_trivia_game():       #reusable block of code ist eine funktion, da kommt der meiste code vom Spiel
    questions_list = list(questions.keys())   #um alles keys zu bekommen macht man .keys um alle values zu bekommen macht man .values
    total_questions = 6
    score = 0
    
    selected_questions = random.sample(questions_list, total_questions)     # es wählt k unique random elemente von einem population sequence, also ich bekomme 6 questions random von der liste
    # for loop is something that repeats a certain number of times, INDEX ist die position eines elements
    for idx, question in enumerate(selected_questions):   #es looped durch alle fragen und gibt mir die position des index von jeder frage und den value der frage, enumerate gibt uns index und value
        print(f"{idx + 1}. {question}") #position plus 1 also zuerst erste frage, dann 2 frage und etc
        user_answer = input("Deine Antwort: ").strip() #strip ist um leerzeichen weg zu machen wenn man als antwort ..8 anstat 8 eingibt
        correct_answer = questions[question]
        
        if user_answer == correct_answer:  # == vergleicht obt etwas gleich ist
            print("Richtig!😊\n")  #\n wird un in der nächsten linie in terminal runter moven, also es geht nach unten 
            score += 1
        else:
            print(f"Falsch!😢. Die Richtige Antwort ist: {correct_answer}. \n")
            
        
        if score > 3:
            print(f"Game over! Dein final score ist: {score}/{total_questions}. Gut gemacht👍")
        elif score == 3:
            print(f"Game over! Dein final score ist: {score}/{total_questions}. Geht so🤷")
        else:
            print(f"Game over! Dein final score ist: {score}/{total_questions}. Bissle schlecht👎")

python_trivia_game()
    