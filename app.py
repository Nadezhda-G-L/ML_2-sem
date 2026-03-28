import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import os

st.title("Определение тональности текста")

# 1. Загрузка и обучение модели

# Данные
data = {
    'text': [
        'Я очень доволен покупкой!', 'Это ужасный фильм', 'Прекрасный сервис', 
        'Не рекомендую', 'Великолепно!', 'Плохое качество', 'Лучшая вещь на свете'
    ],
    'label': [1, 0, 1, 0, 1, 0, 1]
}
df = pd.DataFrame(data)

X = df['text']
y = df['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_tfidf, y_train)
y_pred = model.predict(X_test_tfidf)

# 2. Вывод метрик
# st.subheader("Метрики модели")
# st.write(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
# st.text(classification_report(y_test, y_pred))

# 3. Визуализация матрицы ошибок
cm = confusion_matrix(y_test, y_pred, labels=model.classes_)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Negative', 'Positive'])
fig, ax = plt.subplots()
disp.plot(ax=ax)
# st.pyplot(fig)

# 4. Обработка пользовательского ввода
st.subheader("Проверка тональности текста")
user_text = st.text_area("Введите текст")

if user_text:
    text_tfidf = vectorizer.transform([user_text])
    prediction = model.predict(text_tfidf)[0]
    sentiment = "Позитивный" if prediction == 1 else "Негативный"
    st.success(f"Тональность текста: **{sentiment}**")

# 5. Сохранение графика
os.makedirs("output", exist_ok=True)
plt.savefig("output/plot.png")
