from db_config import get_db_connection

def get_recommendations():
    conn = get_db_connection()
    cur = conn.cursor()

    query = """
    SELECT 
        t.name,
        c.category_name,
        g.percentage,
        crs.title,
        crs.platform,
        crs.expected_score_boost
    FROM teacher_gap_analysis g
    JOIN teachers t ON g.teacher_id = t.teacher_id
    JOIN pbas_categories c ON g.category_id = c.category_id
    JOIN courses crs ON crs.category_id = c.category_id
    WHERE g.gap_level = 'CRITICAL'
    ORDER BY t.name, crs.expected_score_boost DESC;
    """

    cur.execute(query)
    data = cur.fetchall()

    cur.close()
    conn.close()

    return data


if __name__ == "__main__":
    recommendations = get_recommendations()

    current_teacher = None

    for row in recommendations:
        teacher, category, score, course, platform, boost = row

        if teacher != current_teacher:
            print("\n===================================")
            print(f"Teacher: {teacher}")
            print(f"Weak Area: {category} ({score}%)")
            print("Recommended Courses:")
            current_teacher = teacher

        print(f"  - {course} ({platform}) | Expected Boost: +{boost}")
