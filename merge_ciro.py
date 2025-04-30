import pandas as pd
import sys

def merge_ciro(excel1_path, excel2_path, output_path="output.xlsx"):
    # Excel 1: Tüm müşteri ve ciro listesi
    df1 = pd.read_excel(excel1_path)
    df1.columns = ['Müşteri', 'Ciro']  # Kolon adlarını sabitliyoruz

    # Excel 2: Filtrelenmiş müşteri listesi, boş ciro sütunu
    df2 = pd.read_excel(excel2_path)
    df2.columns = ['Müşteri', 'Ciro']  # Aynı kolon adlarını burada da kullanıyoruz

    # Ciroyu eşleştir
    merged_df = df2.copy()
    merged_df['Ciro'] = merged_df['Müşteri'].map(df1.set_index('Müşteri')['Ciro'])

    # Sonuçları yaz
    merged_df.to_excel(output_path, index=False)
    print(f"[✔] İşlem tamamlandı. Sonuç dosyası: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Kullanım: python merge_ciro.py <excel1.xlsx> <excel2.xlsx>")
    else:
        excel1 = sys.argv[1]
        excel2 = sys.argv[2]
        merge_ciro(excel1, excel2)
