class Calculadora:
    def somar(num1, num2):
        return int(num1) + int(num2)
    
    def maiorNumero(num1, num2):
        if num1 == num2:
            return 'Os dois números são iguais'
        if num1 > num2:
            return f'O maior número é {num1}'
        else:
            return f'O maior número é {num2}'
        
    def diferenca(numero1, numero2):
        return abs(int(numero1) - int(numero2))
