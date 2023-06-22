from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://bl78orpw6rhz6o46nknc:pscale_pw_jINTdWmaSzMGRPsSDXDNZHzMNiYSl2jLyuwcIxOiQrk@aws.connect.psdb.cloud/jplcareers?charset=utf8mb4"

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    column_names = result.keys()
    
    jobs = []
    
    for row in result.all():
      jobs.append(dict(zip(column_names, row)))
    
    return jobs

  
  # result = conn.execute(text("select * from jobs"))
  # result_all = result.all()
  # first_result = result_all[0]
  # column_names = result.keys() 
  # first_result_dict = dict(zip(column_names, first_result))
  # print(first_result_dict)