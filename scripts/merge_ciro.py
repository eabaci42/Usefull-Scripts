import pandas as pd
import sys
import os

def merge_ciro(excel1_path, excel2_path, output_path="output.xlsx"):
    """
    İki Excel dosyası arasında müşteri adına göre ciro eşleştirmesi yapar.
    
    Args:
        excel1_path (str): Ciro bilgilerini içeren Excel dosyası
        excel2_path (str): Müşteri listesini içeren Excel dosyası
        output_path (str, optional): Sonuç dosyasının adı. Varsayılan: "output.xlsx"
    """
    # Dosyaların varlığını kontrol et
    if not os.path.exists(excel1_path):
        print(f"[✘] Hata: {excel1_path} dosyası bulunamadı.")
        return
    
    if not os.path.exists(excel2_path):
        print(f"[✘] Hata: {excel2_path} dosyası bulunamadı.")
        return
    
    try:
        # Excel 1: Tüm müşteri ve ciro listesi
        df1 = pd.read_excel(excel1_path)
        # Ciro.xlsx için kolon adlarını düzeltme
        df1.columns = ['Müşteri', 'Ciro']
        
        # Excel 2: Filtrelenmiş müşteri listesi
        df2 = pd.read_excel(excel2_path)
        # Müşteri.xlsx için tek kolon olduğundan yeni kolon ekleme
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
        
        # Sonuç dizini kontrol et
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Sonuçları yaz
        df2.to_excel(output_path, index=False)
        print(f"[✔] İşlem tamamlandı. Sonuç dosyası: {output_path}")
        
    except Exception as e:
        print(f"[✘] Hata: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Kullanım: python merge_ciro.py <ciro_listesi.xlsx> <musteri_listesi.xlsx> [sonuc_dosyasi.xlsx]")
    else:
        excel1 = sys.argv[1]
        excel2 = sys.argv[2]
        output_path = sys.argv[3] if len(sys.argv) > 3 else "output.xlsx"
        merge_ciro(excel1, excel2, output_path)
