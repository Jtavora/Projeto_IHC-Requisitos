from .CommonRouter import associationRouter, oauth_scheme
from fastapi import HTTPException
from App.Models.PydanticModels import *
from App.Controller import AssociationController
from fastapi import Depends

association_controller = AssociationController()

@associationRouter.post("/create_association")
def create_association(association: Association, token: str = Depends(oauth_scheme)):
    association = association_controller.create_association(association)
    if association:
        return association
    raise HTTPException(status_code=400, detail="Association already exists")