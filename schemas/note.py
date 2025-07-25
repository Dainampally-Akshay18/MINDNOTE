def noteEntity(item)-> dict:
    return {
        "_id": str(item.get("_id", "")),
        "title": item.get("title", ""),
        "Description": item.get("Description", ""),
        "important": item.get("important", False)
    }
    
def notesEntity(item) -> list:
    return [noteEntity(item) for item in item]