def read_csv_file(filepath) -> list:
    normalized = []

    with open(filepath, encoding="utf-8") as f:
        lines = f.readlines()

    # Обработка заголовков
    raw_headers = lines[0].split(",")
    headers = []
    for header in raw_headers:
        headers.append(header.strip())

    # Определение поля с зарплатой
    salary_field = None
    for field in ["hourly_rate", "rate", "salary"]:
        if field in headers:
            salary_field = field
            break

    if not salary_field:
        raise ValueError(f"Поля с зарплатой не найдено: {filepath}")

    # Обработка строк с данными
    for line in lines[1:]:
        values_raw = line.strip().split(",")
        values = []
        for value in values_raw:
            values.append(value.strip())

        record = dict(zip(headers, values))

        normalized.append({
            "name": record["name"],
            "department": record["department"],
            "hours_worked": int(record["hours_worked"]),
            "hourly_rate": int(record[salary_field])
        })
        
    return normalized
