def init_recommendations():
    # Добавление упражнений в БД (упрощено)
    print("Упражнения добавлены")

def get_exercises_for_error(error_type):
    exercises = {
        "руки": [
            "Упражнение 1: Ловля воды",
            "Упражнение 2: Один рукав",
            "Упражнение 3: Захват"
        ]
    }
    return exercises.get(error_type, ["Общее упражнение"])
