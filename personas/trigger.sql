create or replace TRIGGER TRIGGER_PERSONAS_AUDITORIA 

BEFORE INSERT OR UPDATE ON PERSONAS_NOTA
for each row

DECLARE
V_INSERT VARCHAR2(100) := 'INSERT-ALUMNO-'||:NEW.alumno_ID;
V_UPDATE VARCHAR2(100) := 'UPDATE-ALUMNO-'||:NEW.alumno_ID;
V_DELETE VARCHAR2(100) := 'BORRADO-ALUMNO-'||:NEW.alumno_ID;
V_user varchar2(30) := user;  --Definir usuario de donde se toma porque el user del sistema es alfanumerico

BEGIN

        if inserting then    
            insert into personas_auditoria  (id,accion,campo,valor_old,valor_new,usuario,fecha)
                values(ISEQ$$_74216.nextval, V_INSERT,'nota1', 0, :new.n1, v_user,sysdate) ;
            insert into personas_auditoria  (id,accion,campo,valor_old,valor_new,usuario,fecha)
                values(ISEQ$$_74216.nextval, V_INSERT,'nota2',0, :new.n2,   v_user,sysdate) ;
            insert into personas_auditoria  (id,accion,campo,valor_old,valor_new,usuario,fecha)
                values(ISEQ$$_74216.nextval, V_INSERT,'nota3',0, :new.n3,  v_user,sysdate) ;
            insert into personas_auditoria  (id,accion,campo,valor_old,valor_new,usuario,fecha)
                values(ISEQ$$_74216.nextval, V_INSERT,'alumno',0, :new.alumno_id, v_user,sysdate) ;
            insert into personas_auditoria  (id,accion,campo,valor_old,valor_new,usuario,fecha)
                values(ISEQ$$_74216.nextval, V_INSERT,'año', 0,:new.ano, v_user,sysdate) ;
            insert into personas_auditoria  (id,accion,campo,valor_old,valor_new,usuario,fecha)
                values(ISEQ$$_74216.nextval, V_INSERT,'asignatura', 0,:new.asignatura_id,  v_user,sysdate) ;
        end if;

         if updating then
            if :old.n1 <> :new.n1 Then
              insert into  personas_auditoria  (id,accion,campo,valor_old,valor_new,usuario,fecha)
                values(ISEQ$$_74216.nextval,V_UPDATE,'n1', :old.n1,:new.n1,   v_user,sysdate) ;
            end if;  
            if :old.n2 <> :new.n2 Then
              insert into  personas_auditoria  (id,accion,campo,valor_old,valor_new,usuario,fecha)
                values(ISEQ$$_74216.nextval, V_UPDATE,'n2', :old.n2,:new.n2,    v_user,sysdate) ;
            end if;  
            if :old.n3 <> :new.n3 Then
              insert into  personas_auditoria  (id,accion,campo,valor_old,valor_new,usuario,fecha)
                values(ISEQ$$_74216.nextval, V_UPDATE,'n3', :old.n3,:new.n3,  v_user,sysdate) ;
            end if; 
            if :old.activo <> :new.activo Then
              insert into  personas_auditoria  (id,accion,campo,valor_old,valor_new,usuario,fecha)
                values(ISEQ$$_74216.nextval, V_DELETE ,'estado', :old.activo,:new.activo,  v_user,sysdate) ;
            end if; 
            if :old.asignatura_id <> :new.asignatura_id Then
              insert into  personas_auditoria  (id,accion,campo,valor_old,valor_new,usuario,fecha)
                values(ISEQ$$_74216.nextval,V_UPDATE,'asignatura_id', :old.ASIGNATURA_id,:new.asignatura_id,  v_user,sysdate) ;
            end if;
         end if;
         
END;
