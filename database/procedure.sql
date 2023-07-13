DELIMITER //

CREATE PROCEDURE InserirEstudante(
  IN p_nome VARCHAR(100),
  IN p_email VARCHAR(100),
  IN p_matricula VARCHAR(20),
  IN p_curso VARCHAR(100),
  IN p_senha VARCHAR(100),
  IN p_administrador BOOLEAN,
  IN p_foto_perfil BLOB
)
BEGIN
  INSERT INTO Estudantes (nome, email, matricula, curso, senha, administrador, foto_perfil)
  VALUES (p_nome, p_email, p_matricula, p_curso, p_senha, p_administrador, p_foto_perfil);
END //

DELIMITER ;
