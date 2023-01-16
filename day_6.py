def sort_csv_columns(csv_data):
    """Sort the columns of a CSV file alphabetically."""
    rows_csv = csv_data.strip().split("\n")
    clm_names = rows_csv[0].split(",")
    sorted_column_indices = sorted(range(len(clm_names)), key=lambda i: column_names[i].lower())
    sorted_rows_csv = []
    for row in rows_csv:
        columns = row.split(",")
        sorted_columns = [columns[i] for i in sorted_column_indices]
        sorted_rows_csv.append(",".join(sorted_columns))
    return "\n".join(sorted_rows)