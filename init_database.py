from database.crud import init_db
from analysis.recommendation_engine import init_recommendations

if __name__ == '__main__':
    print("Инициализация БД...")
    init_db()
    print("Добавление упражнений...")
    init_recommendations()
    print("✅ База данных готова!")
