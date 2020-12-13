Drop Database Sicco;

Create Database Sicco;

Use Sicco;

Create Table persona(
	CI varchar(10) Primary Key,
    Unique Index CI_UNIQUE (CI ASC),
    Nombre char(30) Not Null,
    Apellido varchar(30) Not Null,
    Sexo char(1) Not Null,
    Edad int Not Null
);

Create Table Telefono(
	Cod_Tlf int(10) auto_increment Primary Key,
	Cod_Area1 int(4) unsigned Not Null,
    Cod_Area2 int(4) unsigned,
	Num1 int(7) unsigned zerofill Not Null,
    Num2 int(7) unsigned zerofill,
    CI varchar(10) Not Null Unique,
    Constraint CI_T
		Foreign Key (CI)
        References sicco.persona(CI)
        On Delete Cascade
        On Update Cascade
);
Create Table paciente(
	Cod_Paciente int(10) auto_increment Primary Key,
    CI varchar(10) Not Null Unique,
    Constraint CI_P
		Foreign Key (CI)
        References sicco.persona(CI)
        On Delete Cascade
        On Update Cascade
);

Create Table Usuario(
	IDUsuario varchar(50) Primary Key Unique,
    Contraseña varchar(50) Not Null,
	Tipo_Usuario varchar(22) Not Null,
    Pregunta1 varchar(90) Not Null,
    Pregunta2 varchar(90) Not Null,
    Respuesta1 varchar(90) Not Null,
    Respuesta2 varchar(90) Not Null,
    CI varchar(10) Not Null Unique,
    Constraint CI_Usuario
		Foreign Key (CI)
        References sicco.persona (CI)
        On Delete Cascade
        On Update Cascade
);

Create Table Fecha(
	Cod_Fecha int(10) Primary Key auto_increment Unique,
    Fecha_F Date Not Null
);       

Create Table Citas(
	Cod_Cita int(10) Primary Key Auto_increment Unique,
    Hora time Not Null,
    Precio float Not Null,
    Asistencia char(10),
    Cod_Paciente int(10),
    Cod_Fecha int(10),
    Constraint Cod_Fecha_C
		Foreign Key (Cod_Fecha)
        References sicco.fecha (Cod_Fecha)
        On Delete Cascade
        On Update Cascade,
	Constraint Cod_Paciente_C
		Foreign Key (Cod_Paciente)
        References sicco.Paciente(Cod_Paciente)
        On Delete Cascade
        On Update Cascade
);
Create Table Citas_Asistidas(
	Cod_CitaA int(10) Primary Key Auto_increment Unique,
    Hora time Not Null,
    Precio float Not Null,
    Asistencia char(10) Not Null,
    Cod_Paciente int(10) Not Null,
    Cod_Fecha int(10) Not Null,
    Cod_Cita int(10) Not Null,
    IDUsuario varchar(50), 
    Fecha_Modif date
);
Create Table Citas_Canceladas(
	Cod_CitaC int(10) Primary Key Auto_increment Unique,
    Hora time Not Null,
    Precio float Not Null,
    Asistencia char(10) Not Null,
    Cod_Paciente int(10) Not Null,
    Cod_Fecha int(10) Not Null,
    Cod_Cita int(10) Not Null,
    IDUsuario varchar(50),
    Fecha_Modif date
);
Create Table Citas_Ausentes(
	Cod_CitaAu int(10) Primary Key Auto_increment Unique,
    Hora time Not Null,
    Precio float Not Null,
    Asistencia char(10) Not Null,
    Cod_Paciente int(10) Not Null,
    Cod_Fecha int(10) Not Null,
    Cod_Cita int(10) Not Null,
    IDUsuario varchar(50),
    Fecha_Modif date
);



Create Table Servicio(
	Cod_Servicio int(10) Primary Key auto_increment Unique,
    Cod_Cita int(10) Not Null,
    Precio float Not Null,
    Tipo1 varchar(20) Not Null,
    Tipo2 varchar(20),
    Tipo3 varchar(20),
    Constraint Cod_Cita_S
		Foreign Key (Cod_Cita)
        References sicco.citas(Cod_Cita)
        On Delete Cascade
        On Update Cascade
);


Create Table Diagnostico(
	Cod_Diagnostico int(10) Primary Key auto_increment Unique,
    Descripcion longtext Not Null,
    Cod_Paciente int(10) Not Null Unique,
    Constraint Cod_Paciente_D
		Foreign Key (Cod_Paciente)
        References sicco.paciente(Cod_Paciente)
        On Delete Cascade
        On Update Cascade
);

Create Table Expediente(
	Cod_Expediente int (10) Primary Key auto_increment Unique,
    Antecedentes_Clinicos longtext,
    Enfermedades varchar(50),
    Alergias varchar(50),
	Cod_Paciente int(10) Not Null Unique,
    Cod_Diagnostico int(10) Not Null Unique,
    Constraint Cod_Paciente_E
		Foreign Key (Cod_Paciente)
        References sicco.paciente(Cod_Paciente)
        On Delete Cascade
        On Update Cascade,
    Constraint Cod_Diagnostico_E
		Foreign Key (Cod_Diagnostico)
        References sicco.diagnostico(Cod_Diagnostico)
        On Delete Cascade        
        On Update Cascade
);

Create Table Tratamiento(
	Cod_Tratamiento int(10) Primary Key auto_increment Unique,
    Descripcion longtext Not Null,
    Frecuencia varchar(20) Not Null,
    Tiempo_Necesario varchar(20) Not Null,
    Num_Serv_Necesario int Not Null,
    Cod_Diagnostico int(10) Not Null Unique,
    	Constraint Cod_Diagnostico_T
		Foreign Key (Cod_Diagnostico)
        References sicco.diagnostico (Cod_Diagnostico)
        On Delete Cascade
        On Update Cascade
);

Create Table Moroso(
	Cod_Moroso int(10) Primary Key auto_increment Unique,
    Saldo_Deudor float,
    Fecha_Limite date,
    Fecha_Ultimo_Pago date,
    Cod_Paciente int(10) Not Null Unique,
    Cod_Fecha int (10),
    Constraint Cod_Paciente_M
		Foreign Key (Cod_Paciente)
        References sicco.paciente(Cod_Paciente)
        On Delete Cascade
        On Update Cascade,
	Constraint Cod_Fecha_M
		Foreign Key (Cod_Fecha)
		References sicco.fecha(Cod_Fecha)
		On Delete Cascade
		On Update Cascade
);

Create Table Pago(
	Cod_Pago int(10) Primary Key auto_increment Unique,
    Monto float Not Null,
    Inicial float,
    Cuota1 float,
    Cuota2 float,
    Tipo_Pago varchar(15) Not Null,
    Metodo_Pago varchar(10) Not Null,
    Num_Ref int(10),
    Cod_Fecha int(10),
    Cod_Paciente int(10),
    Cod_Moroso int(10),
    Constraint Cod_Fecha_P
		Foreign Key (Cod_Fecha)
        References sicco.Fecha(Cod_Fecha)
        On Delete Cascade
        On Update Cascade,
    Constraint Cod_Paciente_P
		Foreign Key (Cod_Paciente)
        References sicco.Paciente(Cod_Paciente)
        On Delete Cascade
        On Update Cascade,
	Constraint Cod_Moroso_P
		Foreign Key (Cod_Moroso)
        References sicco.moroso(Cod_Moroso)
        On Delete Cascade
        On Update Cascade
);

Create Table Recibo(
	Cod_Recibo int(10) Primary Key auto_increment Unique,
    Num_Pago int,
    Cod_Paciente int(10),
    Cod_Pago int(10) Unique,
    Constraint Cod_Paciente_R
		Foreign Key (Cod_Paciente)
        References sicco.Paciente (Cod_Paciente)
        On Delete Cascade
        On Update Cascade,
	Constraint Cod_Pago_R
		Foreign Key (Cod_Pago)
        References sicco.pago(Cod_Pago)
        On Delete Cascade
        On Update Cascade
);
       
Create Table Paciente_Solicita_Servicio(
	Cod_Paciente int(10),
    Cod_Servicio int(10),
    Primary Key (Cod_Paciente , Cod_Servicio),
    Constraint Cod_Paciente_PSS
		Foreign Key (Cod_Paciente)
        References sicco.Paciente(Cod_Paciente)
        On Delete Cascade
        On Update Cascade,
	Constraint Cod_Servicio_PSS
		Foreign Key (Cod_Servicio)
        References sicco.servicio(Cod_Servicio)
        On Delete Cascade
        On Update Cascade
);

Create Table Servicio_Tiene_Pago(
    Cod_Servicio int(10),
    Cod_Pago int(10),
    Primary Key (Cod_Servicio , Cod_Pago),
	Constraint Cod_Servicio_STP
		Foreign Key (Cod_Servicio)
        References sicco.servicio(Cod_Servicio)
        On Delete Cascade
        On Update Cascade,
	Constraint Cod_Pago_STP
		Foreign Key (Cod_Pago)
        References sicco.pago(Cod_Pago)
        On Delete Cascade
        On Update Cascade
);

Create Table Servicio_Tiene_Tratamiento(
    Cod_Servicio int(10),
    Cod_Tratamiento int(10),
    Primary Key (Cod_Servicio , Cod_Tratamiento),
	Constraint Cod_Servicio_STT
		Foreign Key (Cod_Servicio)
        References sicco.servicio(Cod_Servicio)
        On Delete Cascade
        On Update Cascade,
	Constraint Cod_Tratamiento_STT
		Foreign Key (Cod_Tratamiento)
        References sicco.tratamiento(Cod_Tratamiento)
        On Delete Cascade
        On Update Cascade
);

Create Table Cita_Tiene_Pago(
    Cod_Cita int(10),
    Cod_Pago int(10),
    Primary Key (Cod_Cita , Cod_Pago),
	Constraint Cod_Cita_CTP
		Foreign Key (Cod_Cita)
        References sicco.Citas(Cod_Cita)
        On Delete Cascade
        On Update Cascade,
	Constraint Cod_Pago_CTP
		Foreign Key (Cod_Pago)
        References sicco.pago(Cod_Pago)
        On Delete Cascade
        On Update Cascade
);

DELIMITER $$;

CREATE TRIGGER Citas_Asistencia_BU BEFORE UPDATE ON citas FOR EACH ROW

	BEGIN 
		IF(NEW.Asistencia='Asistida') THEN
        
			INSERT INTO citas_asistidas (Hora, Precio, Asistencia, Cod_Paciente, Cod_Fecha, Cod_Cita, IDUsuario, Fecha_Modif)
            VALUES (NEW.Hora, NEW.Precio, NEW.Asistencia, NEW.Cod_Paciente, NEW.Cod_Fecha, NEW.Cod_Cita, current_user(), now());
            
		ELSEIF(NEW.Asistencia='Cancelada') THEN
			
            INSERT INTO citas_canceladas (Hora, Precio, Asistencia, Cod_Paciente, Cod_Fecha, Cod_Cita, IDUsuario, Fecha_Modif)
            VALUES (NEW.Hora, NEW.Precio, NEW.Asistencia, NEW.Cod_Paciente, NEW.Cod_Fecha, NEW.Cod_Cita, current_user(), now());
		
        ELSEIF(NEW.Asistencia='Ausentes') THEN
			
            INSERT INTO citas_ausentes (Hora, Precio, Asistencia, Cod_Paciente, Cod_Fecha, Cod_Cita, IDUsuario, Fecha_Modif)
            VALUES (NEW.Hora, NEW.Precio, NEW.Asistencia, NEW.Cod_Paciente, NEW.Cod_Fecha, NEW.Cod_Cita, current_user(), now());
            
		END IF;
	
    END;$$

DELIMITER ;