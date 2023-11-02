import re
import openpyxl

# Mở file txt
with open("product_train_0.txt", "r", encoding="utf-8") as f:
    # Đọc dữ liệu từ file txt
    lines = f.readlines()

    # Tạo file excel
    wb = openpyxl.Workbook()
    sheet = wb.active

    # Thêm dữ liệu vào file excel
    for i, line in enumerate(lines, start=1):
        # Tìm và loại bỏ ký tự _label_
        line = re.sub("_label_", "", line)
        # Chia dòng thành hai phần
        parts = line.split(' ', 1)
        # Thêm dữ liệu vào file excel
        # parts[0].strip().replace( "_" , " ")
        sheet['A' + str(i)] = parts[0].strip()
        if len(parts) > 1:
            sheet['B' + str(i)] = parts[1].strip()

    # Lưu file excel
    labels = [item.value for item in sheet['A']]
    labels_set = set(labels)
    print(len(labels))
    print(len(labels_set))
    # wb.save("data_output.xlsx")

