import pandas as pd
import numpy as np
import os

file_name = 'train.csv'
if not os.path.exists(file_name):
    print(f"ОШИБКА: Файл {file_name} не найден.")
    exit()

print("="*50)
print("ЧАСТЬ II. ЗАГРУЗКА И ПЕРВИЧНЫЙ АНАЛИЗ ДАННЫХ")
print("="*50)

df = pd.read_csv(file_name)

try:
    n = int(input("Введите количество первых строк для вывода (n): "))
except ValueError:
    n = 5
    print("Введено неверное значение. По умолчанию n=5")

print(f"\n7. Первые {n} строк:")
print(df.head(n))

print("\n8. Последние 5 строк:")
print(df.tail())

print(f"\n9. Размер таблицы (строки, столбцы): {df.shape}")

print("\n10. Названия столбцов:")
print(df.columns.tolist())

print("\n11. Типы данных столбцов:")
print(df.dtypes)

print("\n12. Числовые признаки: Age, Fare, SibSp, Parch")
print("    Категориальные признаки: Pclass, Sex, Embarked, Survived, Cabin")

print("\n13. Статистика числовых признаков:")
print(df[['Age', 'Fare', 'SibSp', 'Parch']].describe().loc[['mean', '50%', 'min', 'max', 'std']])

print("\n14. Количество пассажиров каждого класса (Pclass):")
print(df['Pclass'].value_counts())

print("\n15. Количество уникальных значений в Embarked:")
print(df['Embarked'].nunique())


print("\n" + "="*50)
print("ЧАСТЬ III. ОБРАБОТКА ПРОПУЩЕННЫХ ЗНАЧЕНИЙ")
print("="*50)

print("\n16. Количество пропусков в каждом столбце:")
print(df.isnull().sum())

print("\n17. Процент пропусков:")
print((df.isnull().sum() / len(df) * 100).round(2))

print("\n18. Столбец с максимальным количеством пропусков:")
print(df.isnull().sum().idxmax())

age_before = df['Age'].describe().loc[['mean', '50%', 'min', 'max', 'std', 'count']]
age_before.index = ['Среднее', 'Медиана', 'Минимум', 'Максимум', 'Ст. отклонение', 'Кол-во известных']

median_age = df['Age'].median()
df['Age'] = df['Age'].fillna(median_age)

age_after = df['Age'].describe().loc[['mean', '50%', 'min', 'max', 'std', 'count']]
age_after.index = ['Среднее', 'Медиана', 'Минимум', 'Максимум', 'Ст. отклонение', 'Кол-во известных']

print("\n22. Сравнение статистики Age до и после обработки:")
comparison = pd.DataFrame({'До обработки': age_before, 'После обработки': age_after})
print(comparison.round(2))

df.dropna(subset=['Embarked'], inplace=True)

cabin_missing = df['Cabin'].isnull().mean() * 100
if cabin_missing > 50:
    df.drop(columns=['Cabin'], inplace=True)
    print(f"\n24. Столбец Cabin удален (доля пропусков {cabin_missing:.2f}%)")

print("\n25. Оставшиеся пропуски:")
print(df.isnull().sum())

print(f"\n26. Размер таблицы до обработки: (891, 12)")
print(f"    Размер таблицы после обработки: {df.shape}")


print("\n" + "="*50)
print("ЧАСТЬ IV. АНАЛИЗ ДАННЫХ С ПОМОЩЬЮ NUMPY")
print("="*50)

survived = df['Survived'].to_numpy()
sex = df['Sex'].to_numpy()
age = df['Age'].to_numpy()
fare = df['Fare'].to_numpy()

print(f"\n31. Общий процент выживших: {np.mean(survived) * 100:.2f}%")

male_survived = np.mean(survived[sex == 'male']) * 100
female_survived = np.mean(survived[sex == 'female']) * 100
print(f"32. Процент выживших мужчин: {male_survived:.2f}%")
print(f"    Процент выживших женщин: {female_survived:.2f}%")

print(f"\n33. Средний возраст мужчин: {np.mean(age[sex == 'male']):.2f}")
print(f"    Средний возраст женщин: {np.mean(age[sex == 'female']):.2f}")

surv_male_age = np.mean(age[(sex == 'male') & (survived == 1)])
died_male_age = np.mean(age[(sex == 'male') & (survived == 0)])
surv_female_age = np.mean(age[(sex == 'female') & (survived == 1)])
died_female_age = np.mean(age[(sex == 'female') & (survived == 0)])

print("\n34. Средний возраст по полу и выживаемости:")
print(f"    Выжившие мужчины: {surv_male_age:.2f} | Погибшие мужчины: {died_male_age:.2f}")
print(f"    Выжившие женщины: {surv_female_age:.2f} | Погибшие женщины: {died_female_age:.2f}")

print(f"\n35. Стоимость билета (Min, Max, Mean): {np.min(fare):.2f}, {np.max(fare):.2f}, {np.mean(fare):.2f}")
print(f"36. Стандартное отклонение возраста: {np.std(age):.2f}")


print("\n" + "="*50)
print("ЧАСТЬ V. ФИЛЬТРАЦИЯ ДАННЫХ")
print("="*50)

task1 = df[(df['Sex'] == 'male') & (df['Age'] > 30) & (df['Pclass'] == 1)]
print(f"\nЗадание 1. Мужчины старше 30 лет в 1 классе. Найдено: {len(task1)}")
print(task1.head(10))

task2 = df[(df['Age'] < 18) | ((df['Sex'] == 'female') & (df['Survived'] == 1))]
print(f"\nЗадание 2. Моложе 18 ИЛИ (Женщины И выжили). Найдено: {len(task2)}")

mean_fare_class3 = df[df['Pclass'] == 3]['Fare'].mean()
task3 = df[(df['Pclass'] == 3) & (df['Fare'] > mean_fare_class3)]
print(f"\nЗадание 3. 3 класс, стоимость билета выше средней по классу ({mean_fare_class3:.2f}). Найдено: {len(task3)}")

task4 = df[(df['Age'] >= 20) & (df['Age'] <= 40) & (df['Embarked'] == 'S')]
print(f"\nЗадание 4. Возраст 20-40, порт S. Найдено: {len(task4)}")


print("\n" + "="*50)
print("ЧАСТЬ VI. ГРУППИРОВКА И АГРЕГИРОВАНИЕ")
print("="*50)

print("\n37. Группировка по классу и полу:")
group1 = df.groupby(['Pclass', 'Sex']).agg(
    Количество=('PassengerId', 'count'),
    Средний_возраст=('Age', 'mean'),
    Доля_выживших=('Survived', lambda x: x.mean() * 100),
    Средняя_стоимость=('Fare', 'mean')
).round(2)
print(group1)

print("\n38. Группировка по порту посадки (Embarked):")
group2 = df.groupby('Embarked').agg(
    Количество=('PassengerId', 'count'),
    Доля_выживших=('Survived', lambda x: x.mean() * 100)
).round(2)
print(group2)

print("\n39. Класс с наибольшей долей выживших:")
survival_by_class = df.groupby('Pclass')['Survived'].mean() * 100
best_class = survival_by_class.idxmax()
print(f"Класс {best_class} ({survival_by_class.max():.2f}%)")


print("\n" + "="*50)
print("ЧАСТЬ VII. СОХРАНЕНИЕ РЕЗУЛЬТАТОВ")
print("="*50)

df.to_csv('titanic_processed.csv', index=False)
group1.to_csv('titanic_statistics.csv')
print("\n40-41. Данные сохранены в titanic_processed.csv и titanic_statistics.csv")

print("\n42. Проверка повторной загрузки titanic_processed.csv:")
df_loaded = pd.read_csv('titanic_processed.csv')
print(f"Размер загруженного файла: {df_loaded.shape} (Совпадает с {df.shape})")
