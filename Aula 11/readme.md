# 🏦 Simulador de Caixa Eletrônico - Documentação

## 📁 Estrutura do Projeto

O projeto é composto por duas classes principais:

- `ContaBancaria`: representa uma conta de banco.
- `CaixaEletronico`: gerencia o menu e as operações entre contas.

---

## 📘 Classe `ContaBancaria`

```python
class ContaBancaria:
```

### 🔐 Atributos privados:

- `__numero`: número da conta bancária.
- `__titular`: nome do titular da conta.
- `__saldo`: saldo disponível na conta.

### ✅ Métodos:

- `depositar(valor)`  
  Adiciona um valor ao saldo, se for positivo.

- `sacar(valor)`  
  Subtrai um valor do saldo, se for suficiente.

- `transferir(destino, valor)`  
  Transfere um valor para outra conta bancária, desde que haja saldo suficiente.

- `exibir_saldo()`  
  Mostra o saldo atual da conta.

- `@property titular`  
  Retorna o nome do titular.

- `@property numero`  
  Retorna o número da conta.

---

## 🏧 Classe `CaixaEletronico`

```python
class CaixaEletronico:
```

### 🔐 Atributos:

- `contas`: dicionário que armazena objetos `ContaBancaria`, indexados pelo número da conta.

### ✅ Métodos:

- `criar_conta(numero, titular)`  
  Cria uma nova conta bancária, se o número ainda não existir.

- `acessar_conta(numero)`  
  Retorna o objeto da conta correspondente ao número informado, ou `None` se não existir.

- `menu()`  
  Exibe o menu principal:

  1. Criar nova conta
  2. Acessar conta existente
  3. Sair

- `menu_conta(conta)`  
  Exibe o menu de operações para uma conta acessada:
  1. Ver saldo
  2. Depositar
  3. Sacar
  4. Transferir
  5. Voltar ao menu principal

---

## ▶️ Execução do Programa

```python
if __name__ == "__main__":
    caixa = CaixaEletronico()
    caixa.menu()
```

Este trecho executa o menu principal ao rodar o script, criando uma instância da classe `CaixaEletronico`.

---

## 🛡️ Validações Implementadas

- Não é possível depositar ou sacar valores negativos.
- O saque e a transferência só são feitos se houver saldo suficiente.
- Contas só podem ser criadas se o número ainda não existir.
