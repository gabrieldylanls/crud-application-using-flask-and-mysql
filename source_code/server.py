from flask import Flask, flash, render_template, redirect, url_for, request, session
from module.database import EstudanteDAO, AvaliacaoDAO, DenunciaDAO


app = Flask(__name__)   
app.secret_key = "mys3cr3tk3y"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        est_dao = EstudanteDAO()
        email = request.form['email']
        senha = request.form['senha']

        estudante = [e for e in est_dao.read() if e[2] == email and e[5] == senha][0]

        if estudante:
            session['user'] = str(estudante[2])
            session['user_id'] = str(estudante[0])
            session['administrador'] = str(estudante[6])
            return redirect('/estudantes')
        else:
            return render_template('login.html', error='Usuário ou senha inválidos')

    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        est_dao = EstudanteDAO()

        res = est_dao.insert({
            'nome': request.form['nome'],
            'email': request.form['email'],
            'matricula': request.form['matricula'],
            'curso': request.form['curso'],
            'senha': request.form['senha'],
            'administrador': request.form.get('administrador') == 'on',
            'foto_perfil': request.files['foto_perfil'].read()
        })

        if res:
            return redirect('/login')
        else:
            return redirect('/')


    return render_template('cadastro.html')

@app.route('/perfil/<id>', methods=['GET','POST'])
def perfil(id=1):
    estudante = EstudanteDAO().read_by_id(id)
    
    if request.method == 'POST':
        res = EstudanteDAO().update(id, {
            'nome': request.form['nome'],
            'email': request.form['email'],
            'matricula': request.form['matricula'],
            'curso': request.form['curso'],
            'senha': estudante[0][5],
            'administrador': request.form.get('administrador') == 'on',
            'foto_perfil': request.files['foto_perfil'].read() if request.files['foto_perfil'].filename != '' else estudante[0][7]
        })



        if res:
            return redirect('/estudantes')
        else:
            return redirect('/login')

    return render_template('perfil.html', data=estudante)

@app.route('/estudantes')
def estudantes():
    data = EstudanteDAO().read()
    return render_template('estudantes.html', data=data)

@app.route('/estudantes/deletar/<id>', methods=['GET', 'POST'])
def deleta_estudante(id):
    if request.method == 'POST':
        if session.get('administrador') == '1':
            res = EstudanteDAO().delete(id)
            if res:
                return redirect('/estudantes')
            else:
                return redirect('/login')
        else:
            return redirect('/login')
        
    return render_template('deleta_estudante.html', id=id)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

@app.route('/avaliacoes')
def avaliacoes():
    data = AvaliacaoDAO().read()
    return render_template('avaliacoes.html', data=data)

@app.route('/avaliacoes/cadastrar', methods=['GET', 'POST'])
def cadastra_avaliacao():
    user_id = session.get('user_id')
    if user_id:
        estudante = EstudanteDAO().read_by_id(user_id)[0]
    else:
        redirect('/login')

    if request.method == 'POST':
        res = AvaliacaoDAO().insert({
            'estudante_id': user_id,
            'turma_id': request.form['turma_id'],
            'avaliacao': request.form['avaliacao'],
        })

        if res:
            return redirect('/avaliacoes')
        else:
            return redirect('/login')


    return render_template('cadastra_avaliacao.html', estudante=estudante)

@app.route('/avaliacoes/atualizar/<id>', methods=['GET', 'POST'])
def atualiza_avaliacao(id):
    avaliacao = AvaliacaoDAO().read_by_id(id)

    if request.method == 'POST':
        res = AvaliacaoDAO().update(id, {
            'estudante_id': session.get('user_id'),
            'turma_id': request.form['turma_id'],
            'avaliacao': request.form['avaliacao'],
        })

        if res:
            return redirect('/avaliacoes')
        else:
            return redirect('/login')

    return render_template('atualiza_avaliacao.html', data=avaliacao)

@app.route('/avaliacoes/deletar/<id>', methods=['GET', 'POST'])
def deleta_avaliacao(id):
    if request.method == 'POST':
        if session.get('administrador') == '1':
            res = AvaliacaoDAO().delete(id)
            if res:
                return redirect('/avaliacoes')
            else:
                return redirect('/login')
        else:
            return redirect('/login')
        
    return render_template('deleta_avaliacao.html', id=id)    

@app.route('/denuncias')
def denuncias():
    data = DenunciaDAO().read()
    return render_template('denuncias.html', data=data)

@app.route('/denuncias/cadastrar/<avaliacao_id>', methods=['GET', 'POST'])
def cadastra_denuncia(avaliacao_id):
    avaliacao = AvaliacaoDAO().read_by_id(avaliacao_id)[0]

    user_id = session.get('user_id')
    if user_id:
        estudante = EstudanteDAO().read_by_id(user_id)[0]
    else:
        redirect('/login')

    if request.method == 'POST':
        res = DenunciaDAO().insert({
            'estudante_id': user_id,
            'avaliacao_id': avaliacao_id,
            'denuncia': request.form['denuncia'],
        })

        if res:
            return redirect('/denuncias')
        else:
            return redirect('/login')


    return render_template('cadastra_denuncia.html', estudante=estudante, avaliacao=avaliacao)

@app.route('/denuncias/atualizar/<id>', methods=['GET', 'POST'])
def atualiza_denuncia(id):
    denuncia = DenunciaDAO().read_by_id(id)

    if request.method == 'POST':
        res = DenunciaDAO().update(id, {
            'estudante_id': session.get('user_id'),
            'avaliacao_id': request.form['avaliacao_id'],
            'denuncia': request.form['denuncia'],
        })

        if res:
            return redirect('/denuncias')
        else:
            return redirect('/login')

    return render_template('atualiza_denuncia.html', data=denuncia)

@app.route('/denuncias/deletar/<id>', methods=['GET', 'POST'])
def deleta_denuncia(id):
    if request.method == 'POST':
        if session.get('administrador') == '1':
            res = DenunciaDAO().delete(id)
            if res:
                return redirect('/denuncias')
            else:
                return redirect('/login')
        else:
            return redirect('/login')
        
    return render_template('deleta_denuncia.html', id=id)    

if __name__ == '__main__':
    app.run(debug=True, port=8181, host="0.0.0.0")        

"""
@app.route('/')
def index():
    data = db.read(None)

    return render_template('index.html', data = data)

@app.route('/add/')
def add():
    return render_template('add.html')

@app.route('/addphone', methods = ['POST', 'GET'])
def addphone():
    if request.method == 'POST' and request.form['save']:
        if db.insert(request.form):
            flash("A new phone number has been added")
        else:
            flash("A new phone number can not be added")

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/update/<int:id>/')
def update(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['update'] = id
        return render_template('update.html', data = data)

@app.route('/updatephone', methods = ['POST'])
def updatephone():
    if request.method == 'POST' and request.form['update']:

        if db.update(session['update'], request.form):
            flash('A phone number has been updated')

        else:
            flash('A phone number can not be updated')

        session.pop('update', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/delete/<int:id>/')
def delete(id):
    data = db.read(id);

    if len(data) == 0:
        return redirect(url_for('index'))
    else:
        session['delete'] = id
        return render_template('delete.html', data = data)

@app.route('/deletephone', methods = ['POST'])
def deletephone():
    if request.method == 'POST' and request.form['delete']:

        if db.delete(session['delete']):
            flash('A phone number has been deleted')

        else:
            flash('A phone number can not be deleted')

        session.pop('delete', None)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(port=8181, host="0.0.0.0")
"""