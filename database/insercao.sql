INSERT INTO Estudantes (nome, email, matricula, curso, senha, administrador, foto_perfil)
VALUES ('João Silva', 'joao@email.com', '20210001', 'Engenharia', '123456', 0, NULL);

INSERT INTO Estudantes (nome, email, matricula, curso, senha, administrador, foto_perfil)
VALUES ('Maria Santos', 'maria@email.com', '20190012', 'Medicina', 'abcdef', 0, NULL);

INSERT INTO Estudantes (nome, email, matricula, curso, senha, administrador, foto_perfil)
VALUES ('Pedro Oliveira', 'pedro@email.com', '20220005', 'Direito', 'xyz123', 1, NULL);

INSERT INTO Departamentos (id, nome)
VALUES (1, 'Ciência da Computação');

INSERT INTO Departamentos (id, nome)
VALUES (2, 'Administração');

INSERT INTO Departamentos (id, nome)
VALUES (3, 'Biologia');

INSERT INTO Professores (nome, departamento_id)
VALUES ('Carlos Rocha', 1);

INSERT INTO Professores (nome, departamento_id)
VALUES ('Ana Rodrigues', 2);

INSERT INTO Professores (nome, departamento_id)
VALUES ('Mariana Lima', 3);

INSERT INTO Disciplinas (id, nome, departamento_id)
VALUES ('COMP101', 'Introdução à Programação', 1);

INSERT INTO Disciplinas (id, nome, departamento_id)
VALUES ('ADM201', 'Gestão Empresarial', 2);

INSERT INTO Disciplinas (id, nome, departamento_id)
VALUES ('BIOL301', 'Genética Molecular', 3);

INSERT INTO Turmas (disciplina_id, professor_nome, departamento_id, total_vagas, vagas_ocupadas, horario, periodo, localizacao)
VALUES ('COMP101', 'Carlos Rocha', 1, 50, 30, 'Segunda-feira, 14:00-16:00', '2022/1', 'Sala A101');

INSERT INTO Turmas (disciplina_id, professor_nome, departamento_id, total_vagas, vagas_ocupadas, horario, periodo, localizacao)
VALUES ('ADM201', 'Ana Rodrigues', 2, 40, 20, 'Terça-feira, 09:00-11:00', '2022/1', 'Sala B201');

INSERT INTO Turmas (disciplina_id, professor_nome, departamento_id, total_vagas, vagas_ocupadas, horario, periodo, localizacao)
VALUES ('BIOL301', 'Mariana Lima', 3, 60, 45, 'Quarta-feira, 10:00-12:00', '2022/1', 'Sala C301');
