data_mhs = [
    {"Nama": "Jonas", "NIM": "24415001", "Tugas": 95, "UTS": 75, "UAS": 80},
    {"Nama": "Gracia", "NIM" : "24415002", "Tugas": 70, "UTS": 90, "UAS": 90},
    {"Nama": "Lopez", "NIM" : "24415003", "Tugas": 85, "UTS": 90, "UAS": 95},
    {"Nama": "Eric", "NIM" : "24415004", "Tugas": 75, "UTS": 80, "UAS": 85},
    {"Nama": "Ricardo", "NIM" : "24415005", "Tugas": 80, "UTS": 85, "UAS": 80},
]

nilai_akhir = [
    {
        **mhs,
        "Nilai Akhir": (
            mhs["Tugas"] * 0.3
            + mhs["UTS"] * 0.3
            + mhs["UAS"] * 0.4
        )
    }
    for mhs in data_mhs
]

for mhs in nilai_akhir:
    print(
        f"Nama: {mhs['Nama']}, "
        f"NIM: {mhs['NIM']}, "
        f"Nilai Akhir: {mhs['Nilai Akhir']:.2f}"
    )