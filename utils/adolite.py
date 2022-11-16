"""
Adolite
"""

from sqlite3 import Error
import sqlite3


class AdoLite():
  """
    Adolite Class
  """
  __cnn = None
  __error = None
  __cursor = None

  @property
  def cnn(self):
    return self.__cnn
  
  @property
  def error(self):
    return self.__error

  @property
  def cursor(self):
    return self.__cursor
  

  def __init__(self, name:str):
    self.__database = name

  @staticmethod
  def __row_to_dict(row, descriptions)->dict:
    """
    """
    _n = 0
    _row = {}
    for _desc in descriptions:
      _row[_desc[0].lower()] = row[_n]
      _n+=1
    return _row

  def __new_cursor(self)->bool:
    self.__error = None
    try:
      if self.__cnn:
        self.__cursor = self.__cnn.cursor()
        return True
      return False
    except Error as err:
      self.__error = err
    return False

  def createdb(self)->bool:
    """
      Crea la base de datos
    """
    self.__cnn = None
    self.__error = None
    try:
      self.__cnn = sqlite3.connect(self.__database)
      return True
    except Error as err:
      self.__error = err
    return False

  def opendb(self)->bool:
    """
      Abre la base de datos
    """
    self.__cnn = None
    self.__error = None
    try:
      self.__cnn = sqlite3.connect(self.__database)
      return True
    except Error as err:
      self.__error = err
    return False

  def closedb(self)->bool:
    """
      Clierra la base de datos
    """
    self.__error = None
    try:
      if self.__cnn:
        self.__cnn.close()
        return True
    except Error as err:
      self.__error = err
    return False

  def is_cursor(self)->bool:
    """
      Determina si hay un cursor activo
    """
    if self.__cursor is None:
      return False
    return True

  def run_sql(self, mi_sql:str)->bool:
    """
      Ejecuta una sentencia SQL sin parametros
    """
    self.__error = None
    try:
      if self.__cnn:
        if not self.is_cursor():
          self.__new_cursor()
        self.__cursor.execute(mi_sql)
        return True
    except Error as err:
      self.__error = err
    return False

  def run_sql_param(self, mi_sql:str, mi_param:tuple)->bool:
    """
      Eecuta una sentencia SQL pasando parametros
    """
    self.__error = None
    try:
      if self.__cnn:
        if not self.is_cursor():
          self.__new_cursor()
        self.__cursor.execute(mi_sql, mi_param)
        return True
    except Error as err:
      self.__error = err
    return False

  def run_sql_script(self, mi_script:str)->bool:
    """
      Ejecuta una o mas sentencias SQL
    """
    self.__error = None
    try:
      if self.__cnn:
        if not self.is_cursor():
          self.__new_cursor()
        self.__cursor.executescript(mi_script)
        return True
    except Error as err:
      self.__error = err
    return False

  def run_sql_script_file(self, name:str, encoding='utf-8')->bool:
    """
      Ejecuta una o mas sentencias SQL
    """
    self.__error = None
    try:
      if self.__cnn:
        if not self.is_cursor(): 
          self.__new_cursor()
        with open(file=name, mode="r", encoding=encoding) as f:
          buffer = f.read()
          self.__cursor.executescript(buffer)
        return True
    except Error as err:
      self.__error = err
    except FileNotFoundError as err:
      self.__error = err
    return False

  def fetch_one(self):
    """
      Devuelve el primer registro del cursor activo
    """
    self.__error = None
    if self.is_cursor():
      try:
        return self.__cursor.fetchone()
      except Error as err:
        self.__error = err
        return None
    return None

  def fetch_all(self)->list:
    """
      Devuelve todos los registros del cursor activo
    """
    self.__error = None
    if self.is_cursor():
      try:
        rows = self.__cursor.fetchall()
        fields = self.__cursor.description
        result = []
        for row in rows:
          result.append(self.__row_to_dict(row, fields))
        return result
      except Error as err:
        self.__error = err
        return []
    return []

  def get_last_error(self)->Error:
    """
      Devuelve el ultimo error encontrado
    """
    return self.__error

  def print_error(self):
    """
      Se imprime el error
    """
    if self.__error is None:
      return
    print(self.__error)

  def commit(self)->bool:
    """
      Ejecuta un commiten la conexion activa
    """
    try:
      if self.__cnn:
        self.__cnn.commit()
        return True
    except Error as err:
      self.__error = err
    return False
