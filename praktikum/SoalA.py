from functools import reduce

# Daftar transaksi pembelian produk
transactions = [
    {"product": "Buku", "Price": 10000, "quantity": 2},
    {"product": "Pensil", "Price": 2000, "quantity": 5},
    {"product": "Pensil", "Price": 2000, "quantity": 3},
    {"product": "Pulpen", "Price": 5000, "quantity": 2},
    {"product": "Buku", "Price": 12000, "quantity": 1},
    {"product": "Pulpen", "Price": 6000, "quantity": 4}
]

# Fungsi untuk menghitung total harga transaksi menggunakan lambda


def calculate_transaction_total(
    transaction): return transaction["Price"] * transaction["quantity"]

# Fungsi untuk menyaring transaksi hanya untuk produk tertentu dengan HOF


def filter_transactions_by_product(transactions, product_name):
    filtered_transactions = filter(
        lambda transaction: transaction["product"] == product_name, transactions)
    return list(filtered_transactions)


# Input nama produk yang ingin disaring
product_filter_input = input("Masukkan nama produk yang ingin disaring: ")

# Menggunakan filter() untuk menyaring transaksi sesuai input produk
filtered_transactions = filter_transactions_by_product(
    transactions, product_filter_input)

# Menggunakan map() untuk menghitung total harga untuk setiap transaksi yang tersaring
transaction_totals = list(
    map(calculate_transaction_total, filtered_transactions))

# Menggunakan reduce() untuk menghitung total pendapatan dari semua transaksi yang tersaring
total_income = reduce(lambda x, y: x + y, transaction_totals, 0)

# Menampilkan output
print(f"Transaksi pembelian Produk {product_filter_input}:")
for transaction in filtered_transactions:
    print(transaction)

print("\nTotal Harga untuk Setiap Transaksi Produk", product_filter_input, ":")
for total in transaction_totals:
    print(total)

print("\nTotal Pendapatan dari Transaksi Produk",
      product_filter_input, ":", total_income)
print("Total Jumlah Item Terjual dari Produk", product_filter_input, ":",
      sum([transaction["quantity"] for transaction in filtered_transactions]))
