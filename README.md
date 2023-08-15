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

