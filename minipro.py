parking_manage = []

next_id = 1
choice = ''

while choice != '5':

    print("\n" + "=" * 55)
    print("        QUẢN LÝ BÃI XE - SMART PARKING")
    print("=" * 55)
    print("1. Check-in (Đăng ký xe vào)")
    print("2. Báo cáo tồn kho (Hiển thị danh sách)")
    print("3. Tìm kiếm xe (Theo biển số)")
    print("4. Check-out (Xử lý xe ra & Tính phí)")
    print("5. Thoát chương trình")
    print("=" * 55)

    choice = input("Nhập lựa chọn của bạn (1-5): ")

    match choice:

        case '1':

            plate = input("Nhập biển số xe: ").strip()

            if plate == "":
                print("Biển số không được để trống!")
                continue

            duplicate = False

            for vehicle in parking_manage:
                if vehicle["plate"].upper() == plate.upper():
                    duplicate = True
                    break

            if duplicate:
                print("Biển số đã tồn tại!")
                continue

            vehicle_type = input("Loại xe (1-Xe máy, 2-Ô tô): ")

            while vehicle_type != "1" and vehicle_type != "2":
                print("Vui lòng nhập 1 hoặc 2!")
                vehicle_type = input("Loại xe (1-Xe máy, 2-Ô tô): ")

            if vehicle_type == "1":
                vehicle_type = "Xe máy"
            else:
                vehicle_type = "Ô tô"

            entry_time = input("Nhập giờ vào (0-23): ")

            while not entry_time.isdigit() or int(entry_time) < 0 or int(entry_time) > 23:
                print("Giờ không hợp lệ!")
                entry_time = input("Nhập giờ vào (0-23): ")

            vehicle = {
                "id": next_id,
                "plate": plate.upper(),
                "type": vehicle_type,
                "entry_time": int(entry_time)
            }

            parking_manage.append(vehicle)
            next_id += 1

            print("Check-in thành công!")

        case '2':

            if len(parking_manage) == 0:
                print("Bãi xe hiện đang trống!")

            else:
                print("-" * 55)
                print(f"{'ID':<5} | {'Biển số':<15} | {'Loại xe':<15} | {'Giờ vào':<10}")
                print("-" * 55)

                for vehicle in parking_manage:
                    print(f"{vehicle['id']:<5} | {vehicle['plate']:<15} | {vehicle['type']:<15} | {vehicle['entry_time']:<10}")

        case '3':

            plate = input("Nhập biển số cần tìm: ").strip()

            found = False

            for vehicle in parking_manage:

                if vehicle["plate"].upper() == plate.upper():

                    print("\nThông tin xe:")
                    print(vehicle)

                    found = True
                    break

            if found == False:
                print("Không tìm thấy xe!")

        case '4':

            plate = input("Nhập biển số xe cần check-out: ").strip()

            found_vehicle = None

            for vehicle in parking_manage:
                if vehicle["plate"].upper() == plate.upper():
                    found_vehicle = vehicle
                    break

            if found_vehicle == None:
                print("Không tìm thấy xe!")
                continue

            exit_time = input("Nhập giờ ra (0-23): ")

            while (
                not exit_time.isdigit()
                or int(exit_time) > 23
                or int(exit_time) < found_vehicle["entry_time"]
            ):
                print("Giờ ra không hợp lệ!")
                exit_time = input("Nhập giờ ra (0-23): ")

            exit_time = int(exit_time)

            hours = exit_time - found_vehicle["entry_time"]

            if found_vehicle["type"] == "Xe máy":
                fee = hours * 5000
            else:
                fee = hours * 10000

            print("\nCHECK-OUT THÀNH CÔNG")
            print("Biển số :", found_vehicle["plate"])
            print("Loại xe :", found_vehicle["type"])
            print("Giờ vào :", found_vehicle["entry_time"])
            print("Giờ ra  :", exit_time)
            print("Số giờ  :", hours)
            print("Phí gửi :", fee, "VNĐ")

            parking_manage.remove(found_vehicle)

        case '5':
            print("Thoát chương trình!")

        case _:
            print("Lựa chọn không hợp lệ!")
