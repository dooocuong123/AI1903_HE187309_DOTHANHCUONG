class Stock:
    def __init__(self, code, open_price, close_price):
        self.code = code
        self.open_price = open_price
        self.close_price = close_price

def read_file(filename):
    stocks = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        num_stocks = int(lines[0])
        for line in lines[1:]:
            data = line.strip().split()
            code = data[0]
            open_price = float(data[1])
            close_price = float(data[2])
            stocks.append(Stock(code, open_price, close_price))
    return stocks

def print_average_diff(stocks):
    codes = sorted(list(set([stock.code for stock in stocks])))
    for code in codes:
        total_diff = 0
        count = 0
        for stock in stocks:
            if stock.code == code:
                total_diff += stock.close_price - stock.open_price
                count += 1
        if count > 0:
            average_diff = total_diff / count
            print(f"{code}\t{average_diff:.3f}")

def search_stock(stocks, code):
    max_close = float('-inf')
    min_close = float('inf')
    found = False
    for stock in stocks:
        if stock.code == code:
            found = True
            max_close = max(max_close, stock.close_price)
            min_close = min(min_close, stock.close_price)
    if found:
        print(f"Max close price: {max_close:.3f}\nMin close price: {min_close:.3f}")
    else:
        print("Stock code not found.")

def find_trending_stocks(stocks):
    trending_stocks = set()
    for i in range(len(stocks) - 1):
        if stocks[i].close_price > stocks[i].open_price and stocks[i+1].close_price > stocks[i+1].open_price:
            trending_stocks.add(stocks[i].code)
    print("Trending stocks on both Day 1 and Day 2:")
    for code in trending_stocks:
        print(code)

def find_longest_increase(stocks):
    increase_counts = {}
    for stock in stocks:
        if stock.code not in increase_counts:
            increase_counts[stock.code] = 0
        if stock.close_price > stock.open_price:
            increase_counts[stock.code] += 1
    max_increase = max(increase_counts.values())
    longest_increase_stocks = [code for code, count in increase_counts.items() if count == max_increase]
    print(f"Mã có số ngày tăng lớn nhất ({max_increase} ngày):")
    for code in longest_increase_stocks:
        print(f"{code}: {max_increase} days")
        
        
def not_have_data():
    print("RAM không có dữ liệu để đọc. Vui lòng chọn 1 để truy xuất dữ liệu.")

def main():
    filename = "data.txt"
    stocks = []
    data_loaded = False

    while True:
        print("\nMenu:")
        print("1. Đọc file và in thông tin") #phải chọn lựa chọn này nếu không lựa chọn khác sẽ chạy lỗi
        print("2. Tìm kiếm theo mã cổ phiếu")
        print("3. Tìm mã chứng khoán có xu hướng tăng")
        print("4. Tìm mã có số ngày tăng lớn nhất")
        print("5. Thoát chương trình")

        choice = input("Chọn chức năng (1-5): ")

        if choice == '1':
            stocks = read_file(filename)
            print_average_diff(stocks)
            data_loaded = True
        elif choice == '2':
            if data_loaded:
                code = input("Nhập mã cổ phiếu: ")
                search_stock(stocks, code)
            else:
                not_have_data()
        elif choice == '3':
            if data_loaded:
                find_trending_stocks(stocks)
            else:
                not_have_data()
        elif choice == '4':
            if data_loaded:
                find_longest_increase(stocks)
            else:
                not_have_data()
        elif choice == '5':
            print("Tác giả: Đỗ Thành Cường - HE187309")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
