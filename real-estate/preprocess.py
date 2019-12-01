import json
import os
import re
from itertools import filterfalse


def xstr(s):
    if s is None:
        return ""
    if isinstance(s, bool):
        return "1" if s else "0"
    return str(s)


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
            "interior",
            "near_center",
            "owner",
            "alley",
            "villa",
            "new",
            "price",
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

            description = detail["description"].lower()

            interiorStr = features.get("Nội thất")
            if interiorStr is None:
                interior = None
            else:
                interiorStr = interiorStr.lower()
                noStartStrs = ["ko", "khong", "không", "k ", "kxđ"]
                # fmt: off
                if interiorStr == "k" or any(interiorStr.startswith(s) for s in noStartStrs):
                    interior = False
                else:
                    interior = True
                # fmt: on

            # match = re.match(
            #     r"([0-9]*[.,]?[0-9]+)\s*m?\s*[*x]\s*([0-9]*[.,]?[0-9]+)", description,
            # )
            # if match:
            #     width, length = match.group(1, 2)
            # else:
            #     pass

            nearCenter = district in ["Quận 1", "Quận 3", "Quận 4", "Bình Thạnh"]
            owner = any(
                searchStr in description
                for searchStr in ["sổ đỏ", "sổ hồng", "chính chủ", "pháp lý"]
            )

            alley = False
            if address is not None:
                alley = "/" in address

            if not alley:
                alley = "hẻm" in description

            villa = "biệt thự" in description

            new = any(
                searchStr in description
                for searchStr in ["nhà mới", "mới xây", "mới 100"]
            )

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
                xstr(interior),
                xstr(nearCenter),
                xstr(owner),
                xstr(alley),
                xstr(villa),
                xstr(new),
                xstr(price),
            )
            fOut.write(f"{tab.join(row)}\n")


# from: https://docs.python.org/3/library/itertools.html#itertools-recipes
def unique_everseen(iterable, key=None):
    "List unique elements, preserving order. Remember all elements ever seen."
    # unique_everseen('AAAABBBCCDAABBB') --> A B C D
    # unique_everseen('ABBCcAD', str.lower) --> A B C D
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in filterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element


def removeDuplicates(inputFile: str, outputFile: str):
    with open(inputFile) as fIn, open(outputFile, "w") as fOut:
        for line in unique_everseen(fIn):
            fOut.write(line)


dataFile = "data/2019-11-29_23_18_43.json"
noDuplicatedFile = "data/2019-11-29_23_18_43-no-dup.json"
outputFile = "data/2019-11-29_23_18_43.csv"

if not os.path.exists(noDuplicatedFile):
    removeDuplicates(inputFile=dataFile, outputFile=noDuplicatedFile)
preprocess(inputFile=noDuplicatedFile, outputFile=outputFile)
