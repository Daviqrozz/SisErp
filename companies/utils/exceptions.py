from rest_framework.exceptions import APIException

class NotFoundEmployee(APIException):
    status_code = 404
    default_detail = 'Funcionario da empresa'
    default_code = 'Not_Found_Employee'
class NotFoundGroup(APIException):
    status_code = 404
    default_detail = 'Grupo da empresa'
    default_code = 'Not_Found_Group'
    
class RequiredFields(APIException):
    status_code = 400
    default_detail = 'Preencha os campos corretamente'
    default_code = 'error_required_field'
    
class NotFoundTasks(APIException):
    status_code = 404
    default_detail = 'Nao existem tarefas'
    default_code = 'Not_Found_Tasks'

class NotFoundTasksStatus(APIException):
    status_code = 404
    default_detail = 'Status da tarefa nao encontrado'
    default_code = 'Not_Found_Tasks_Status'