CREATE VIEW DetalhesAvaliacoes AS
SELECT a.id AS avaliacao_id, e.nome AS estudante_nome, t.id AS turma_id, t.disciplina_id, t.periodo, a.avaliacao
FROM Avaliacoes a
JOIN Estudantes e ON a.estudante_id = e.id
JOIN Turmas t ON a.turma_id = t.id;
