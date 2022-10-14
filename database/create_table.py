from sqlalchemy import *

engine = create_engine('sqlite:///big_data_airlines.db', echo=True)
meta = MetaData()

#Table's schema
air_cia = Table( 
    'air_cia', meta,
    Column('CNPJ', String),
    Column('ATIVIDADES_AEREAS', String), 
    Column('ENDERECO_SEDE', String),
    Column('TELEFONE', String),
    Column('EMAIL', String),
    Column('DECISAO_OPERACIONAL', String) ,
    Column('DATA_DECISAO_OPERACIONAL', Date),
    Column('VALIDADE_OPERACIONAL', Date),
    Column('ICAO', String),
    Column('IATA', String)
)

vra_data = Table(
    'vra_data', meta,
    Column('ICAO_EMPRESA_AEREA', String),
    Column('NUMERO_VOO', String), 
    Column('CODIGO_AUTORIZACAO', String),
    Column('CODIGO_TIPO_LINHA', String),
    Column('ICAO_AERODROMO_ORIGEM', String),
    Column('ICAO_AERODROMO_DESTINO', String) ,
    Column('PARTIDA_PREVISTA', Date),
    Column('PARTIDA_REAL', Date),
    Column('CHEGADA_PREVISTA', Date),
    Column('CHEGADA_REAL', Date),
    Column('SITUACAO_VOO', String),
    Column('CODIGO_JUSTIFICATIVA', String)
)

aerodromos   = Table(
    'aerodromos', meta,
    Column('ID', String),
    Column('IATA', String), 
    Column('ICAO', String),
    Column('NAME', String),
    Column('LOCATION', String),
    Column('STREET_NUMBER', String) ,
    Column('STREET', String),
    Column('CITY', String),
    Column('COUNTY', String),
    Column('STATE', String),
    Column('COUNTRY_ISO', String),
    Column('COUNTRY', String),
    Column('POSTAL_CODE', String),
    Column('PHONE', String), 
    Column('LATITUDE', String),
    Column('LONGITUDE', String),
    Column('UCT', String),
    Column('WEBSITE', String), 
    Column('ERROR_TEXT', String)
)


if __name__=='__main__':
    meta.create_all(engine)



