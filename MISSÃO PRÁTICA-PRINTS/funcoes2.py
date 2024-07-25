def loginUsuario (perfil) :
    perfil = 'admin'

    if perfil.lower() == 'admin' :
        print('Bem vindo, administrador.')
    else:
        print('Bem vindo, usuário.')

loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('Usuário')
loginUsuario('usuário')