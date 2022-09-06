#schemas helps to serialize and alsoconvert mongodb format json to out ui needed

def studentEntity (item) -> dict:
    return {
        "id": str(item["-id"]),
        "name": item["student_name"],
        "email": item["student_email"],
        "phone": item["student_phone"]
    }

def listOfStudentEntity(db_item_list) -> list:

    list_stu_entity=[]

    for item in db_item_list:
        list_stu_entity.append(studentEntity(item))
    return list_stu_entity
