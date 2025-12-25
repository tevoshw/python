# TRY-EXECEPT IT'S A CONTROL STRUCTURE CONDITIONAL AND LONG



while True:
    try: # PRIMEIRA COISA QUE SERÁ RODADA SERÁ ISSO, APÓS AS EXPECTS
        input_user = int(input("Digite o seu número: "))
        resultado = 10 / input_user
        print(f"O resultado deu: {resultado}")
        break # PODEMOS UTILZIAR O BREAK EM TRY/EXCEPT E  FINALLY
    except ZeroDivisionError:
        print("0 não pode ser divisivel")
    except ValueError:
        print("Não é um número válido")
    finally: # SEMPRE SERÁ EXECUTADO AO PASSAR O TRY E TODAS AS EXCEPTS
        print("Fim das tentativas")