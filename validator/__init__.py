from azure.functions import HttpRequest, HttpResponse
import logging

def main(req: HttpRequest) -> HttpResponse:
    logging.info('Iniciando a validação do CPF.')

    cpf = req.params.get('cpf')
    if not cpf:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            cpf = req_body.get('cpf')

    if cpf:
        if validate_cpf(cpf):
            return HttpResponse(f"O CPF {cpf} é válido.")
        else:
            return HttpResponse(f"O CPF {cpf} é inválido.", status_code=400)
    else:
        return HttpResponse(
            "Esta função HTTP foi executada com sucesso. Passe um CPF na string de consulta ou no corpo da solicitação para validação.",
            status_code=200
        )

def validate_cpf(cpf: str) -> bool:
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    for i in range(9, 11):
        value = sum((int(cpf[num]) * ((i + 1) - num) for num in range(0, i)))
        check_digit = ((value * 10) % 11) % 10
        if check_digit != int(cpf[i]):
            return False

    return True