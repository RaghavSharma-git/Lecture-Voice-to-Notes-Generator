import random

def generate_mcqs(text, num_questions=3):
    sentences = text.split(".")
    questions = []

    for sentence in sentences:
        sentence = sentence.strip()
        words = sentence.split()

        if len(words) > 6:   # lowered condition
            keyword = words[0]   # pick first word instead of random

            question_text = sentence.replace(keyword, "______", 1)

            options = [keyword]

            while len(options) < 4:
                fake_word = random.choice(words)
                if fake_word not in options:
                    options.append(fake_word)

            random.shuffle(options)

            questions.append({
                "question": question_text,
                "options": options,
                "answer": keyword
            })

        if len(questions) >= num_questions:
            break

    return questions