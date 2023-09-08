# ImageTextExtractor

This Python script extracts text from images, saves the obtained data to a text file, and later converts this textual data into an Excel file. It allows you to transfer data in formats suitable for flashcard applications or dictionary entries.

## Requirements

- Python 3.x
- `pytesseract` library
- `PIL` (Python Imaging Library)
- `pandas` library

You can install these requirements using the following commands in your terminal or command prompt:

```bash
pip install pytesseract pillow pandas
```

## Usage

1. Place your images in the `pic` folder.

2. Run the script:

    ```bash
    python main.py
    ```

3. Text extraction from the images will be performed, and the obtained data will be saved to `words.txt` and `data.xlsx` files.

## Notes

- The image format should be `.PNG`, `.jpg`, or `.jpeg`. (You may need to make adjustments in the code for different formats)

- Tesseract OCR should be installed on your system for `pytesseract` to work.

- Turkish character issues may occur in the extracted data and should be corrected if necessary. For this, my advice is to ask ChatGPT to correct the spelling errors in the translation section as "word, definition, translation."

- You may need to adjust the `tesseract_cmd` path. Below is an example that includes adjustments for different operating systems:

  **Windows:**
  ```python
  # Path to Tesseract OCR (example path for Windows)
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
  ```

  **Mac:**
  ```python
  # Path to Tesseract OCR (example path for Mac)
  pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'
  ```

  **Linux:**
  ```python
  # Path to Tesseract OCR (example path for Linux)
  pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
  ```

  These example paths indicate the directory where Tesseract OCR is installed. If you have installed Tesseract OCR in a different location, you should update the path accordingly. The file names "tesseract.exe" or "tesseract" in the example paths may vary depending on the operating system and Tesseract OCR version. To ensure that the path is correct, you can check the file name and path in the directory where Tesseract OCR is installed. If there are only eng files in these files, you need to move the relevant documents for [Turkish](https://github.com/tesseract-ocr/tessdata/blob/main/tur.traineddata) to the directory containing eng information. 

  Note to Myself: I can explain how to extract data from images with examples using conditions and loops.

Translate this readme file into Turkish.



# `TÜRKÇE`

# ImageTextExtractor

Bu Python betiği, görüntülerden metin çıkartma işlemi yaparak elde edilen verileri metin dosyasına kaydeder ve daha sonra bu metin verilerini bir Excel dosyasına dönüştürür. Bu, kelime kartı uygulamalarına veya sözlük verilerine uygun formatlarda veri aktarmanızı sağlar.

## Gereksinimler

- Python 3.x
- `pytesseract` kütüphanesi
- `PIL` (Python Imaging Library)
- `pandas` kütüphanesi

Bu gereksinimleri yüklemek için terminal veya komut istemcisinde şu komutları kullanabilirsiniz:

```bash
pip install pytesseract pillow pandas
```



## Kullanım

1. Görüntülerinizi `pic` klasörüne ekleyin.

2. Script'i çalıştırın:

    ```bash
    python main.py
    ```

3. Görüntülerden metin çıkartma işlemi yapılıp, elde edilen veriler `kelimeler.txt`  ve `veriler.xlsx` dosyasına kaydedilecektir.

## Notlar

- Görüntülerin formatı `.PNG`, `.jpg` veya `.jpeg` olmalıdır. (Farklı formatlar için kod içinde düzetme yapmalısınız)

- `pytesseract` için Tesseract OCR'ın sisteminizde yüklü olması gerekmektedir.

- Verilerde Türkçe karakter sorunları yaşanabilir, gerekirse düzeltilmelidir. Bunun için tavsiyem word, definition, translation şeklinde chatGPT'ye translation kısmındaki yazım hatalarını düzeltmesini istemenizdir. 

- `tesseract_cmd` yolunu düzenlemek gerekebilir. Aşağıda farklı işletim sistemleri için düzenlemeyi içeren bir örnek veriyorum:

  **Windows:**
  ```python
  # Tesseract OCR'nin yolu (Windows için örnek yol)
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
  ```

  **Mac:**
  ```python
  # Tesseract OCR'nin yolu (Mac için örnek yol)
  pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'
  ```

  **Linux:**
  ```python
  # Tesseract OCR'nin yolu (Linux için örnek yol)
  pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
  ```

  Bu örnek yollar, Tesseract OCR'ın yüklendiği dizini göstermektedir. Eğer Tesseract OCR'ı farklı bir yere yüklediyseniz, yolunu buna göre güncellemelisiniz. Örnek yollardaki "tesseract.exe" veya "tesseract" dosya isimleri, işletim sistemine ve Tesseract OCR sürümüne bağlı olarak değişebilir. Yolun doğru olduğundan emin olmak için Tesseract OCR'ın yüklendiği dizindeki dosya adını ve yolunu kontrol edebilirsiniz. Eğer bu dosyalar içinde sadece eng dosyaları varsa [türkçe](https://github.com/tesseract-ocr/tessdata/blob/main/tur.traineddata) için ilgili dokümanları eng bilgilerini içeren dosya yoluna atmanız gerekiyor. 
  
  Kendime Not: Örneklerle resimler üzerinden verilerin conditionlar ve looplar ile nasıl alınacağını açıklayabilirim. 

