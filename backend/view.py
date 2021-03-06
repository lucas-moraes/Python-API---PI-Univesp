from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from backend.controllers import get_controller
from backend.controllers import post_controller
from backend.controllers import delete_controller
from backend.controllers import update_controller
from pydantic import BaseModel
from typing import List


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def root():
    return {"home": "It's running !"}


#----------------------------------------#
#                                        #
#  Alergias                              #
#                                        #
#----------------------------------------#

class Alergias(BaseModel):
    matricula_sus: int
    descricao: str


@app.get('/listar-alergias')
def ListarAlergias() -> List:
    try:
        do = get_controller.Get()
        lista = do.ListarTodasAlergias()
        if lista is False:
            return JSONResponse(status_code=404, content={"message": "Erro na consulta"})
        elif (lista is None):
            return JSONResponse(status_code=404, content={"message": "Não encontrado"})
        return lista
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


@app.post('/listar-alergias-matricula/{matricula_sus}')
def ListarAlergias(matricula_sus: int) -> List:
    try:
        do = post_controller.Search()
        lista = do.ListarAlergiasPorMatricula(matricula_sus)
        if lista is False:
            return JSONResponse(status_code=404, content={"message": "Erro na consulta"})
        elif (lista is None):
            return JSONResponse(status_code=404, content={"message": "Não encontrado"})
        return lista
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


@app.post('/listar-alergias-id/{id}')
def ListarAlergiasPodId(id: int) -> List:
    try:
        do = post_controller.Search()
        lista = do.ListarAlergiasPorId(id)
        if lista is False:
            return JSONResponse(status_code=404, content={"message": "Erro na consulta"})
        elif (lista is None):
            return JSONResponse(status_code=404, content={"message": "Não encontrado"})
        return lista
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


@app.post('/inserir-alergia')
def InserirAlergia(inserir: Alergias) -> List:
    try:
        do = post_controller.Insert()
        response = do.InserirAlergia(
            inserir.matricula_sus,
            inserir.descricao
        )
        if response is False:
            return {"response": "Alergia depende do Paciente"}
        return JSONResponse(status_code=200, content={"message": "Executado com sucesso"})
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


@app.put('/editar-alergia')
def EditarAlergia(id: int, desc: str) -> List:
    try:
        do = update_controller.Update()
        response = do.EditarAlergia(id, desc)
        if response is False:
            return {"response": "Edição não realizada"}
        return JSONResponse(status_code=200, content={"message": "Executado com sucesso"})
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


@app.delete('/deletar-alergia/{id}')
def DeletarAlergia(id: int) -> List:
    try:
        do = delete_controller.Delete()
        response = do.DeletarAlergia(id)
        if response is False:
            return {"response": "Exclusão não realizada"}
        return JSONResponse(status_code=200, content={"message": "Executado com sucesso"})
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


#----------------------------------------#
#                                        #
#  Consultas                             #
#                                        #
#----------------------------------------#

class Consultas(BaseModel):
    matricula_sus: int
    id_especialidade_medica: int
    data_hora_marcada: str  # YYYY-MM-DD hh:mm:ss
    id_medico: int
    id_local_atendimento: int
    compareceu: bool


@app.get('/listar-consultas')
def ListarConsultas() -> List:
    try:
        do = get_controller.Get()
        lista = do.ListarTodasConsultas()
        if lista is False:
            return JSONResponse(status_code=404, content={"message": "Erro na consulta"})
        elif (lista is None):
            return JSONResponse(status_code=404, content={"message": "Não encontrado"})
        return lista
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


@app.post('/listar-consultas-matricula/{matricula_sus}')
def ListarConsultasPorMatricula(matricula_sus: int) -> List:
    try:
        do = post_controller.Search()
        lista = do.ListarConsultasPorMatricula(matricula_sus)
        if lista is False:
            return JSONResponse(status_code=404, content={"message": "Erro na consulta"})
        elif (lista is None):
            return JSONResponse(status_code=404, content={"message": "Não encontrado"})
        return lista
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


@app.post('/listar-consultas-id/{id}')
def ListarConsultasPodId(id: int) -> List:
    try:
        do = post_controller.Search()
        lista = do.ListarConsultasPorId(id)
        if lista is False:
            return JSONResponse(status_code=404, content={"message": "Erro na consulta"})
        elif (lista is None):
            return JSONResponse(status_code=404, content={"message": "Não encontrado"})
        return lista
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


@app.post('/inserir-consulta')
def InserirConsulta(inserir: Consultas) -> List:
    try:
        iten = post_controller.Insert()
        response = iten.InserirConsulta(
            inserir.matricula_sus,
            inserir.id_especialidade_medica,
            inserir.data_hora_marcada,
            inserir.id_medico,
            inserir.id_local_atendimento,
            inserir.compareceu
        )
        if response is False:
            return {"response": "Consulta depende do Paciente, Local de atendimento, medicos e especialidade médica"}
        return JSONResponse(status_code=200, content={"message": "Executado com sucesso"})
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


@app.put('/editar-consulta')
def EditarConsulta(id: int, edit: Consultas) -> List:
    try:
        do = update_controller.Update()
        response = do.EditarConsulta(
            id,
            edit.matricula_sus,
            edit.id_especialidade_medica,
            edit.data_hora_marcada,
            edit.id_medico,
            edit.id_local_atendimento,
            edit.compareceu
        )
        if response is False:
            return {"response": "Edição não realizada"}
        return JSONResponse(status_code=200, content={"message": "Executado com sucesso"})
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


@app.delete('/deletar-consulta/{id}')
def DeletarConsulta(id: int) -> List:
    try:
        do = delete_controller.Delete()
        response = do.DeletarConsulta(id)
        if response is False:
            return {"response": "Edição não realizada"}
        return JSONResponse(status_code=200, content={"message": "Executado com sucesso"})
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


#----------------------------------------#
#                                        #
#  Especialidade Medicas                 #
#                                        #
#----------------------------------------#

class EspecialidadeMedica(BaseModel):
    desc_especialidade: str


@app.get('/listar-especialidades-medicas')
def ListarEspecialidadesMedicas() -> List:
    try:
        do = get_controller.Get()
        lista = do.ListarTodasEspecialidadesMedicas()
        if lista is False:
            return JSONResponse(status_code=404, content={"message": "Erro na consulta"})
        elif (lista is None):
            return JSONResponse(status_code=404, content={"message": "Não encontrado"})
        return lista
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


@app.post('/listar-especialidade-medica-id/{id}')
def ListarEspecialidadeMedicaPodId(id: int) -> List:
    try:
        do = post_controller.Search()
        lista = do.ListarEspecialidadeMedicaPorId(id)
        if lista is False:
            return JSONResponse(status_code=404, content={"message": "Erro na consulta"})
        elif (lista is None):
            return JSONResponse(status_code=404, content={"message": "Não encontrado"})
        return lista
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


@app.post('/inserir-especialidade-medica')
def InserirEspecialidadMedica(post: EspecialidadeMedica) -> List:
    try:
        do = post_controller.Insert()
        response = do.InserirEspecialidadeMedica(
            post.desc_especialidade
        )
        if response is False:
            return JSONResponse(status_code=404, content={"message": "Erro na resposta"})
        return JSONResponse(status_code=200, content={"message": "Executado com sucesso"})
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


@app.put('/editar-especialidade-medica')
def EditarEspecialidadeMedica(id: int, edit: EspecialidadeMedica) -> List:
    try:
        do = update_controller.Update()
        response = do.EditarEspecialidadeMedica(id, edit.desc_especialidade)
        if response is False:
            return JSONResponse(status_code=404, content={"message": "Erro na resposta"})
        return JSONResponse(status_code=200, content={"message": "Executado com sucesso"})
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


@app.delete('/deletar-especialidade-medica/{id}')
def DeletarEspecialidadeMedica(id: int) -> List:
    try:
        do = delete_controller.Delete()
        response = do.DeletarEspecialidadeMedica(id)
        if response is False:
            return JSONResponse(status_code=404, content={"message": "Erro na resposta"})
        return JSONResponse(status_code=200, content={"message": "Executado com sucesso"})
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


#----------------------------------------#
#                                        #
#  Local Atendimento                     #
#                                        #
#----------------------------------------#

class LocalAtendimento(BaseModel):
    nome_local: str
    endereco: str
    complemento: str
    bairro: str
    cep: str
    cidade: str
    uf: str


@app.get('/listar-local-atendimento')
def ListarLocalAtendimento() -> List:
    try:
        do = get_controller.Get()
        lista = do.ListarTodosLocalAtendimento()
        if lista is False:
            return JSONResponse(status_code=404, content={"message": "Erro na consulta"})
        elif (lista is None):
            return JSONResponse(status_code=404, content={"message": "Não encontrado"})
        return lista
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


@app.post('/listar-local-atendimento-id/{id}')
def ListarLocalAtendimentoPodId(id: int) -> List:
    try:
        do = post_controller.Search()
        lista = do.ListarLocalAtendimentoPorId(id)
        if lista is False:
            return JSONResponse(status_code=404, content={"message": "Erro na consulta"})
        elif (lista is None):
            return JSONResponse(status_code=404, content={"message": "Não encontrado"})
        return lista
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


@app.post('/inserir-local-atendimento')
def InserirLocalAtendimento(post: LocalAtendimento) -> List:
    try:
        do = post_controller.Insert()
        response = do.InserirLocalAtendiemnto(
            post.nome_local,
            post.endereco,
            post.complemento,
            post.bairro,
            post.cep,
            post.cidade,
            post.uf
        )
        if response is False:
            return JSONResponse(status_code=404, content={"message": "Erro na resposta"})
        return JSONResponse(status_code=200, content={"message": "Executado com sucesso"})
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


@app.put('/editar-local-atendimento')
def EditarLocalAtendimento(id: int, edit: LocalAtendimento) -> List:
    try:
        do = update_controller.Update()
        response = do.EditarLocalAtendimento(
            id,
            edit.nome_local,
            edit.endereco,
            edit.complemento,
            edit.bairro,
            edit.cep,
            edit.cidade,
            edit.uf
        )
        print('ok')
        if response is False:
            return JSONResponse(status_code=404, content={"message": "Erro na resposta"})
        return JSONResponse(status_code=200, content={"message": "Executado com sucesso"})
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


@app.delete('/deletar-local-atendimento/{id}')
def DeletarEspecialidadeMedica(id: int) -> List:
    try:
        do = delete_controller.Delete()
        response = do.DeletarLocalAtendimento(id)
        if response is False:
            return JSONResponse(status_code=404, content={"message": "Erro na resposta"})
        return JSONResponse(status_code=200, content={"message": "Executado com sucesso"})
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})

#----------------------------------------#
#                                        #
#  Medicos                               #
#                                        #
#----------------------------------------#


class Medicos(BaseModel):
    crm: int
    nome: str
    sobrenome: str
    endereco: str
    complemento: str
    bairro: str
    cep: str
    cidade: str
    uf: str
    id_especialidade_medica: int


@app.get('/listar-medicos')
def ListarMedicos() -> List:
    try:
        do = get_controller.Get()
        lista = do.ListarTodosMedicos()
        if lista is False:
            return JSONResponse(status_code=404, content={"message": "Erro na consulta"})
        elif (lista is None):
            return JSONResponse(status_code=404, content={"message": "Não encontrado"})
        return lista
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


@app.post('/listar-medicos-id/{id}')
def ListarMedicosPodId(id: int) -> List:
    try:
        do = post_controller.Search()
        lista = do.ListarMedicosPorId(id)
        if lista is False:
            return JSONResponse(status_code=404, content={"message": "Erro na consulta"})
        elif (lista is None):
            return JSONResponse(status_code=404, content={"message": "Não encontrado"})
        return lista
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


@app.post('/inserir-medico')
def InserirMedico(post: Medicos) -> List:
    try:
        do = post_controller.Insert()
        response = do.InserirMedico(
            post.crm,
            post.nome,
            post.sobrenome,
            post.endereco,
            post.complemento,
            post.bairro,
            post.cep,
            post.cidade,
            post.uf,
            post.id_especialidade_medica
        )
        if response is False:
            return JSONResponse(status_code=404, content={"message": "Erro na resposta"})
        return JSONResponse(status_code=200, content={"message": "Executado com sucesso"})
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


@app.put('/editar-medico')
def EditarMedico(id: int, edit: Medicos) -> List:
    try:
        do = update_controller.Update()
        response = do.EditarMedico(
            id,
            edit.crm,
            edit.nome,
            edit.sobrenome,
            edit.endereco,
            edit.complemento,
            edit.bairro,
            edit.cep,
            edit.cidade,
            edit.uf,
            edit.id_especialidade_medica
        )
        if response is False:
            return JSONResponse(status_code=404, content={"message": "Erro na resposta"})
        return JSONResponse(status_code=200, content={"message": "Executado com sucesso"})
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


@app.delete('/deletar-medico/{id}')
def DeletarMedico(id: int) -> List:
    try:
        do = delete_controller.Delete()
        response = do.DeletarMedico(id)
        if response is False:
            return JSONResponse(status_code=404, content={"message": "Erro na resposta"})
        return JSONResponse(status_code=200, content={"message": "Executado com sucesso"})
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})

#----------------------------------------#
#                                        #
#  Pacientes                             #
#                                        #
#----------------------------------------#


class Pacientes(BaseModel):
    matricula_sus: int
    data_registro: str
    tipo_sangue: str
    nome: str
    sobrenome: str
    data_nasc: str
    endereco: str
    complemento: str
    bairro: str
    cep: str
    cidade: str
    uf: str


@app.get('/listar-pacientes')
def ListarPacientes() -> List:
    try:
        do = get_controller.Get()
        lista = do.ListarTodosPacientes()
        if lista is False:
            return JSONResponse(status_code=404, content={"message": "Erro na consulta"})
        elif (lista is None):
            return JSONResponse(status_code=404, content={"message": "Não encontrado"})
        return lista
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


@app.post('/listar-paciente-matricula/{matricula_sus}')
def ListarPacientePorMatricula(matricula_sus: int) -> List:
    try:
        do = post_controller.Search()
        lista = do.ListarPacientesPorMatricula(matricula_sus)
        if lista is False:
            return JSONResponse(status_code=404, content={"message": "Erro na consulta"})
        elif (lista is None):
            return JSONResponse(status_code=404, content={"message": "Não encontrado"})
        return lista
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


@app.post('/listar-pacientes-id/{id}')
def ListarPacientesPodId(id: int) -> List:
    try:
        do = post_controller.Search()
        lista = do.ListarPacientesPorId(id)
        if lista is False:
            return JSONResponse(status_code=404, content={"message": "Erro na consulta"})
        elif (lista is None):
            return JSONResponse(status_code=404, content={"message": "Não encontrado"})
        return lista
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


@app.post('/inserir-paciente')
def InserirPaciente(post: Pacientes) -> List:
    try:
        do = post_controller.Insert()
        response = do.InserirPaciente(
            post.matricula_sus,
            post.data_registro,
            post.tipo_sangue,
            post.nome,
            post.sobrenome,
            post.data_nasc,
            post.endereco,
            post.complemento,
            post.bairro,
            post.cep,
            post.cidade,
            post.uf
        )
        if response is False:
            return JSONResponse(status_code=404, content={"message": "Erro na resposta"})
        return JSONResponse(status_code=200, content={"message": "Executado com sucesso"})
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


@app.put('/editar-paciente')
def EditarPaciente(id: int, edit: Pacientes) -> List:
    try:
        do = update_controller.Update()
        response = do.EditarPaciente(
            id,
            edit.matricula_sus,
            edit.data_registro,
            edit.tipo_sangue,
            edit.nome,
            edit.sobrenome,
            edit.data_nasc,
            edit.endereco,
            edit.complemento,
            edit.bairro,
            edit.cep,
            edit.cidade,
            edit.uf
        )
        if response is False:
            return JSONResponse(status_code=404, content={"message": "Erro na resposta"})
        return JSONResponse(status_code=200, content={"message": "Executado com sucesso"})
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})


@app.delete('/deletar-paciente/{id}')
def DeletarPaciente(id: int) -> List:
    try:
        do = delete_controller.Delete()
        response = do.DeletarPaciente(id)
        if response is False:
            return JSONResponse(status_code=404, content={"message": "Erro na resposta"})
        return JSONResponse(status_code=200, content={"message": "Executado com sucesso"})
    except:
        return JSONResponse(status_code=404, content={"message": "Erro na execução"})
