
if __name__ == '__main__':
    location = "Parsippany, NJ"
    start_hr = datetime.time(12, 0)
    end_hr = datetime.time(6, 0)
    activity_description = "hike, study"
    clothes = "shorts, hoodie, tshirt"
    start_hr = datetime.time(0, 0)
    end_hr = datetime.time(12, 0)
    wd = asyncio.run(getweather(location, start_hr, end_hr))
    result = llm_text(wd, location, start_hr, end_hr, activity_description, clothes)
    print(result)