question_data = [
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
''' ''',
]


import re
import random


def find_duplicates_and_clean(question_data):
    question_texts = {}
    unique_questions = []
    duplicates_count = 0
    total_questions_count = len(question_data)  # Total questions count

    for i, line in enumerate(question_data):
        match = re.search(r'QuestionModule\("(.+?)",', line)
        if match:
            text = match.group(1)

            if text in question_texts:
                duplicates_count += 1
            else:
                question_texts[text] = i + 1
                unique_questions.append(line)

    # Calculate unique question count
    unique_count = len(unique_questions)


    print(f"Duplicates count: {duplicates_count}")
    print(f"Unique count: {unique_count}")
    print(f"Total questions count: {total_questions_count}")  # Total questions count

    return unique_questions, duplicates_count, total_questions_count


def create_sets(question_data, set_size=25):
    random.shuffle(question_data)
    sets = []
    for i in range(0, len(question_data), set_size):
        sets.append(question_data[i:i + set_size])
    return sets


# Remove duplicates and clean the data
unique_questions, duplicates_count, total_questions_count = find_duplicates_and_clean(question_data)

# Create question sets
question_sets = create_sets(unique_questions)

setname = input("Enter your set name: ")
question_sets_map = {}
for index, question_set in enumerate(question_sets):
    if question_set:
        set_name = f"{setname}set{index + 1}"
        question_sets_map[set_name] = question_set

        # Print the ArrayList initialization inside the set
        print(f"\n{set_name} = [")  # Open the set
        print(f"//Total questions in {set_name}: {len(question_set)}")
        print(
            f"    ArrayList<QuestionModule> {set_name} = new ArrayList<>();")  # ArrayList initialization inside the list

        for question in question_set:
            print(f"    {question.replace('add(', f'{set_name}.add(')}")
        print("]")  # Close the set



# Print the questionSets.put() function for each set
for set_name in question_sets_map.keys():
    print(f"questionSets.put(\"{set_name}\", {set_name});")

# Display the total number of question sets and total questions
print(f"//Total number of question sets: {len(question_sets)}")
print(f"//Total number of questions: {total_questions_count}")

