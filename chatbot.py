import random
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from deep_translator import GoogleTranslator
import text2emotion as te
import string
import cv2 as cv
import os
import py_avataaars as pa

style = ['CIRCLE', 'TRANSPARENT']

skin_color = ['TANNED', 'YELLOW', 'PALE', 'LIGHT', 'BROWN', 'DARK_BROWN', 'BLACK']

hair_color = ['AUBURN', 'BLACK', 'BLONDE', 'BLONDE_GOLDEN', 'BROWN', 'BROWN_DARK', 'PASTEL_PINK', 'PLATINUM', 'RED', 'SILVER_GRAY']

hat_color = ['BLACK', 'BLUE_01', 'BLUE_02', 'BLUE_03', 'GRAY_01', 'GRAY_02', 'HEATHER', 'PASTEL_BLUE', 'PASTEL_GREEN', 'PASTEL_ORANGE',
             'PASTEL_RED', 'PASTEL_YELLOW', 'PINK', 'RED', 'WHITE']

facial_hair_type = ['DEFAULT', 'BEARD_MEDIUM', 'BEARD_LIGHT', 'BEARD_MAJESTIC', 'MOUSTACHE_FANCY', 'MOUSTACHE_MAGNUM']

top_type = ['NO_HAIR', 'EYE_PATCH', 'HAT', 'HIJAB', 'TURBAN', 'WINTER_HAT1', 'WINTER_HAT2', 'WINTER_HAT3',
            'WINTER_HAT4', 'LONG_HAIR_BIG_HAIR', 'LONG_HAIR_BOB', 'LONG_HAIR_BUN', 'LONG_HAIR_CURLY', 'LONG_HAIR_CURVY',
            'LONG_HAIR_DREADS', 'LONG_HAIR_FRIDA', 'LONG_HAIR_FRO', 'LONG_HAIR_FRO_BAND', 'LONG_HAIR_NOT_TOO_LONG',
            'LONG_HAIR_SHAVED_SIDES', 'LONG_HAIR_MIA_WALLACE', 'LONG_HAIR_STRAIGHT', 'LONG_HAIR_STRAIGHT2',
            'LONG_HAIR_STRAIGHT_STRAND', 'SHORT_HAIR_DREADS_01', 'SHORT_HAIR_DREADS_02', 'SHORT_HAIR_FRIZZLE',
            'SHORT_HAIR_SHAGGY_MULLET', 'SHORT_HAIR_SHORT_CURLY', 'SHORT_HAIR_SHORT_FLAT', 'SHORT_HAIR_SHORT_ROUND',
            'SHORT_HAIR_SHORT_WAVED', 'SHORT_HAIR_SIDES', 'SHORT_HAIR_THE_CAESAR', 'SHORT_HAIR_THE_CAESAR_SIDE_PART']

mouth_type = ['DEFAULT', 'CONCERNED', 'DISBELIEF', 'EATING', 'GRIMACE', 'SAD', 'SCREAM_OPEN', 'SERIOUS', 'SMILE', 'TONGUE', 'TWINKLE', 'VOMIT']

eye_type = ['DEFAULT', 'CLOSE', 'CRY', 'DIZZY', 'EYE_ROLL', 'HAPPY', 'HEARTS', 'SIDE', 'SQUINT', 'SURPRISED', 'WINK', 'WINK_WACKY']

eyebrow_type = ['DEFAULT', 'DEFAULT_NATURAL', 'ANGRY', 'ANGRY_NATURAL', 'FLAT_NATURAL', 'RAISED_EXCITED',
                'RAISED_EXCITED_NATURAL', 'SAD_CONCERNED', 'SAD_CONCERNED_NATURAL', 'UNI_BROW_NATURAL', 'UP_DOWN',
                'UP_DOWN_NATURAL', 'FROWN_NATURAL']

accessories_type = ['DEFAULT', 'KURT', 'PRESCRIPTION_01', 'PRESCRIPTION_02', 'ROUND', 'SUNGLASSES', 'WAYFARERS']

clothe_type = ['BLAZER_SHIRT', 'BLAZER_SWEATER', 'COLLAR_SWEATER', 'GRAPHIC_SHIRT', 'HOODIE', 'OVERALL', 'SHIRT_CREW_NECK',
               'SHIRT_SCOOP_NECK', 'SHIRT_V_NECK']

clothe_color = ['BLACK', 'BLUE_01', 'BLUE_02', 'BLUE_03', 'GRAY_01', 'GRAY_02', 'HEATHER', 'PASTEL_BLUE', 'PASTEL_GREEN',
                'PASTEL_ORANGE', 'PASTEL_RED', 'PASTEL_YELLOW', 'PINK', 'RED', 'WHITE']

clothe_graphic_type = ['BAT', 'CUMBIA', 'DEER', 'DIAMOND', 'HOLA', 'PIZZA', 'RESIST', 'SELENA', 'BEAR', 'SKULL_OUTLINE', 'SKULL']

facial_hair_color = ['AUBURN', 'BLACK', 'BLONDE', 'BLONDE_GOLDEN', 'BROWN', 'BROWN_DARK', 'PLATINUM', 'RED']

powitania = [
    "Cześć! Jak mogę ci pomóc dzisiaj?",
    "Witaj! W czym mogę ci pomóc?",
    "Hej! Czego szukasz dzisiaj?",
    "Dzień dobry! Jak mogę ci służyć?",
    "Miło cię widzieć! W czym mogę pomóc?",
    "Witamy w sklepie! W czym mogę pomóc?",
    "Hej! W czym mogę być pomocny?",
    "Cześć! Jak mogę służyć?",
    "Witaj! Czego potrzebujesz?",
    "Dzień dobry! Jak mogę ci pomóc w zakupach?",
    "Miło cię widzieć! W czym mogę pomóc?",
    "Witamy w naszym sklepie! W czym mogę pomóc?",
    "Hej! Czego szukasz dzisiaj?",
    "Cześć! W czym mogę być pomocny?",
    "Witaj! Jak mogę ci pomóc dzisiaj?",
    "Dzień dobry! Czego potrzebujesz?",
    "Miło cię widzieć! W czym mogę pomóc?",
    "Witamy w sklepie z RTV i AGD! W czym mogę pomóc?",
    "Hej! Jak mogę ci służyć?",
    "Cześć! Czego szukasz dzisiaj?"
]

pozegnania = [
    "Dziękuję za skorzystanie z mojej pomocy! Do zobaczenia!",
    "Mam nadzieję, że udało mi się pomóc. Jeśli masz jeszcze jakieś pytania, jestem do dyspozycji!",
    "W razie potrzeby jestem tutaj. Do zobaczenia następnym razem!",
    "Życzę udanych zakupów! Do widzenia!",
    "Dziękuję za skorzystanie z naszego chatbota. Jeśli masz jeszcze jakieś pytania, nie wahaj się z nimi zgłosić!",
    "Do zobaczenia! Miłego dnia!",
    "Dziękuję za odwiedzenie naszego sklepu. Do widzenia!",
    "Życzę udanych zakupów i zapraszam ponownie!",
    "Miłego dnia! Do zobaczenia!",
    "Dziękuję za skorzystanie z mojej pomocy. Do zobaczenia!",
    "Do widzenia i życzę udanych zakupów!",
    "Mam nadzieję, że byłem pomocny. Miłego dnia!",
    "Dziękuję za korzystanie z naszych usług. Do zobaczenia!",
    "Życzę udanych zakupów i miłego dnia!",
    "Do widzenia! Jeśli masz jeszcze jakieś pytania, jestem tutaj!",
    "Dziękujemy za odwiedzenie sklepu z RTV i AGD. Do zobaczenia ponownie!",
    "Miłego dnia! Jeśli potrzebujesz pomocy, daj znać!",
    "Dziękuję za skorzystanie z chatbota. Do zobaczenia!",
    "Do widzenia! Miłego dnia i zapraszamy ponownie!",
    "Dziękuję za korzystanie z mojej pomocy. Do zobaczenia następnym razem!"
]

empathy = [
    (["Jestem bardzo smutny, że mój nowy telewizor nie działa poprawnie.",
      "Czuję się przygnębiony, ponieważ laptop, który kupiłem, ma wady fabryczne.",
      "Czuję smutek, że nie mogłem znaleźć żadnego dobrego sprzętu w przystępnej cenie.",
      "Jestem załamany, że uszkodziłem swoje słuchawki i teraz muszę kupić nowe.",
      "Czuję się przygnębiony, że nie mogę znaleźć żadnego produktu, który spełniałby moje oczekiwania."],
     ["Przepraszamy za niedogodności. Zaoferujemy Ci naprawę lub wymianę telewizora.",
      "Rozumiemy Twoje rozczarowanie. Prosimy o przyniesienie laptopa, a postaramy się go naprawić.",
      "Rozumiemy, że ceny mogą być frustrujące. Możemy przedstawić Ci inne opcje w Twoim budżecie.",
      "Przepraszamy za uszkodzone słuchawki. W naszym sklepie znajdziesz wiele innych modeli do wyboru.",
      "Przepraszamy, że nie znaleźliśmy odpowiedniego produktu. Czy mogę pomóc w znalezieniu alternatywy?"]),

    (["Jestem bardzo zadowolony z zakupu tego nowego laptopa.",
      "Cieszę się, że znalazłem świetną promocję na telewizor.",
      "To jest dokładnie to, czego potrzebowałem!",
      "Czuję się spełniony, że znalazłem doskonały smartfon.",
      "Jestem podekscytowany, że wreszcie mam nową konsolę do gier."],
     ["Cieszymy się, że jesteś zadowolony z zakupu! Jeśli masz jakiekolwiek pytania lub potrzebujesz pomocy, służymy wsparciem.",
      "To świetko, że znalazłeś promocję na telewizor! Jest to doskonała okazja.",
      "Jesteśmy bardzo zadowoleni, że znalazłeś to, czego potrzebowałeś. Jeśli będziesz potrzebował dodatkowej pomocy, daj nam znać.",
      "Cieszymy się, że jesteś spełniony swoim nowym smartfonem! Jeśli masz jakieś pytania dotyczące jego funkcji, z przyjemnością pomożemy.",
      "Gratulacje z powodu nowej konsoli! Mamy nadzieję, że dostarczy Ci wiele godzin rozrywki."]),

    (["Czuję ogromny żal, że zapłaciłem tak dużo za ten smartfon, który teraz jest w przecenie.",
      "Jestem rozżalony, że nie zauważyłem promocji na laptopa, który kupiłem kilka dni temu.",
      "Czuję się żałosny, że straciłem okazję na zakup tańszego telewizora.",
      "Jestem rozgoryczony, że nie otrzymałem darmowych akcesoriów do mojego zamówienia.",
      "Czuję się zawiedziony, że nie mogłem wymienić mojego produktu na inny model."],
     ["Rozumiemy Twój żal. Niestety, nie możemy zmienić ceny po zakupie, ale mamy inne atrakcyjne oferty, które mogą Cię zainteresować.",
      "Przykro nam, że przegapiłeś promocję. Czy jest coś innego, czym możemy Ci pomóc?",
      "Żałujemy, że nie skorzystałeś z promocji. Możemy przedstawić Ci inne produkty, które są w Twoim budżecie.",
      "Przepraszamy za niedogodności. Czy mogę zaoferować Ci inne akcesoria jako rekompensatę?",
      "Przepraszamy, że nie mogłeś wymienić produktu. Czy mogę pomóc w znalezieniu innych rozwiązań?"]),

    (["Jestem bardzo rozczarowany, że zamówione słuchawki nie pasują do mojego telefonu.",
      "Czuję się sfrustrowany, że mój nowy tablet nie działa poprawnie.",
      "Jestem zawiedziony jakością usług serwisowych w tym sklepie.",
      "Czuję się zdegustowany, że sprzedawca nie udzielił mi właściwych informacji na temat produktu.",
      "Jestem zawiedziony, że przesyłka z moim zamówieniem opóźniła się."],
     ["Przepraszamy za problem. Sprawdzimy, jak możemy rozwiązać tę sytuację i zaoferować Ci alternatywną opcję, która będzie pasować do Twojego telefonu.",
      "Rozumiemy Twoje rozczarowanie. Prosimy o przyniesienie tabletu, a postaramy się naprawić problem.",
      "Przepraszamy za złe doświadczenie. Czy mogę poprosić o więcej informacji, aby móc to zbadać?",
      "Przepraszamy za błędne informacje. Postaramy się, aby takie sytuacje się nie powtarzały.",
      "Przepraszamy za opóźnienie. Sprawdzimy status Twojej przesyłki i poinformujemy Cię o postępach."]),

    (["Czuję nienawiść do tego sklepu, który sprzedał mi uszkodzony tablet.",
      "Jestem wściekły na obsługę sklepu, która nie potrafiła mi pomóc z problemem.",
      "To jest nie do przyjęcia! Czuję ogromną frustrację.",
      "Jestem zdegustowany, że nie otrzymałem odpowiedniego wsparcia od sprzedawcy.",
      "Czuję wstręt do tej marki, która nie spełniła moich oczekiwań."],
     ["Przepraszamy za trudności, z którymi się spotkałeś. Proszę przynieść tablet z powrotem, a my postaramy się znaleźć satysfakcjonujące rozwiązanie tego problemu.",
      "Przepraszamy za brak pomocy. Czy możemy teraz podjąć działania, aby naprawić sytuację?",
      "Rozumiemy Twoją frustrację i będziemy pracować nad poprawą naszych usług.",
      "Przepraszamy za brak wsparcia. Czy możemy coś zrobić, aby rozwiązać Twój problem?",
      "Przepraszamy, że nie spełniliśmy Twoich oczekiwań. Czy możemy Cię prosić o więcej szczegółów, abyśmy mogli podjąć odpowiednie kroki?"]),

    (["Jestem niezwykle podekscytowany nowym głośnikiem, który właśnie zakupiłem!",
      "To jest dokładnie to, czego szukałem!",
      "Nie mogę się doczekać, aż go przetestuję!",
      "Jestem pełen radości, że znalazłem idealną kamerę do mojego hobby.",
      "Czuję ekscytację, że w końcu będę miał nowy smartwatch."],
     ["To wspaniale! Nowy głośnik z pewnością dostarczy Ci mnóstwo radości podczas słuchania ulubionej muzyki.",
      "Cieszymy się, że znalazłeś to, czego szukałeś! Jeśli będziesz potrzebował wsparcia lub porady, jesteśmy tutaj, aby Ci pomóc.",
      "Mamy nadzieję, że nowy głośnik spełni Twoje oczekiwania! Jeśli będziesz miał jakiekolwiek pytania dotyczące jego obsługi, nie wahaj się zwrócić do nas.",
      "Gratulacje z powodu znalezienia idealnej kamery! Jeśli będziesz potrzebował wskazówek dotyczących jej użytkowania, chętnie Ci pomożemy.",
      "Cieszymy się, że będziesz miał nowy smartwatch! Jeśli będziesz miał jakieś pytania lub potrzebujesz pomocy w konfiguracji, jesteśmy tu, aby Cię wesprzeć."])
]

def gpt2_generate(user_input, context):
    input_text = 'Ja: ' + user_input + "\nBot:"
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    input_ids = input_ids#.to(device)

    output = model.generate(input_ids, max_length=100, early_stopping=True, pad_token_id=tokenizer.eos_token_id, no_repeat_ngram_size=2)

    return tokenizer.decode(output[0], skip_special_tokens=True)

def generate_output(user_input, context):
    for phrases, responses in empathy:
        for i, phrase in enumerate(phrases):
            if phrase.lower() == user_input:
                return responses[i]

    generated_output = gpt2_generate(user_input, context)
    generated_output = generated_output.split("Bot: ")[1]
    generated_output = generated_output.replace("\n", '')

    return generated_output

def determine_emotion(text):
    emotions = te.get_emotion(text)
    sum = 0
    for i in emotions:
        sum += emotions[i]
    if sum == 0:
        return 'Neutral'
    else:
        return max(emotions, key=emotions.get)

def remove_punctuation(text):
    # Tworzenie tłumaczenia, które usuwa znaki interpunkcyjne
    translator = str.maketrans('', '', string.punctuation)
    # Zastosowanie tłumaczenia do tekstu i zwrócenie wyniku
    return text.translate(translator)

def draw_avatar(emotion):
    cv.namedWindow('Avatar')
    cv.moveWindow('Avatar', 600, 600)
    param_list = []

    if os.path.isfile('avatar.txt'):
        with open('avatar.txt') as f:
            for line in f:
                param_list.append(int(line.strip()))
    else:
        for i in range(13):
            param_list.append(0)

    if emotion == 'Happy':
        param_list[6] = 8
        param_list[7] = 10
        param_list[8] = 1
    elif emotion == 'Angry':
        param_list[6] = 2
        param_list[7] = 2
        param_list[8] = 8
    elif emotion == 'Sad':
        param_list[6] = 2
        param_list[7] = 8
        param_list[8] = 8
    elif emotion == 'Surprise':
        param_list[6] = 9
        param_list[7] = 8
        param_list[8] = 0
    elif emotion == 'Fear':
        param_list[6] = 2
        param_list[7] = 9
        param_list[8] = 0
    else:
        param_list[6] = 7
        param_list[7] = 0
        param_list[8] = 0

    avatar = pa.PyAvataaar(
        style=eval('pa.AvatarStyle.%s' % style[param_list[0]]),
        skin_color=eval('pa.SkinColor.%s' % skin_color[param_list[1]]),
        top_type=eval('pa.TopType.SHORT_HAIR_SHORT_FLAT.%s' % top_type[param_list[2]]),
        hair_color=eval('pa.HairColor.%s' % hair_color[param_list[3]]),
        hat_color=eval('pa.Color.%s' % hat_color[param_list[4]]),
        facial_hair_type=eval('pa.FacialHairType.%s' % facial_hair_type[param_list[5]]),
        mouth_type=eval('pa.MouthType.%s' % mouth_type[param_list[6]]),
        eye_type=eval('pa.EyesType.%s' % eye_type[param_list[7]]),
        eyebrow_type=eval('pa.EyebrowType.%s' % eyebrow_type[param_list[8]]),
        nose_type=pa.NoseType.DEFAULT,
        accessories_type=eval('pa.AccessoriesType.%s' % accessories_type[param_list[9]]),
        clothe_type=eval('pa.ClotheType.%s' % clothe_type[param_list[10]]),
        clothe_color=eval('pa.Color.%s' % clothe_color[param_list[11]]),
        clothe_graphic_type=eval('pa.ClotheGraphicType.%s' % clothe_graphic_type[param_list[12]])
    )
    avatar.render_png_file("AVATAR.png")
    new_avatar = cv.imread("AVATAR.png", 1)
    cv.imshow('Avatar', new_avatar)
    cv.waitKey(1)

if __name__ == '__main__':

    device = torch.device("mps")
    model = AutoModelForCausalLM.from_pretrained('./Model')
    tokenizer = AutoTokenizer.from_pretrained('./Model')

    model.eval()
    context = []

    print("Wpisz 'koniec' aby wyjść.")
    response = random.choice(powitania)
    print(response)
    context.append(response)
    emotion = 'Neutral'
    draw_avatar(emotion)

    while True:
        user_input = input('Ja: ')
        user_input = user_input.lower()

        if user_input.lower() == 'koniec':
            print(random.choice(pozegnania))
            break

        response = generate_output(user_input, context)
        print('Bot: ', response)
        emotion = determine_emotion(GoogleTranslator(source='auto', target='en').translate(remove_punctuation(user_input)))

        context.append(user_input)
        context.append(response)

        draw_avatar(emotion)



