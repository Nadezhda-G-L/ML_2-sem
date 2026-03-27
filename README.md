# Определение тональности текста с помощью Naive Bayes

## Описание
ML-проект, демонстрирующий использование Naive Bayes для классификации текста на положительный и отрицательный.

## Функции
- Обучение модели
- Визуализация результатов
- Интерактивный интерфейс на Streamlit
- Сохранение графика в `output/plot.png`
- Ввод пользовательского текста для анализа

## Зависимости
- scikit-learn
- pandas
- matplotlib
- streamlit

## Как запустить
1. Склонировать репозиторий:
git clone https://github.com/Nadezhda-G-L/ML_2-sem
2. Перейдите в папку:
cd sentiment-analysis
3. Собрать Docker-образ:
docker build -t sentiment-analysis
4. Запустить контейнер:
docker run -p 8501:8501 sentiment-analysis
5. Открыть в браузере:
http://localhost:8501
