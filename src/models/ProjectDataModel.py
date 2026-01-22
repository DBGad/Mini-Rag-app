from .BaseDataModel import BaseDataModel
from .db_schemes.project import Project
from .enums.DataBaseEnum import DataBaseEnum

class ProjectDataModel(BaseDataModel):
    def __init__(self, db_client):
        super().__init__(db_client)
        self.collection = self.db_client[DataBaseEnum.COLLECTION_PROJECT_NAME.value]

    
    async def create_project(self,project:Project):
        res = await self.collection.insert_one(
            project.dict(exclude_none=True, by_alias=True, exclude={'id'})  # ✅ استبعاد id
        )
        project._id = res.inserted_id
        return project
    

    async def  get_project_or_create_one(self,project_id:str ):
       record  = await self.collection.find_one({
           "project_id" : project_id
       })

       if record is None :
           project = Project(project_id=project_id)
           project = await self.create_project(project)

           return project
            
       return Project(**record)   
    
    async def get_all_projects(self,page:int= 1 , page_size:int=10):
        total_docs = await self.collection.count_documents({})

        total_pages = total_docs // page_size
        if total_pages % page_size > 0 :
            total_pages = total_pages +1 

        cursor = self.collection.find().skip((page-1) * page_size).limit(page_size)
        projects = []
        async for doc in cursor:
            projects.append(
                Project(**doc)
            )
        return projects,total_pages