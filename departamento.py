# coding: utf-8

class Departamento:

    def __init__(self, nome, sigla, localizacao, coordenador):
        self.nome = nome
        self.sigla = sigla
        self.localizacao = localizacao
        self.coordenador = coordenador

    def validar_campos_obrigatorios(self):
        
        if not self.nome:
            raise Exception("O campo nome do departamento é obrigatório")
        if not self.localizacao:
            raise Exception("O campo localização do departamento é obrigatório")

    def dados_departamento(self):
        
        self.validar_campos_obrigatorios()

        _nome = self.sigla and self.nome + ", " or self.nome
        _sigla = self.sigla and self.sigla or ""
        _localizacao = "Localização do departamento: " + self.localizacao
    
        return (
f"""{_nome}{_sigla}
{_localizacao}
{self.coordenador.dados_coordenador()}""")

class Coordenador:

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
    
    def validar_campos_obrigatorios(self):
        
        if not self.nome:
            raise Exception("O campo nome do coordenador do departamento é obrigatório")
        if not self.cpf:
            raise Exception("O campo cpf do coordenador do departamento é obrigatório")
    
    def dados_coordenador(self):
        
        self.validar_campos_obrigatorios()

        _idade = self.idade and (f"\nIdade do coordenador: {self.idade}") or ""
        _cpf = "CPF do coordenador: " + self.cpf

        return (
f"""{self.nome}{_idade}
{_cpf}""")


