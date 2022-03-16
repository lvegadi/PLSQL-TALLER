CREATE OR REPLACE PROCEDURE sp_listar_notas(notas out SYS_REFCURSOR)
IS
BEGIN
    OPEN notas FOR SELECT N.id, (A.nombres||' '||A.apellidos)as nombre, asg.nombre as asignatura , N.n1, N.n2, N.n3,round(((N.n1 + N.n2)*0.3 + N.n3*0.4),1) as definitiva
    FROM personas_nota N INNER JOIN personas_alumno A ON A.id = N.alumno_id INNER JOIN personas_asignatura asg ON asg.id = n.asignatura_id 
    WHERE N.ACTIVO = '1';
END;

CREATE OR REPLACE PROCEDURE sp_listar_notas(notas out SYS_REFCURSOR)
IS
BEGIN
    OPEN notas FOR SELECT (A.nombres||' '||A.apellidos)as nombre, asg.nombre as asignatura , N.n1, N.n2, N.n3,round(((N.n1 + N.n2)*0.3 + N.n3*0.4),1) as definitiva
    FROM personas_nota N INNER JOIN personas_alumno A ON A.id = N.alumno_id INNER JOIN personas_asignatura asg ON asg.id = n.asignatura_id 
    WHERE N.ACTIVO = '1';
END;

CREATE OR REPLACE PROCEDURE sp_agregar_notas(
    v_alumno_id NUMBER,
    v_asignatura_id NUMBER,
    v_n1 NUMBER(2,1),
    v_n2 NUMBER(2,1),
    v_n3 NUMBER(2,1),
    v_salida,
 )

