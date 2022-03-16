-- Procedimiento para mostrar las notas activas
CREATE OR REPLACE PROCEDURE sp_listar_notas(notas out SYS_REFCURSOR)
IS
BEGIN
    OPEN notas FOR SELECT N.id,A.id as alumno_id, (A.nombres||' '||A.apellidos)as nombre, asg.nombre as asignatura , N.n1, N.n2, N.n3,round(((N.n1 + N.n2)*0.3 + N.n3*0.4),1) as definitiva
    FROM personas_nota N INNER JOIN personas_alumno A ON A.id = N.alumno_id INNER JOIN personas_asignatura asg ON asg.id = n.asignatura_id 
    WHERE N.ACTIVO = '1';
END;

-- Procedimiento para mostrar los alumnos activados
CREATE OR REPLACE PROCEDURE sp_listar_alumnos(alumnos out SYS_REFCURSOR)
IS
BEGIN
    OPEN alumnos FOR SELECT * FROM personas_alumno WHERE activo = '1';
END;

-- Procedimiento para mostrar las asignaturas activadas
CREATE OR REPLACE PROCEDURE sp_listar_asignaturas(asignaturas OUT SYS_REFCURSOR)
IS
BEGIN
    OPEN asignaturas FOR SELECT * FROM personas_asignatura WHERE activo = '1';
END;

/* procedimiento al. para agregar notas del CRUD de notas
    salida = 1 --> se inserto la nota
    salida = 0 --> fallo el insert
*/

CREATE OR REPLACE PROCEDURE sp_agregar_notas(
    v_alumno_id NUMBER,
    v_asignatura_id NUMBER,
    v_n1 NUMBER,
    v_n2 NUMBER,
    v_n3 NUMBER,
    v_salida OUT NUMBER
 ) IS
 BEGIN
    INSERT INTO personas_nota(alumno_id,asignatura_id,n1, n2, n3,ACTIVO)
    VALUES (v_alumno_id, v_asignatura_id,v_n1, v_n2, v_n3,1);
    COMMIT;
    v_salida := 1;

EXCEPTION
    WHEN OTHERS THEN
        v_salida := 0;
END;

