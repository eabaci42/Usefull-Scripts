import pandas as pd
import sys

def merge_ciro(excel1_path, excel2_path, output_path="output.xlsx"):
    # Excel 1: Tüm müşteri ve ciro listesi
    df1 = pd.read_excel(excel1_path)
    # 2025ciro.xlsx için kolon adlarını düzeltme
    df1.columns = ['Müşteri', 'Ciro']
    
    # Excel 2: Filtrelenmiş müşteri listesi
    df2 = pd.read_excel(excel2_path)
    # alpercebi.xlsx için tek kolon olduğundan yeni kolon ekleme
    df2.columns = ['Müşteri']
    df2['Ciro'] = 0  # Boş ciro sütunu ekliyoruz
    
    # Ciroyu eşleştir
    for index, row in df2.iterrows():
        müşteri = row['Müşteri']
        # Tam eşleşme kontrolü yapalım
        match = df1[df1['Müşteri'] == müşteri]
        
        if not match.empty:
            df2.at[index, 'Ciro'] = match.iloc[0]['Ciro']
        else:
            # Kısmi eşleşme kontrolü
            for idx, master_row in df1.iterrows():
                if müşteri in master_row['Müşteri'] or master_row['Müşteri'] in müşteri:
                    df2.at[index, 'Ciro'] = master_row['Ciro']
                    break
    
    # Sonuçları yaz
    df2.to_excel(output_path, index=False)
    print(f"[✔] İşlem tamamlandı. Sonuç dosyası: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Kullanım: python merge_ciro.py <excel1.xlsx> <excel2.xlsx>")
    else:
        excel1 = sys.argv[1]
        excel2 = sys.argv[2]
        merge_ciro(excel1, excel2)
