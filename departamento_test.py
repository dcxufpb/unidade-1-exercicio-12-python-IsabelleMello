import pytest

import departamento

def verifica_campo_obrigatorio_objeto(mensagem_esperada, departamento):
    with pytest.raises(Exception) as excinfo:
        departamento.dados_departamento()
    the_exception = excinfo.value
    assert mensagem_esperada == str(the_exception)

NOME_DEPARTAMENTO = "Departamento 1"
SIGLA = "Dep 1"
LOCALIZACAO = "Localização 1"
NOME_COORDENADOR = "Coordenador 1"
IDADE = 30
CPF = "999.999.999-99"    


COORDENADOR_COMPLETO = departamento.Coordenador(NOME_COORDENADOR, IDADE, CPF)
DEPARTAMENTO_COMPLETO = departamento.Departamento(NOME_DEPARTAMENTO, SIGLA, LOCALIZACAO, COORDENADOR_COMPLETO)

TEXTO_ESPERADO_DEPARTAMENTO_COMPLETO = """Departamento 1, Dep 1
Localização do departamento: Localização 1
Coordenador 1
Idade do coordenador: 30
CPF do coordenador: 999.999.999-99"""

def test_departamento_completo():
    assert (DEPARTAMENTO_COMPLETO.dados_departamento() == TEXTO_ESPERADO_DEPARTAMENTO_COMPLETO)


SIGLA_NULA = departamento.Departamento(NOME_DEPARTAMENTO, None, LOCALIZACAO, COORDENADOR_COMPLETO)
SIGLA_VAZIA = departamento.Departamento(NOME_DEPARTAMENTO, "", LOCALIZACAO, COORDENADOR_COMPLETO)

TEXTO_ESPERADO_SEM_SIGLA = """Departamento 1
Localização do departamento: Localização 1
Coordenador 1
Idade do coordenador: 30
CPF do coordenador: 999.999.999-99"""

def test_sigla_nula():
    assert (SIGLA_NULA.dados_departamento() == TEXTO_ESPERADO_SEM_SIGLA)

def test_sigla_vazia():
    assert (SIGLA_VAZIA.dados_departamento() == TEXTO_ESPERADO_SEM_SIGLA)


COORDENADOR_IDADE_NULA = departamento.Coordenador(NOME_COORDENADOR, None, CPF)
COORDENADOR_IDADE_VAZIA = departamento.Coordenador(NOME_COORDENADOR, "", CPF)
IDADE_NULA = departamento.Departamento(NOME_DEPARTAMENTO, SIGLA, LOCALIZACAO, COORDENADOR_IDADE_NULA)
IDADE_VAZIA = departamento.Departamento(NOME_DEPARTAMENTO, SIGLA, LOCALIZACAO, COORDENADOR_IDADE_VAZIA)

TEXTO_ESPERADO_SEM_IDADE = """Departamento 1, Dep 1
Localização do departamento: Localização 1
Coordenador 1
CPF do coordenador: 999.999.999-99"""

def test_idade_nula():
    assert (IDADE_NULA.dados_departamento() == TEXTO_ESPERADO_SEM_IDADE)

def test_idade_vazia():
    assert (IDADE_VAZIA.dados_departamento() == TEXTO_ESPERADO_SEM_IDADE)

SIGLA_E_IDADE_VAZIAS = departamento.Departamento(NOME_DEPARTAMENTO, None, LOCALIZACAO, COORDENADOR_IDADE_VAZIA)

TEXTO_ESPERADO_SEM_SIGLA_SEM_IDADE = """Departamento 1
Localização do departamento: Localização 1
Coordenador 1
CPF do coordenador: 999.999.999-99"""

def test_sigla_e_idade_vazias():
    assert (SIGLA_E_IDADE_VAZIAS.dados_departamento() == TEXTO_ESPERADO_SEM_SIGLA_SEM_IDADE)


NOME_DEPARTAMENTO_NULO = departamento.Departamento(None, SIGLA, LOCALIZACAO, COORDENADOR_COMPLETO)
NOME_DEPARTAMENTO_VAZIO = departamento.Departamento("", SIGLA, LOCALIZACAO, COORDENADOR_COMPLETO)

MENSAGEM_NOME_OBRIGATORIO = "O campo nome do departamento é obrigatório"

def test_valida_nome_departamento():
    verifica_campo_obrigatorio_objeto(MENSAGEM_NOME_OBRIGATORIO, NOME_DEPARTAMENTO_NULO)
    verifica_campo_obrigatorio_objeto(MENSAGEM_NOME_OBRIGATORIO, NOME_DEPARTAMENTO_VAZIO)


LOCALIZACAO_NULA = departamento.Departamento(NOME_DEPARTAMENTO, SIGLA, None, COORDENADOR_COMPLETO)
LOCALIZACAO_VAZIA = departamento.Departamento(NOME_DEPARTAMENTO, SIGLA, "", COORDENADOR_COMPLETO)

MENSAGEM_LOCALIZACAO_OBRIGATORIA = "O campo localização do departamento é obrigatório"

def test_valida_localizacao():
    verifica_campo_obrigatorio_objeto(MENSAGEM_LOCALIZACAO_OBRIGATORIA, LOCALIZACAO_NULA)
    verifica_campo_obrigatorio_objeto(MENSAGEM_LOCALIZACAO_OBRIGATORIA, LOCALIZACAO_VAZIA)

COORDENADOR_NOME_NULO = departamento.Coordenador(None, IDADE, CPF)
COORDENADOR_NOME_VAZIO = departamento.Coordenador("", IDADE, CPF)
NOME_COORDENADOR_NULO = departamento.Departamento(NOME_DEPARTAMENTO, SIGLA, LOCALIZACAO, COORDENADOR_NOME_NULO)
NOME_COORDENADOR_VAZIO = departamento.Departamento(NOME_DEPARTAMENTO, SIGLA, LOCALIZACAO, COORDENADOR_NOME_VAZIO)

MENSAGEM_NOME_COORDENADOR_OBRIGATORIO = "O campo nome do coordenador do departamento é obrigatório"

def test_valida_nome_coordenador():
    verifica_campo_obrigatorio_objeto(MENSAGEM_NOME_COORDENADOR_OBRIGATORIO, NOME_COORDENADOR_NULO)
    verifica_campo_obrigatorio_objeto(MENSAGEM_NOME_COORDENADOR_OBRIGATORIO, NOME_COORDENADOR_VAZIO)


COORDENADOR_CPF_NULO = departamento.Coordenador(NOME_COORDENADOR, IDADE, None)
COORDENADOR_CPF_VAZIO = departamento.Coordenador(NOME_COORDENADOR, IDADE, "")
CPF_NULO = departamento.Departamento(NOME_DEPARTAMENTO, SIGLA, LOCALIZACAO, COORDENADOR_CPF_NULO)
CPF_VAZIO = departamento.Departamento(NOME_DEPARTAMENTO, SIGLA, LOCALIZACAO, COORDENADOR_CPF_VAZIO)

MENSAGEM_CPF_OBRIGATORIO = "O campo cpf do coordenador do departamento é obrigatório"

def test_valida_cpf():
    verifica_campo_obrigatorio_objeto(MENSAGEM_CPF_OBRIGATORIO, CPF_NULO)
    verifica_campo_obrigatorio_objeto(MENSAGEM_CPF_OBRIGATORIO, CPF_VAZIO)