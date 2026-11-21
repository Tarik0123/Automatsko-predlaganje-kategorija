import joblib

model = joblib.load("train_model.py")

while True:
    unos = input("Unesite tekst za predikciju kategorije (ili 'exit' za izlaz): ")
    
    if unos.lower() == 'exit':
        break

    predikcija = model.predict([unos])
    print(f"Predikcija kategorije: {predikcija[0]}")