import pytest

from core.models import City, SearchResult

features = {
    "features": [
        {
            "type": "Feature",
            "properties": {
                "mag": 5,
                "place": "144 km WSW of Ternate, Indonesia",
                "time": 1622820282249,
                "updated": 1629840946040,
                "tz": None,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000e9r2",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000e9r2&format=geojson",
                "felt": None,
                "cdi": None,
                "mmi": None,
                "alert": None,
                "status": "reviewed",
                "tsunami": 0,
                "sig": 385,
                "net": "us",
                "code": "7000e9r2",
                "ids": ",us7000e9r2,",
                "sources": ",us,",
                "types": ",origin,phase-data,",
                "nst": None,
                "dmin": 1.274,
                "rms": 1.11,
                "gap": 45,
                "magType": "mb",
                "type": "earthquake",
                "title": "M 5.0 - 144 km WSW of Ternate, Indonesia"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [126.2436, 0.1655, 10]
            },
            "id": "us7000e9r2"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 5.3,
                "place": "Molucca Sea",
                "time": 1622814313276,
                "updated": 1629840947040,
                "tz": None,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000e9p4",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000e9p4&format=geojson",
                "felt": None,
                "cdi": None,
                "mmi": 3.161,
                "alert": "green",
                "status": "reviewed",
                "tsunami": 0,
                "sig": 432,
                "net": "us",
                "code": "7000e9p4",
                "ids": ",usauto7000e9p4,us7000e9p4,",
                "sources": ",usauto,us,",
                "types": ",internal-moment-tensor,losspager,moment-tensor,origin,phase-data,shakemap,",
                "nst": None,
                "dmin": 1.159,
                "rms": 1,
                "gap": 26,
                "magType": "mww",
                "type": "earthquake",
                "title": "M 5.3 - Molucca Sea"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [126.2897, 0.34, 8.6]
            },
            "id": "us7000e9p4"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 5.9,
                "place": "149 km W of Gold Beach, Oregon",
                "time": 1622794620663,
                "updated": 1633199594382,
                "tz": None,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000e9mr",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000e9mr&format=geojson",
                "felt": 18,
                "cdi": 3.8,
                "mmi": 3.741,
                "alert": "green",
                "status": "reviewed",
                "tsunami": 1,
                "sig": 542,
                "net": "us",
                "code": "7000e9mr",
                "ids": ",at00qu64cd,us7000e9mr,usauto7000e9mr,pt21155001,",
                "sources": ",at,us,usauto,pt,",
                "types": ",dyfi,general-text,ground-failure,impact-link,internal-moment-tensor,internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
                "nst": None,
                "dmin": 1.715,
                "rms": 0.92,
                "gap": 75,
                "magType": "mww",
                "type": "earthquake",
                "title": "M 5.9 - 149 km W of Gold Beach, Oregon"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [-126.218, 42.2405, 13.91]
            },
            "id": "us7000e9mr"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 5.9,
                "place": "153 km W of Gold Beach, Oregon",
                "time": 1622793163544,
                "updated": 1684628785213,
                "tz": None,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000e9mg",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000e9mg&format=geojson",
                "felt": 25,
                "cdi": 5.3,
                "mmi": 5.006,
                "alert": "green",
                "status": "reviewed",
                "tsunami": 1,
                "sig": 549,
                "net": "us",
                "code": "7000e9mg",
                "ids": ",at00qu637v,us7000e9mg,usauto7000e9mg,pt21155000,",
                "sources": ",at,us,usauto,pt,",
                "types": ",dyfi,general-text,ground-failure,impact-link,internal-moment-tensor,internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
                "nst": None,
                "dmin": 1.739,
                "rms": 0.84,
                "gap": 74,
                "magType": "mww",
                "type": "earthquake",
                "title": "M 5.9 - 153 km W of Gold Beach, Oregon"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [-126.2778, 42.2881, 16.57]
            },
            "id": "us7000e9mg"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 5.1,
                "place": "19 km S of Carora, Venezuela",
                "time": 1622740652180,
                "updated": 1628374060040,
                "tz": None,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000e9hi",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000e9hi&format=geojson",
                "felt": 2,
                "cdi": 5.3,
                "mmi": None,
                "alert": None,
                "status": "reviewed",
                "tsunami": 0,
                "sig": 401,
                "net": "us",
                "code": "7000e9hi",
                "ids": ",us7000e9hi,",
                "sources": ",us,",
                "types": ",dyfi,origin,phase-data,",
                "nst": None,
                "dmin": 1.232,
                "rms": 0.57,
                "gap": 26,
                "magType": "mb",
                "type": "earthquake",
                "title": "M 5.1 - 19 km S of Carora, Venezuela"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [-70.0634, 9.9933, 10]
            },
            "id": "us7000e9hi"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 5,
                "place": "central Mid-Atlantic Ridge",
                "time": 1622717756800,
                "updated": 1628374052040,
                "tz": None,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000e9cx",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000e9cx&format=geojson",
                "felt": None,
                "cdi": None,
                "mmi": None,
                "alert": None,
                "status": "reviewed",
                "tsunami": 0,
                "sig": 385,
                "net": "us",
                "code": "7000e9cx",
                "ids": ",us7000e9cx,",
                "sources": ",us,",
                "types": ",origin,phase-data,",
                "nst": None,
                "dmin": 10.549,
                "rms": 0.95,
                "gap": 30,
                "magType": "mb",
                "type": "earthquake",
                "title": "M 5.0 - central Mid-Atlantic Ridge"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [-31.5117, 3.8327, 10]
            },
            "id": "us7000e9cx"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 5.1,
                "place": "132 km WSW of Ternate, Indonesia",
                "time": 1622715810359,
                "updated": 1628374051040,
                "tz": None,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000e9cj",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000e9cj&format=geojson",
                "felt": None,
                "cdi": None,
                "mmi": None,
                "alert": None,
                "status": "reviewed",
                "tsunami": 0,
                "sig": 400,
                "net": "us",
                "code": "7000e9cj",
                "ids": ",us7000e9cj,",
                "sources": ",us,",
                "types": ",origin,phase-data,",
                "nst": None,
                "dmin": 1.162,
                "rms": 1.05,
                "gap": 34,
                "magType": "mb",
                "type": "earthquake",
                "title": "M 5.1 - 132 km WSW of Ternate, Indonesia"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [126.293, 0.3224, 35]
            },
            "id": "us7000e9cj"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 6.2,
                "place": "132 km WSW of Ternate, Indonesia",
                "time": 1622714998295,
                "updated": 1660022366929,
                "tz": None,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000e9bi",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000e9bi&format=geojson",
                "felt": 3,
                "cdi": 6.7,
                "mmi": 3.847,
                "alert": "green",
                "status": "reviewed",
                "tsunami": 0,
                "sig": 593,
                "net": "us",
                "code": "7000e9bi",
                "ids": ",us7000e9bi,usauto7000e9bi,pt21154051,at00qu4ewp,",
                "sources": ",us,usauto,pt,at,",
                "types": ",dyfi,ground-failure,internal-moment-tensor,internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
                "nst": None,
                "dmin": 1.166,
                "rms": 1.24,
                "gap": 30,
                "magType": "mww",
                "type": "earthquake",
                "title": "M 6.2 - 132 km WSW of Ternate, Indonesia"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [126.2911, 0.3165, 26]
            },
            "id": "us7000e9bi"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 5,
                "place": "Southern Qinghai, China",
                "time": 1622699718480,
                "updated": 1628374047040,
                "tz": None,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us7000e9a3",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us7000e9a3&format=geojson",
                "felt": 1,
                "cdi": 7.6,
                "mmi": 6.008,
                "alert": "green",
                "status": "reviewed",
                "tsunami": 0,
                "sig": 385,
                "net": "us",
                "code": "7000e9a3",
                "ids": ",us7000e9a3,",
                "sources": ",us,",
                "types": ",dyfi,losspager,origin,phase-data,shakemap,",
                "nst": None,
                "dmin": 10.448,
                "rms": 0.47,
                "gap": 28,
                "magType": "mww",
                "type": "earthquake",
                "title": "M 5.0 - Southern Qinghai, China"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [97.8048, 34.6927, 10]
            },
            "id": "us7000e9a3"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 5.4,
                "place": "82 km SW of Atocha, Bolivia",
                "time": 1622551326038,
                "updated": 1628374016040,
                "tz": None,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us6000egm7",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us6000egm7&format=geojson",
                "felt": 7,
                "cdi": 2,
                "mmi": 2.802,
                "alert": "green",
                "status": "reviewed",
                "tsunami": 0,
                "sig": 450,
                "net": "us",
                "code": "6000egm7",
                "ids": ",us6000egm7,usauto6000egm7,",
                "sources": ",us,usauto,",
                "types": ",dyfi,internal-moment-tensor,losspager,moment-tensor,origin,phase-data,shakemap,",
                "nst": None,
                "dmin": 1.961,
                "rms": 0.7,
                "gap": 30,
                "magType": "mww",
                "type": "earthquake",
                "title": "M 5.4 - 82 km SW of Atocha, Bolivia"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [-66.7637, -21.4857, 231.48]
            },
            "id": "us6000egm7"
        },
        {
            "type": "Feature",
            "properties": {
                "mag": 5.5,
                "place": "south of Panama",
                "time": 1622546456204,
                "updated": 1660022286783,
                "tz": None,
                "url": "https://earthquake.usgs.gov/earthquakes/eventpage/us6000eglq",
                "detail": "https://earthquake.usgs.gov/fdsnws/event/1/query?eventid=us6000eglq&format=geojson",
                "felt": 2,
                "cdi": 3.8,
                "mmi": 2.732,
                "alert": "green",
                "status": "reviewed",
                "tsunami": 0,
                "sig": 466,
                "net": "us",
                "code": "6000eglq",
                "ids": ",us6000eglq,usauto6000eglq,pt21152000,",
                "sources": ",us,usauto,pt,",
                "types": ",dyfi,internal-moment-tensor,internal-origin,losspager,moment-tensor,origin,phase-data,shakemap,",
                "nst": None,
                "dmin": 3.403,
                "rms": 0.46,
                "gap": 53,
                "magType": "mww",
                "type": "earthquake",
                "title": "M 5.5 - south of Panama"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [-82.677, 5.046, 10]
            },
            "id": "us6000eglq"
        }
    ]
}

city_data = {
    "id": 1,
    "name": "Los Angeles",
    "state": "CA",
    "country": "USA",
    "lat": 34.0522,
    "long": -118.2437,
}

@pytest.fixture
def city():
    return City.objects.create(**city_data)

@pytest.fixture
def searched_result(city):
    return SearchResult.objects.create(
        city=city,
        start_date="2021-06-01",
        end_date="2021-06-05",
        title="M 5.9 - 149 km W of Gold Beach, Oregon",
        earthquake_date="2021-06-04"
    )