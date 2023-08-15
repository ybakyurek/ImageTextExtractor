import pytesseract
from PIL import Image
import os
import pandas as pd

# Tesseract OCR'nin yolu
pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'


def ocr_and_save(image_path, lang):
    # Resmi açın
    image = Image.open(image_path)

    # Tesseract OCR ile metni çıkarın
    extracted_text = pytesseract.image_to_string(image, lang=lang)

    # Metni satırlara ayırın
    lines = extracted_text.strip().split('\n')

    # Sonuçları listeye ekleyin
    results = []

    word = None
    word_type = None
    definition = None
    example = None
    synonyms = None
    translation = None


    # Word'un alınması. Resme göre bazen arada yeni satır algılıyor.
    for i in range(len(lines)):
        if "/5 x" in lines[i]:
            word = lines[i + 2].strip()
            if word == "":
                word = lines[i + 1].strip()
            word_type = lines[i + 3].strip()
            if word_type == "":
                word_type = lines[i + 4].strip()
            word_type = word_type
            if "/" in word_type:
                index_of_slash = word_type.index("/")
                word_type = word_type[:index_of_slash].strip()

        if "example" in lines[i]:
            example = lines[i + 1].strip()

            # "synonyms" ya da "translation" kısmını bulana kadar bir sonraki satırları da ekleyin
            j = i + 2
            while j < len(lines):
                if "synonyms" in lines[j] or "translation" in lines[j]:
                    break
                example += " " + lines[j].strip()
                j += 1

        if "translation" in lines[i]:
            translation = lines[i + 1].strip()
            if translation == "":
                translation = lines[i + 2].strip()
            # print(translation)

        if "definition" in lines[i]:
            definition = lines[i + 1].strip()

            # "example" kısmını bulana kadar bir sonraki satırları da ekleyin
            j = i + 2
            while j < len(lines):
                if "example" in lines[j]:
                    break
                definition += " " + lines[j].strip()
                j += 1

        if "synonyms" in lines[i]:
            synonyms = lines[i + 1].strip()

            # "translation" kısmını bulana kadar bir sonraki satırları da ekleyin
            j = i + 2
            while j < len(lines):
                if "translation" in lines[j]:
                    break
                synonyms += " " + lines[j].strip()
                j += 1

    blank_example = example.replace(word, "...")
    # Turkce karakterlerde sorun olduugu icin o kismi chatgpt'ile duzeltmek gerekiyor.
    # Python ile duzeltmek istedigimizde yanlis duzeltmeler yapabiliyor
    results.append(
        f"{word}:{word_type}:{definition}:({translation}):{synonyms}:{example}:{blank_example}:{word}({word_type})~{blank_example}:{word}~{definition}")

    # Metni bir txt dosyasına kaydedin
    with open("kelimeler.txt", "a", encoding="utf-8") as file:
        for result in results:
            file.write(result.replace("|", "I") + "\n")


def process_images_in_folder(folder_path, lang):
    # Klasördeki tüm dosyaların listesini alın
    file_list = os.listdir(folder_path)

    # Resim dosyalarını seçin (isteğe bağlı olarak belirli uzantıları da filtreleyebilirsiniz)
    image_files = [f for f in file_list if f.endswith(('.PNG', '.jpg', '.jpeg'))]

    for image_file in image_files:
        # Resmin tam yolu
        image_path = os.path.join(folder_path, image_file)
        print(image_path)

        # OCR ve kaydetme işlemini çağırın
        ocr_and_save(image_path, lang)

def txt_to_xlsx(folder_path, xlsx_name):
    # Dosyadan verileri okuma
    with open(folder_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # ":" karakterine göre bölmek ve veriyi düzenlemek
    data = [line.strip().split(":") for line in lines]

    # Pandas DataFrame oluşturma

    df = pd.DataFrame(data,
                      columns=["word", "word_type", "definition", "translation", "synonyms", "example", "blank_example",
                               "word_type_blankex", "word_def"])

    # DataFrame'i Excel dosyasına yazdırma
    df.to_excel(xlsx_name+".xlsx", index=False)


# Örnek çağrı
process_images_in_folder("/Users/yba/PycharmProjects/pythonProject/pic", lang="eng+tur")
txt_to_xlsx("kelimeler.txt","veriler")


