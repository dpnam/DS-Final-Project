import json


def xstr(s):
    return '' if s is None else str(s)


def preprocess(inputFile: str, outputFile: str):
    with open(inputFile) as fIn, open(outputFile, "w") as fOut:
        tab = "\t"
        headers = (
            "area",
            "district",
            "address",
            "floors",
            "bedrooms",
            "toilets",
            "front",
            "entrance",
            "house_aspect",
            "balcony_aspect",
            "price"
        )
        fOut.write(f"{tab.join(headers)}\n")
        for i, line in enumerate(fIn):
            row = json.loads(line)
            if row["area"] == "Không xác định":
                area = None
            else:
                area = float(row["area"][:-3])

            if row["price"].endswith(" tỷ"):
                price = float(row["price"][:-3]) * 1000
            elif row["price"].endswith(" triệu"):
                price = float(row["price"][:-6])
            elif row["price"].endswith(" triệu/m²"):
                if area is not None:
                    price = float(row["price"][:-9]) * area
                else:
                    price = None
            else:
                price = None

            if price is None:
                continue

            district = row["district"]
            detail = row["detail"]
            features = detail["features"]

            address = features.get("Địa chỉ")
            if address is not None:
                address = address.replace(district, "").strip(" \t\r\n,.")
                if len(address) == 0:
                    address = None
            district = district.replace("Hồ Chí Minh", "").strip(" \t\r\n,.")

            floors = features.get("Số tầng")
            if floors is not None:
                floors = int(floors.replace(" (tầng)", ""))

            bedrooms = features.get("Số phòng ngủ")
            if bedrooms is not None:
                bedrooms = int(bedrooms.replace(" (phòng)", ""))

            toilets = features.get("Số toilet")
            if toilets is not None:
                toilets = int(toilets)

            front = features.get("Mặt tiền")
            if front is not None:
                front = float(front.replace(" (m)", "").replace(",", "."))

            entrance = features.get("Đường vào")
            if entrance is not None:
                entrance = float(entrance.replace(" (m)", "").replace(",", "."))

            houseAspect = features.get("Hướng nhà")
            balconyAspect = features.get("Hướng ban công")
            if balconyAspect is not None:
                if balconyAspect == "KXĐ":
                    balconyAspect = None

            row = (
                xstr(area),
                xstr(district),
                xstr(address),
                xstr(floors),
                xstr(bedrooms),
                xstr(toilets),
                xstr(front),
                xstr(entrance),
                xstr(houseAspect),
                xstr(balconyAspect),
                xstr(price)
            )
            fOut.write(f"{tab.join(row)}\n")



dataFile = "data/2019-11-29_23_18_43-removed-duplicate.json"
outputFile = "data/2019-11-29_23_18_43-preprocessed.csv"

preprocess(inputFile=dataFile, outputFile=outputFile)
