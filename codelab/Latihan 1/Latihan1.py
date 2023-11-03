def konversi(minggu=0, hari=0, jam=0, menit=0):
    return ((minggu * 7 * 24 * 60) + (hari * 24 * 60) + (jam * 60) + menit)

data = ["3 minggu 3 hari 7 jam 21 menit", "5 minggu 5 hari 8 jam 11 menit", "7 minggu 1 hari 5 jam 33 menit"]

output_data = []
for item in data:
    parts = item.split()
    minggu = int(parts[0])
    hari = int(parts[2])
    jam = int(parts[4])
    menit = int(parts[6])
    hasil_konversi = konversi(minggu, hari, jam, menit)
    output_data.append(hasil_konversi)

print("OutputData =", output_data)