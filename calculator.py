import sympy as sp
import math

constants = {
    'pi': sp.pi, # 3.1415926535897932384626433832795 (Pi sayısı)
    'e': sp.E, # 2.7182818284590452353602874713527 (Euler sayısı)
    'phi': (1 + sp.sqrt(5)) / 2 # 1.6180339887 (Altın Oran)
}

def nthroot(n, value):
    return value ** (1/n)

functions = {
    'log': lambda x, base=10: sp.log(x, base),
    'ln': sp.ln,
    'kök': sp.sqrt,
    'sin': sp.sin,
    'cos': sp.cos,
    'tan': sp.tan,
    'sec': sp.sec,
    'csc': sp.csc,
    'cot': sp.cot,
    'arcsin': sp.asin,
    'arccos': sp.acos,
    'arctan': sp.atan,
    'arccot': sp.acot,
    'arcsec': sp.asec,
    'arccsc': sp.acsc,
    'nkök': nthroot,
    'üs': math.pow
}

def show_help():
    print("== HESAP MAKİNESİ ==")
    print("Bu hesap makinesi işlem önceliğine dikkat eder ve fonksiyonlar parantezle kullanılmalıdır.")
    print("pi: π sayısını verir, fonksiyonlarda kullanılabilir")
    print("e: e sayısını verir")
    print("phi: φ sayısını (altın oran) verir")
    print("sin(x): Radyan cinsinden x'in sinüsünü hesaplar")
    print("cos(x): Radyan cinsinden x'in kosinüsünü hesaplar")
    print("tan(x): Radyan cinsinden x'in tanjantını hesaplar")
    print("cot(x): Radyan cinsinden x'in kotanjantını hesaplar")
    print("sec(x): Radyan cinsinden x'in sekantını hesaplar")
    print("csc(x): Radyan cinsinden x'in kosekantını hesaplar")
    print("arcsin(x): x'in ters sinüsünü hesaplar")
    print("arccos(x): x'in ters kosinüsünü hesaplar")
    print("arctan(x): x'in ters tanjantını hesaplar")
    print("arccot(x): x'in ters kotanjantını hesaplar")
    print("arcsec(x): x'in ters sekantını hesaplar")
    print("arccsc(x): x'in ters kosekantını hesaplar")
    print("log(x): x'in 10 tabanında logaritmasını hesaplar")
    print("log(x, n): x'in n tabanında logaritmasını hesaplar")
    print("ln(x): x'in doğal logaritmasını hesaplar")
    print("üs(x, y): x üssü y'yi hesaplar")
    print("kök(x): x'in karekökünü hesaplar")
    print("nkök(n, x): x'in n. dereceden kökünü hesaplar")
    print("Üs almak için şunu da kullanabilirsiniz: x**y (x üssü y) Bu işlem fonksiyonlar içinde uygulanabilir: log(100)**2 (=4)")


def evaluate_expression(expr):
    try:
        context = {**constants, **functions}
        symbolic_expr = eval(expr, {"__builtins__": None}, context)
        result = sp.N(symbolic_expr)
        return result
    except Exception as e:
        raise e

print("Yardım için y, h, help ya da yardım yazabilirsiniz")
while True:
    expression = input("> İfadeyi yaz: ")

    if (['yardım', 'help', 'h', 'y'].__contains__(expression)):
        show_help()
    else:
        try:
            result = evaluate_expression(expression)
            print(f"Sonuç: {result}")
        except:
            print("Lütfen doğru bir ifade girin")