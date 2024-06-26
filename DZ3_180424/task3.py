#В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10
# самых частых. Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
import re
from collections import Counter

def count_words(text):
    # Приводим текст к нижнему регистру и удаляем знаки препинания
    text = re.sub(r'[^\w\s]', '', text.lower())
    words = text.split()
    
    # Считаем количество встречаемых слов
    word_counts = Counter(words)
    
    # Возвращаем 10 самых часто встречающихся слов
    most_common_words = word_counts.most_common(10)
    
    return most_common_words

# Пример текста для анализа (можно заменить на любой другой текст)
text = """
Сама́ра (с 27 января 1935 года по 25 января 1991 года — Куйбышев) — город в 
Среднем Поволжье России, центр Поволжского экономического района и 
Самарской области, образует городской округ Самара[5]. Город трудовой и 
боевой славы[6] (2016). Город трудовой доблести[7] (2020).
Население — 1 163 645[2] чел. (2023), девятый по численности населения 
город России. В пределах агломерации (третьей по численности населения в
России) проживает свыше 2,7 млн человек.
Город расположен на левом берегу Саратовского водохранилища напротив
Самарской Луки, при впадении в неё рек Самары (отсюда название города) и Сока. 
Впервые название реки Самары упоминается в записках секретаря арабского 
посольства и путешественника Ахмеда ибн Фадлана (921 год) как «Самур».
Крупный экономический, транспортный, научно-образовательный и культурный 
центр[8]. Самара также представляет собой крупный центр машиностроения и 
металлообработки, металлургии, нефтеперерабатывающей, пищевой, а также 
космической и авиационной промышленности. В городе располагается более 
150 крупных и средних промышленных предприятий[9].
В Самаре одна из самых длинных в России речных набережных и самое высокое 
здание железнодорожного вокзала в Европе[10][11]. Кроме того, 
площадь им. Куйбышева является первой по размеру площадью в Европе[12].
В Самаре проходит самый продолжительный фестиваль в мире. I Международный 
патриотический фестиваль «Борис Коценко представляет» проводился 238 дней — 
с 30 октября 2005 года по 24 июня 2006 года 2018 году в городе были проведены 
матчи чемпионата мира по футболу.
Указом Президента Российской Федерации от 2 июля 2020 городу было присвоено 
звание «Город трудовой доблести»[13].
"""
most_common_words = count_words(text)
print("10 самых часто встречающихся слов:")
for word, count in most_common_words:
    print(f"{word}: {count}")
