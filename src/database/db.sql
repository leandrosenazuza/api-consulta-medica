-- Criação da table principal.
CREATE TABLE IF NOT EXISTS TAB_PACIENTES(
    codigoPaciente INT(4) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT,
    CPF VARCHAR(11) NOT NULL,
    nome VARCHAR(30) NOT NULL,
    dataNascimento DATE,
    idade INT NOT NULL,
    codigoColetaPaciente INT(4) UNSIGNED ZEROFILL, -- (CHAVE ESTRANGEIRA)
    PRIMARY KEY(codigoPaciente),
    FOREIGN KEY (codigoColetaPaciente) REFERENCES TAB_COLETA_PACIENTE(codigoColetaPaciente) ON DELETE CASCADE

)

-- Criação da table principal.
CREATE TABLE IF NOT EXISTS TAB_COLETA_PACIENTE(
    codigoColetaPaciente INT(4) UNSIGNED ZEROFILL NOT NULL AUTO_INCREMENT,
    coletaAnos JSON NOT NULL, -- A ideia é armazenar assim: ["2022", "2024"], apenas os anos que houve coleta
    ultimaColeta DATE,
    proximaColeta DATE,
    PRIMARY KEY(codigoColetaPaciente)
)