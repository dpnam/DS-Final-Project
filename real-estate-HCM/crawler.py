import json
import logging
import os.path
import time
import traceback
from datetime import datetime
from pprint import pprint

from requests_html import HTMLSession

logger = logging.getLogger("crawler")
logFileName = f'{datetime.today().strftime("%Y-%m-%d_%H_%M_%S")}.log'
formatter = logging.Formatter("[%(asctime)s][%(name)s][%(levelname)s] - %(message)s")
fhandler = logging.FileHandler(filename=logFileName)
fhandler.setLevel(logging.DEBUG)
fhandler.setFormatter(formatter)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.handlers = []
logger.addHandler(fhandler)
logger.addHandler(ch)
logger.setLevel(logging.DEBUG)


def urlGenerator(baseUrl, startPage=1):
    i = startPage
    if i <= 1:
        yield baseUrl
        i = 2
    while True:
        yield f"{baseUrl}/p{i}"
        i += 1


def parseDetailPage(session: HTMLSession, url: str):
    global logger
    logger.info(f"Processing detail url: {url}")
    r = session.get(url)
    result = {}
    result["description"] = r.html.find(".pm-desc", first=True).text

    features = {}
    featuresTable = r.html.find(".table1", first=True)
    rows = featuresTable.find(".row")
    for row in rows:
        key = row.find(".left", first=True).text
        value = row.find(".right", first=True).text
        features[key] = value

    result["features"] = features

    return result


def parseSearchResultPage(
    fileName: str,
    session: HTMLSession,
    baseUrl: str = "https://batdongsan.com.vn/ban-nha-rieng-tp-hcm",
    startPage: int = 1,
):
    global logger
    if os.path.exists(fileName):
        logger.error(f"File exists {fileName}")
        return
    try:
        with open(fileName, "w", encoding="utf8") as f:
            for url in urlGenerator(baseUrl, startPage):
                logger.info(f"Processing url: {url}")
                r = session.get(url)
                notFound = r.html.find(
                    "#LeftMainContent__productSearchResult_pnlNotFound", first=True
                )
                if notFound is not None:
                    logger.info(f"{url} Not found")
                    break

                items = r.html.find(".search-productItem")
                for item in items:
                    result = {}
                    titleAnchor = item.find(".p-title a", first=True)
                    result["title"] = titleAnchor.text
                    result["detailUrl"] = titleAnchor.absolute_links.pop()
                    result["price"] = item.find(".product-price", first=True).text
                    result["area"] = item.find(".product-area", first=True).text
                    result["district"] = item.find(
                        ".product-city-dist", first=True
                    ).text
                    result["uptime"] = item.find(".uptime", first=True).text
                    result["detail"] = parseDetailPage(session, result["detailUrl"])
                    json.dump(result, f, ensure_ascii=False)
                    f.write("\n")

                time.sleep(2)
    except Exception as e:
        logger.error(f"{e}\n{traceback.format_exc}")


session = HTMLSession()
resultFileName = f'data/{datetime.today().strftime("%Y-%m-%d_%H_%M_%S")}.json'
parseSearchResultPage(resultFileName, session)
