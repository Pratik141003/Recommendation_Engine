from db_config import get_db_connection
from psycopg2.extras import RealDictCursor

# ------------------------------
# CONNECT USING CONFIG FILE
# ------------------------------

conn = get_db_connection()
cursor = conn.cursor(cursor_factory=RealDictCursor)

# ------------------------------
# POSITIVE AI MESSAGE GENERATOR
# ------------------------------

def generate_positive_message(category_name, resource_title):
    return (
        f"Participating in '{resource_title}' will help you further strengthen your expertise in {category_name}. "
        "This opportunity supports continuous professional growth and enhances your overall academic contribution."
    )

# ------------------------------
# HEADER
# ------------------------------

print("\n" + "="*70)
print("        PBAS PROFESSIONAL GROWTH RECOMMENDATION REPORT")
print("="*70 + "\n")

# ------------------------------
# FETCH ALL TEACHERS
# ------------------------------

cursor.execute("SELECT * FROM teachers ORDER BY teacher_id")
teachers = cursor.fetchall()

for teacher in teachers:
    teacher_id = teacher["teacher_id"]
    teacher_name = teacher["name"]
    department = teacher["department"]
    designation = teacher["designation"]

    cursor.execute("""
        SELECT 
            c.category_id,
            c.category_name,
            t.minimum_required,
            COALESCE(a.achieved_count, 0) AS achieved_count
        FROM teacher_targets t
        JOIN pbas_categories c ON t.category_id = c.category_id
        LEFT JOIN teacher_achievements a 
            ON a.teacher_id = t.teacher_id 
            AND a.category_id = t.category_id
        WHERE t.teacher_id = %s
    """, (teacher_id,))

    categories = cursor.fetchall()
    teacher_has_recommendation = False

    print("----------------------------------------------------------------------")
    print(f"Teacher      : {teacher_name}")
    print(f"Department   : {department}")
    print(f"Designation  : {designation}")
    print("----------------------------------------------------------------------")

    for cat in categories:
        minimum = cat["minimum_required"]
        achieved = cat["achieved_count"]

        if achieved < minimum:
            teacher_has_recommendation = True

            cursor.execute("""
                SELECT *
                FROM resource_library
                WHERE category_id = %s
                ORDER BY RANDOM()
                LIMIT 1
            """, (cat["category_id"],))

            resource = cursor.fetchone()

            if resource:
                message = generate_positive_message(
                    cat["category_name"],
                    resource["title"]
                )

                print(f"\n📌 Category   : {cat['category_name']}")
                print(f"🎓 Type       : {resource['resource_type']}")
                print(f"📚 Title      : {resource['title']}")
                print(f"🏢 Platform   : {resource['platform']}")
                print(f"⏳ Duration   : {resource['duration']}")
                print(f"🔗 URL        : {resource['resource_url']}")
                print("\n💡 Suggestion :")
                print(f"   {message}")

    if not teacher_has_recommendation:
        print("\n🌟 Outstanding performance across all PBAS categories.")
        print("Continue maintaining your excellent academic standards.")

    print("\n" + "="*70 + "\n")

cursor.close()
conn.close()
