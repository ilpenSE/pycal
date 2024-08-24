from decimal import Decimal, getcontext
from math import factorial
import math
from decimal import Decimal, getcontext

INFINTESIMAL = 1e-10
LANGUAGE = "en"

def sqrt_newton(x):
    if x < 0:
        raise ValueError("Negatif sayıların karekökü alınamaz!")
    if x == 0:
        return 0
    guess = x
    while abs(guess * guess - x) > INFINTESIMAL:
        guess = (guess + x / guess) / 2
    return guess

def calculate_e(precision):
    getcontext().prec = precision + 2
    e = Decimal(1)
    factorial = Decimal(1)
    k = 1
    while True:
        factorial *= k
        term = Decimal(1) / factorial
        new_e = e + term
        if e == new_e:
            break
        e = new_e
        k += 1
    return round(e, precision)

def calculate_pi(n):
    getcontext().prec = n + 2
    t= Decimal(0)
    pi = Decimal(0)
    deno= Decimal(0)

    for k in range(n):
        t = ((-1)**k)*(factorial(6*k))*(13591409+545140134*k)
        deno = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
        pi += Decimal(t)/Decimal(deno)
    pi = pi * Decimal(12) / Decimal(640320 ** Decimal(1.5))
    pi = 1/pi
    return round(pi,n)

supportedLangs = {
    "tr": "Türkçe",
    "en": "English",
    "de": "Deutsch",
    "fr": "Français"
}

langKeys = {
    "tr": {
        "title": "İRRASYONEL HESAPLAYICI",
        "op1": "∏ SAYISINI HESAPLA",
        "op2": "E SAYISINI HESAPLA",
        "op3": "ALTIN ORANI HESAPLA",
        "op4": "KAREKÖK HESAPLA",
        "op5": "HASSASİYETİ AYARLA (VARS.:10)",
        "op6": "HASSASİYETİ AL",
        "op7": "DİLİ DEĞİŞTİR",
        "op8": "DESTEKLENEN DİLLERİ AL",
        "op9": "YARDIM MESAJINI YAZDIR",
        "op10": "ÇIK",
        "warning": "UYARI: Hassasiyet ne kadar büyükse hesap süresi de o kadar uzar.",
        "select_op": "İşlem seç",
        "err_num": "Lütfen bir sayı giriniz",
        "type_sqrt": "Karekök alınacak sayıyı girin",
        "result": "Sonuç",
        "suc_sens": "Hassasiyet artık {}!",
        "sens": "Hassasiyet",
        "type_sens": "Hassasiyeti girin",
        "err_sens": "Hassasiyet {} ile {} arasında olmalıdır!",
        "suc_lang": "Dil başarıyla {} olarak değiştirildi",
        "sup_lang": "Desteklenen diller",
        "err_lang": "Lütfen desteklenen bir dil giriniz!",
        "type_lang": "Değiştirmek istediğiniz dili girin (tr, en şeklinde olmalı)"
    },
    "en": {
        "title": "IRRATIONAL CALCULATOR",
        "op1": "CALCULATE ∏ NUMBER",
        "op2": "CALCULATE E NUMBER",
        "op3": "CALCULATE GOLDEN RATIO",
        "op4": "CALCULATE SQUARE ROOT",
        "op5": "SET SENSITIVITY (DEF.:10)",
        "op6": "GET SENSITIVITY",
        "op7": "CHANGE LANGUAGE",
        "op8": "GET SUPPORTED LANGUAGES",
        "op9": "PRINT HELP MESSAGE",
        "op10": "EXIT",
        "warning": "WARNING: The greater the sensitivity, the longer the calculation time.",
        "select_op": "Select an operation",
        "err_num": "Please enter a number",
        "type_sqrt": "Enter the number to take the square root of",
        "result": "Result",
        "suc_sens": "Sensitivity is now {}!",
        "sens": "Sensitivity",
        "type_sens": "Enter the sensitivity",
        "err_sens": "Sensitivity must be between {} and {}!",
        "suc_lang": "Language has been successfully changed to {}",
        "sup_lang": "Supported Languages",
        "err_lang": "Please enter a supported language!",
        "type_lang": "Enter the language you wanna change to (must be like tr, en)"
    },
    "fr": {
        "title": "CALCULATEUR IRRATIONAL",
        "op1": "CALCULER LE NOMBRE ∏",
        "op2": "CALCULER LE NOMBRE E",
        "op3": "CALCULER LE RATIO D'OR",
        "op4": "CALCULER LA RACINE CARREE",
        "op5": "DEFINIR LA SENSIBILITE (DEF.:10)",
        "op6": "OBTENIR LA SENSIBILITE",
        "op7": "CHANGER DE LANGUE",
        "op8": "OBTENIR LES LANGUES SUPPORTEES",
        "op9": "IMPRIMER LE MESSAGE D'AIDE",
        "op10": "QUITTER",
        "warning": "AVERTISSEMENT : Plus la sensibilité est élevée, plus le temps de calcul est long.",
        "select_op": "Sélectionnez une opération",
        "err_num": "Veuillez entrer un nombre",
        "type_sqrt": "Entrez le nombre dont vous voulez prendre la racine carrée",
        "result": "Résultat",
        "suc_sens": "La sensibilité est maintenant {}!",
        "sens": "Sensibilité",
        "type_sens": "Entrez la sensibilité",
        "err_sens": "La sensibilité doit être comprise entre {} et {}!",
        "suc_lang": "La langue a été changée avec succès en {}",
        "sup_lang": "Langues supportées",
        "err_lang": "Veuillez entrer une langue supportée!",
        "type_lang": "Entrez la langue à laquelle vous souhaitez changer (doit être comme tr, en)"
    },
    "de": {
        "title": "IRRATIONALER RECHNER",
        "op1": "∏-ZAHL BERECHNEN",
        "op2": "E-ZAHL BERECHNEN",
        "op3": "GOLDENES VERHÄLTNIS BERECHNEN",
        "op4": "WURZEL BERECHNEN",
        "op5": "EMPFINDLICHKEIT FESTLEGEN (VORG.:10)",
        "op6": "EMPFINDLICHKEIT ABFRAGEN",
        "op7": "SPRACHE ÄNDERN",
        "op8": "UNTERSTÜTZTE SPRACHEN ABFRAGEN",
        "op9": "HILFSMELDUNG DRUCKEN",
        "op10": "BEENDEN",
        "warning": "WARNUNG: Je höher die Empfindlichkeit, desto länger die Berechnungszeit.",
        "select_op": "Wählen Sie eine Operation",
        "err_num": "Bitte geben Sie eine Zahl ein",
        "type_sqrt": "Geben Sie die Zahl ein, von der die Wurzel gezogen werden soll",
        "result": "Ergebnis",
        "suc_sens": "Die Empfindlichkeit ist jetzt {}!",
        "sens": "Empfindlichkeit",
        "type_sens": "Geben Sie die Empfindlichkeit ein",
        "err_sens": "Die Empfindlichkeit muss zwischen {} und {} liegen!",
        "suc_lang": "Die Sprache wurde erfolgreich auf {} geändert",
        "sup_lang": "Unterstützte Sprachen",
        "err_lang": "Bitte geben Sie eine unterstützte Sprache ein!",
        "type_lang": "Geben Sie die Sprache ein, zu der Sie wechseln möchten (muss wie tr, en sein)"
    }
}

def getKey(key, *argv):
    temp = langKeys[LANGUAGE][key]
    return temp.format(*argv)

def show_help():
    print("== " + getKey("title") + " ==")
    print("[1] " + getKey("op1"))
    print("[2] " + getKey("op2"))
    print("[3] " + getKey("op3"))
    print("[4] " + getKey("op4"))
    print("[5] " + getKey("op5"))
    print("[6] " + getKey("op6"))
    print("[7] " + getKey("op7"))
    print("[8] " + getKey("op8"))
    print("[9] " + getKey("op9"))
    print("[-1] " + getKey("op10"))
    print(getKey("warning"))

show_help()

while True:
    op = input("> " + getKey("select_op") + ": ")
    try:
        op = int(op)
    except ValueError:
        print(getKey("err_num"))
        continue

    precision = int(-math.log10(INFINTESIMAL) * 2)

    match op:
        case 1: # pi
            print("π ~ " + str(calculate_pi(precision)))

        case 2: # e
            print("e ~ " + str(calculate_e(precision)))

        case 3: # phi
            phi = (1 + sqrt_newton(5)) / 2
            txt = "φ ~ {r:."+str(int(precision))+"f}"
            print(txt.format(r=phi))

        case 4: # sqrt
            a = input("> " + getKey("type_sqrt") + ": ")
            try:
                print(getKey("result") + ": " + str(sqrt_newton(float(a))))
            except ValueError:
                print(getKey("err_num"))

        case 5: # sens
            a = input("> " + getKey("type_sens") + " (1-14): ")
            try:
                a = int(a)
                if not a in range(0, 15):
                    print(getKey("err_sens", 1, 14))
                    continue
            except ValueError:
                print(getKey("err_num"))
                continue
            INFINTESIMAL = pow(10, -int(a))
            print(getKey("suc_sens", a))

        case 6: # getsens
            print(getKey("sens") + ": " + str(int(-math.log10(INFINTESIMAL))))

        case 7:
            lang = input("> " + getKey("type_lang") + ": ").lower()
            if not lang in supportedLangs.keys():
                print(getKey("err_lang"))
                continue
            LANGUAGE = lang
            print(getKey("suc_lang", supportedLangs[lang]))

        case 8:
            print(getKey("sup_lang") + ": " + str.join(", ", supportedLangs.values()))

        case 9:
            show_help()

        case -1:
            break
        case _:
            print(getKey("err_num"))
            continue