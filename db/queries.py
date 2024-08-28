class Queries:
    CREATE_SURVEY_TABLE = """
        CREATE TABLE IF NOT EXISTS survey (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            occupation TEXT
        )
    """

    INSERT_SURVEY_DATA = """
        INSERT INTO survey (name, age, gender, occupation)
        VALUES (?, ?, ?, ?)
    """

    SELECT_ALL_SURVEYS = """
        SELECT * FROM survey
    """

    SELECT_SURVEY_BY_ID = """
        SELECT * FROM survey WHERE id = ?
    """

    UPDATE_SURVEY_BY_ID = """
        UPDATE survey
        SET name = ?, age = ?, gender = ?, occupation = ?
        WHERE id = ?
    """

    DELETE_SURVEY_BY_ID = """
        DELETE FROM survey WHERE id = ?
    """

