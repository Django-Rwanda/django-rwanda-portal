
class ParentA: ...
class ParentB: ...


ParentClasses = (ParentA, ParentB)
child = type("Children", ParentClasses, {"new_method": lambda self: print("Dynamic method")})


