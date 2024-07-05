from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file
from flask_bootstrap import Bootstrap
import requests
from io import BytesIO

app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.config['SESSION_TYPE'] = 'null'  # Armazenamento de sessão em memória
Bootstrap(app)

# Configuração do FastAPI URL
API_URL = 'http://api:8000/'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        response = requests.post(f'{API_URL}/login', data={'username': username, 'password': password})
        if response.status_code == 200:
            token = response.json()['access_token']
            session['token'] = token
            session['username'] = username
            session['role'] = response.json()['role']
            session['user_id'] = response.json()['id']
            
            if session['role'] == 'admin':
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('user_certificates'))
        else:
            flash('Login failed. Please check your credentials and try again.', 'error')
            session.clear()  # Limpa a sessão após falha de login
    return render_template('login.html')

@app.route('/user_certificates', methods=['GET'])
def user_certificates():
    token = session.get('token')
    if not token:
        flash('Session expired. Please login again.', 'error')
        return redirect(url_for('login'))
    
    user_id = session.get('user_id')
    response = requests.get(f'{API_URL}/users/get_certificates/{user_id}', headers={'Authorization': f'Bearer {token}'})
    
    if response.status_code == 200:
        certificates = response.json()
        return render_template('user_certificates.html', certificates=certificates)
    else:
        flash('Failed to fetch certificates. Please log in again.', 'error')
        return redirect(url_for('login'))

@app.route('/admin/dashboard')
def admin_dashboard():
    token = session.get('token')
    if not token:
        flash('Session expired. Please login again.', 'error')
        return redirect(url_for('login'))

    if session.get('role') != 'admin':
        flash('Unauthorized access.', 'error')
        return redirect(url_for('home'))

    return render_template('admin_dashboard.html')

@app.route('/admin/create_certificate', methods=['GET', 'POST'])
def admin_create_certificate():
    token = session.get('token')
    if not token:
        flash('Session expired. Please login again.', 'error')
        return redirect(url_for('login'))

    if request.method == 'POST':
        user_id = request.form.get('user_id')
        payload = {
            'nome_coordenador': request.form['nome_coordenador'],
            'nome_curso': request.form['nome_curso'],
            'nome_professor': request.form['nome_professor'],
            'carga_horaria': int(request.form['carga_horaria']),
            'data_conclusao': request.form['data_conclusao'],
            'descricao': request.form['descricao'],
            'user_id': None if user_id == '0' else user_id
        }
        
        print("Payload to be sent:", payload)  # Depuração

        headers = {'Authorization': f'Bearer {token}'}
        response = requests.post(f'{API_URL}/certificates/create_certificate', json=payload, headers=headers)

        if response.status_code in [200, 201]:
            flash('Certificate added successfully.', 'success')
            return redirect(url_for('admin_dashboard'))
        else:
            flash('Failed to add certificate. Please try again.', 'error')

    users = requests.get(f'{API_URL}/users/get_all_users', headers={'Authorization': f'Bearer {token}'})
    if users.status_code == 200:
        return render_template('admin_create_certificate.html', users=users.json())
    else:
        flash('Failed to fetch users. Please try again.', 'error')
        return redirect(url_for('admin_dashboard'))

@app.route('/admin/view_certificates', methods=['GET', 'POST'])
def admin_view_certificates():
    token = session.get('token')
    if not token:
        flash('Session expired. Please login again.', 'error')
        return redirect(url_for('login'))

    if request.method == 'POST':
        action = request.form['action']
        cert_id = request.form.get('cert_id')
        
        if action == 'save':
            print(cert_id)
            payload = {
                'nome_curso': request.form['nome_curso'],
                'nome_coordenador': request.form['nome_coordenador'],
                'nome_professor': request.form['nome_professor'],
                'carga_horaria': int(request.form['carga_horaria']),
                'data_conclusao': request.form['data_conclusao'],
                'descricao': request.form['descricao'],
            }
            headers = {'Authorization': f'Bearer {token}'}
            response = requests.put(f'{API_URL}/certificates/update_certificate/{cert_id}', json=payload, headers=headers)

            if response.status_code in [200, 204]:
                flash('Certificate updated successfully.', 'success')
            else:
                flash('Failed to update certificate. Please try again.', 'error')

        elif action == 'delete':
            headers = {'Authorization': f'Bearer {token}'}
            response = requests.delete(f'{API_URL}/certificates/delete_certificate/{cert_id}', headers=headers)
            
            if response.status_code in [200, 204]:
                flash('Operation successful.', 'success')
            else:
                flash('Failed to perform operation. Please try again.', 'error')

    user_id = session.get('user_id')
    response = requests.get(f'{API_URL}/users/get_certificates/{user_id}', headers={'Authorization': f'Bearer {token}'})
    
    if response.status_code == 200:
        certificates = response.json()
        return render_template('admin_view_certificates.html', certificates=certificates)
    else:
        flash('Failed to retrieve certificates. Please try again.', 'error')
        return redirect(url_for('admin_dashboard'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/download/<certificate_id>', methods=['GET'])
def download(certificate_id):
    token = session.get('token')
    if not token:
        flash('Sessão expirada. Por favor, faça login novamente.', 'error')
        return redirect(url_for('user_certificates'))
    
    print(certificate_id)

    response = requests.get(f'{API_URL}/certificates/generate_certificate/{certificate_id}', headers={'Authorization': f'Bearer {token}'})

    if response.status_code == 200:
        imagem_bytes = response.content
        return send_file(BytesIO(imagem_bytes), as_attachment=True, download_name=f'certificate_{certificate_id}.png', mimetype='image/png')
    
    else:
        flash('Falha ao baixar o certificado. Por favor, tente novamente.', 'error')
        return redirect(url_for('user_certificates'))


if __name__ == '__main__':
    app.run(debug=True, port=3000, host='0.0.0.0') # Executa o servidor Flask na porta 3000
