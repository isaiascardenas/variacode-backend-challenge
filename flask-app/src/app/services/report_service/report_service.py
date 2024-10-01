def get_csv_string(data: list[dict], headers: list[str] = []) -> str:
    if not data:
        return ""

    csv_headers = ""
    csv_data = ""

    if not headers:
        csv_headers = "id,name\n"
    else:
        csv_headers = ",".join(headers) + "\n"

    for record in data:
        csv_data += (
            ",".join(["" if row is None else row for row in list(record.values())])
            + "\n"
        )

    return csv_headers + csv_data
