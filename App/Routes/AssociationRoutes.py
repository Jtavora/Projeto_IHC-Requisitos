from .CommonRouter import associationRouter
from fastapi import HTTPException
from App.Models.PydanticModels import *
from App.Controller import AssociationController

association_controller = AssociationController()

@associationRouter.post("/create_association")
def create_association(association: Association):
    association = association_controller.create_association(association)
    if association:
        return association
    raise HTTPException(status_code=400, detail="Association already exists")