from fastapi import Depends, FastAPI, HTTPException, Body, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
import models, schemas, hashing, tokin, oauth2
from database import get_db, engine



models.Base.metadata.create_all(bind=engine)

app = FastAPI()





# *********DIRECTOR*******

@app.get('/director', tags=["Director"])
def getIDirector(session: Session = Depends(get_db), current_user: schemas.UserSchema = Depends(oauth2.get_current_user)):
    director = session.query(models.DirectorModel).all()
    return director

@app.post("/director", tags=["Director"])
def CreateDirector(director: schemas.DirectorSchema, session: Session = Depends(get_db), current_user: schemas.UserSchema = Depends(oauth2.get_current_user)):
    director = models.DirectorModel(first_name=director.first_name, last_name=director.last_name, email=director.email, Active_time=director.Active_time, Create_time=director.Create_time)
    session.add(director)
    session.commit()
    session.refresh(director)

    return director

@app.put("/director/{id}", tags=["Director"])
def updateDirector(id: int, director: schemas.DirectorSchema, session: Session = Depends(get_db), current_user: schemas.UserSchema = Depends(oauth2.get_current_user)):
    directorObject = session.query(models.DirectorModel).get(id)
    directorObject.first_name = director.first_name
    directorObject.last_name = director.last_name
    directorObject.email = director.email
    directorObject.Active_time = director.Active_time
    directorObject.Create_time = director.Create_time
    session.commit()
    return director

@app.delete("/director/{id}", tags=["Director"])
def deleteDirector(id: int, session: Session = Depends(get_db), current_user: schemas.UserSchema = Depends(oauth2.get_current_user)):
    directorObject = session.query(models.DirectorModel).get(id)
    session.delete(directorObject)
    session.commit()
    session.close()
    return "Item was deleted..."


# ********* PRE_DIRECTOR ********

@app.get('/pre_director', tags=["Pre_Director"])
def getPre_Director(session: Session = Depends(get_db), current_user: schemas.UserSchema = Depends(oauth2.get_current_user)):
    pre_director = session.query(models.Pre_DirectorModel).all()
    return pre_director

@app.post("/pre_director", tags=["Pre_Director"])
def CreatePre_Director(pre_director: schemas.Pre_DirectorSchema, session: Session = Depends(get_db), current_user: schemas.UserSchema = Depends(oauth2.get_current_user)):
    pre_director = models.Pre_DirectorModel(first_name=pre_director.first_name, last_name=pre_director.last_name, email=pre_director.email, Active_time=pre_director.Active_time)
    session.add(pre_director)
    session.commit()
    session.refresh(pre_director)
    return pre_director

@app.put("/pre_director/{id}", tags=["Pre_Director"])
def updatePre_Director(id: int, pre_director: schemas.Pre_DirectorSchema, session: Session = Depends(get_db), current_user: schemas.UserSchema = Depends(oauth2.get_current_user)):
    pre_directorObject = session.query(models.Pre_DirectorModel).get(id)
    pre_directorObject.first_name = pre_director.first_name
    pre_directorObject.last_name = pre_director.last_name
    pre_directorObject.email = pre_director.email
    pre_directorObject.Active_time = pre_director.Active_time
    session.commit()
    return pre_director

@app.delete("/pre_director/{id}", tags=["Pre_Director"])
def deletePre_Director(id: int, session: Session = Depends(get_db), current_user: schemas.UserSchema = Depends(oauth2.get_current_user)):
    pre_directorObject = session.query(models.Pre_DirectorModel).get(id)
    session.delete(pre_directorObject)
    session.commit()
    session.close()
    return "Item was deleted..."


# ************* BOSS *************

@app.get("/boss", tags=["Boss"])
def getBoss(session: Session = Depends(get_db), current_user: schemas.UserSchema = Depends(oauth2.get_current_user)):
    boss = session.query(models.BossModel).all()
    return boss

@app.post("/boss", tags=["Boss"])
def CreateBoss(boss: schemas.BossSchema, session: Session = Depends(get_db), current_user: schemas.UserSchema = Depends(oauth2.get_current_user)):
    boss = models.BossModel(first_name=boss.first_name, last_name=boss.last_name, email=boss.email, Active_time=boss.Active_time, Create_time=boss.Create_time)
    session.add(boss)
    session.commit()
    session.refresh(boss)
    return boss

@app.put("/boss/{id}", tags=["Boss"])
def updateBoss(id: int, boss: schemas.BossSchema, session: Session = Depends(get_db), current_user: schemas.UserSchema = Depends(oauth2.get_current_user)):
    bossObject = session.query(models.BossModel).get(id)
    bossObject.first_name = boss.first_name
    bossObject.last_name = boss.last_name
    bossObject.email = boss.email
    bossObject.Active_time = boss.Active_time
    bossObject.Create_time = boss.Create_time
    session.commit()
    return boss

@app.delete("/boss/{id}", tags=["Boss"])
def deleteBoss(id: int, session: Session = Depends(get_db), current_user: schemas.UserSchema = Depends(oauth2.get_current_user)):
    bossObject = session.query(models.BossModel).get(id)
    session.delete(bossObject)
    session.commit()
    session.close()
    return "Item was deleted..."


# ************ WORKERS ************

@app.get("/worker", tags=["Worker"])
def getWorker(session: Session = Depends(get_db), current_user: schemas.UserSchema = Depends(oauth2.get_current_user)):
    worker = session.query(models.WorkersModel).all()
    return worker

@app.post("/worker", tags=["Worker"])
def CreateWorker(worker: schemas.WorkersSchema, session: Session = Depends(get_db), current_user: schemas.UserSchema = Depends(oauth2.get_current_user)):
    worker = models.BossModel(first_name=worker.first_name, last_name=worker.last_name, email=worker.email, Active_time=worker.Active_time, Create_time=worker.Create_time)
    session.add(worker)
    session.commit()
    session.refresh(worker)
    return worker

@app.put("/worker/{id}", tags=["Worker"])
def updateWorker(id: int, worker: schemas.WorkersSchema, session: Session = Depends(get_db), current_user: schemas.UserSchema = Depends(oauth2.get_current_user)):
    workerObject = session.query(models.WorkersModel).get(id)
    workerObject.first_name = worker.first_name
    workerObject.last_name = worker.last_name
    workerObject.email = worker.email
    workerObject.Active_time = worker.Active_time
    workerObject.Create_time = worker.Create_time
    session.commit()
    return worker

@app.delete("/worker/{id}", tags=["Worker"])
def deleteWorker(id: int, session: Session = Depends(get_db), current_user: schemas.UserSchema = Depends(oauth2.get_current_user)):
    workerObject = session.query(models.WorkersModel).get(id)
    session.delete(workerObject)
    session.commit()
    session.close()
    return "Item was deleted..."


# *************** WORK CRUD ******************

@app.get('/work', tags=["Work"])
def getWork(session: Session = Depends(get_db), current_user: schemas.UserSchema = Depends(oauth2.get_current_user)):
    work = session.query(models.WorksModel).all()
    return work

@app.post("/work", tags=["Work"])
def CreateWork(work: schemas.WorksSchema, session: Session = Depends(get_db), current_user: schemas.UserSchema = Depends(oauth2.get_current_user)):
    work = models.WorksModel(name=work.name, join_data=work.join_data, complete_data=work.complete_data, status=work.status, price=work.price, employer=work.employer, worker=work.worker)
    session.add(work)
    session.commit()
    session.refresh(work)
    return work

@app.put("/work/{id}", tags=["Work"])
def updateWork(id: int, work: schemas.WorksSchema, session: Session=Depends(get_db), current_user: schemas.UserSchema = Depends(oauth2.get_current_user)):
    workObject = session.query(models.WorksModel).get(id)
    workObject.name = work.name
    workObject.join_data = work.join_data
    workObject.complete_data = work.complete_data
    workObject.status = work.status
    workObject.price = work.price
    workObject.employer = work.employer
    workObject.worker = work.worker
    session.commit()
    return work

@app.delete("/work/{id}", tags=["Work"])
def deleteWork(id: int, session: Session=Depends(get_db), current_user: schemas.UserSchema = Depends(oauth2.get_current_user)):
    workObject = session.query(models.WorksModel).get(id)
    session.delete(workObject)
    session.commit()
    session.close()
    return "Item was deleted..."


# ***************** USER **************

@app.get("/user", tags=["User"])
def getUser(session: Session = Depends(get_db), current_user: schemas.UserSchema = Depends(oauth2.get_current_user)):
    user = session.query(models.UserModel).all()
    return user

@app.post("/user", tags=["User"])
def CreateUser(user: schemas.UserSchema, session: Session = Depends(get_db), current_user: schemas.UserSchema = Depends(oauth2.get_current_user)):
    user = models.UserModel(role=user.role, username=user.username, password=hashing.Hash.bcrypt(user.password))
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@app.put("/user/{id}", tags=["User"])
def updateUser(id: int, user: schemas.UserSchema, session: Session = Depends(get_db), current_user: schemas.UserSchema = Depends(oauth2.get_current_user)):
    userObject = session.query(models.UserModel).get(id)
    userObject.role = user.role
    userObject.username = user.username
    userObject.password = user.password
    session.commit()
    return user

@app.delete("/user/{id}", tags=["User"])
def deleteUser(id: int, session: Session = Depends(get_db), current_user: schemas.UserSchema = Depends(oauth2.get_current_user)):
    workObject = session.query(models.UserModel).get(id)
    session.delete(workObject)
    session.commit()
    session.close()
    return "Item was deleted..."


# ******************* AUTH *******************

@app.post('/login', tags=["Auth"])
def login(request: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_db)):
    user = session.query(models.UserModel).filter(models.UserModel.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
    if not hashing.Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Incorrect password")


    access_token = tokin.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}