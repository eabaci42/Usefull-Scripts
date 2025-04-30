# Veri İşleme Araçları

Bu repo, Excel dosyaları arasında veri eşleştirme ve analiz işlemleri yapmak için kullanılan çeşitli Python araçlarını içerir.

## İçindekiler

- [Dosya Yapısı](#dosya-yapısı)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Programlar](#programlar)
  - [merge_ciro.py](#merge_ciropy)

## Dosya Yapısı

```
Usefull-Scripts/
├── data/                  # Veri dosyaları dizini
│   ├── cirolari/          # Ciro excel dosyaları
│   ├── musteriler/        # Müşteri excel dosyaları
│   └── sonuclar/          # Oluşturulan sonuç dosyaları
├── scripts/               # Script dosyaları
│   ├── merge_ciro.py      # Ciro eşleştirme programı
│   └── ...                # Diğer script dosyaları
├── README.md              # Dökümentasyon
├── requirements.txt       # Python bağımlılıkları
└── .gitignore             # Git tarafından görmezden gelinecek dosyalar
```

## Kurulum

1. Gerekli Python paketlerini yükleyin:

```bash
pip install -r requirements.txt
```

## Kullanım

Her program, ilgili script dosyasında belirtilen parametreler ve seçeneklerle çalıştırılabilir.

## Programlar

### merge_ciro.py

Bu program, iki Excel dosyası arasında müşteri adına göre ciro eşleştirmesi yapar.

#### Kullanım

```bash
python scripts/merge_ciro.py <ciro_listesi.xlsx> <musteri_listesi.xlsx> [sonuc_dosyasi.xlsx]
```

#### Parametreler

- `ciro_listesi.xlsx`: Tüm müşteri ve ciro bilgilerini içeren Excel dosyası
- `musteri_listesi.xlsx`: Ciro bilgisi eşleştirilecek müşteri listesi Excel dosyası
- `sonuc_dosyasi.xlsx` (Opsiyonel): Sonuç dosyasının adı (verilmezse "output.xlsx" olarak kaydedilir)

#### Örnek

```bash
python scripts/merge_ciro.py data/cirolari/2025ciro.xlsx data/musteriler/alpercebi.xlsx data/sonuclar/alper_sonuc.xlsx
``` 