from crud import CRUDCategory

CRUDCategory.add(name="Стеки", parent_id=1)
CRUDCategory.add(name="Ролы", parent_id=2)
for category in CRUDCategory.get_all():
    print(category.name)
    print(category.__dict__)