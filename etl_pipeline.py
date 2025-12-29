"""
Pipeline ETL - Mensagens de Marketing Personalizadas
Projeto: Santander Bootcamp Ciência de Dados
"""

import json
from datetime import datetime

# ==================== EXTRACT ====================
print("=" * 50)
print("ETAPA 1: EXTRACT (Extração de Dados)")
print("=" * 50)

# Simulando dados de clientes (substitui a leitura da API)
clientes = [
    {
        'id': 1,
        'nome': 'Ana Silva',
        'conta': '12345-6',
        'saldo': 1500.00,
        'news': []
    },
    {
        'id': 2,
        'nome': 'Carlos Santos',
        'conta': '23456-7',
        'saldo': 3200.00,
        'news': []
    },
    {
        'id': 3,
        'nome': 'Mariana Costa',
        'conta': '34567-8',
        'saldo': 850.00,
        'news': []
    },
    {
        'id': 4,
        'nome': 'Pedro Oliveira',
        'conta': '45678-9',
        'saldo': 5000.00,
        'news': []
    }
]

print(f"\n✅ {len(clientes)} clientes extraídos com sucesso!")
for cliente in clientes:
    print(f"   - {cliente['nome']} (Conta: {cliente['conta']})")

# ==================== TRANSFORM ====================
print("\n" + "=" * 50)
print("ETAPA 2: TRANSFORM (Transformação com IA)")
print("=" * 50)

def gerar_mensagem_personalizada(cliente):
    """
    Simula a geração de mensagem personalizada por IA
    Na vida real, aqui você chamaria a API do ChatGPT/Claude
    """
    nome = cliente['nome'].split()[0]  # Pega só o primeiro nome
    saldo = cliente['saldo']
    
    # Lógica simples de personalização baseada no saldo
    if saldo < 1000:
        mensagem = f"{nome}, investir é o primeiro passo para multiplicar seu patrimônio. Comece hoje!"
    elif saldo < 3000:
        mensagem = f"{nome}, seu perfil está pronto para investimentos. Que tal diversificar sua carteira?"
    else:
        mensagem = f"{nome}, invista de forma inteligente e faça seu dinheiro trabalhar por você!"
    
    return mensagem

# Gerando mensagens para cada cliente
print("\n🤖 Gerando mensagens personalizadas...\n")

for cliente in clientes:
    mensagem = gerar_mensagem_personalizada(cliente)
    
    # Adiciona a mensagem na lista de news do cliente
    cliente['news'].append({
        'icone': '💰',
        'descricao': mensagem,
        'data': datetime.now().strftime('%d/%m/%Y %H:%M')
    })
    
    print(f"✉️  {cliente['nome']}:")
    print(f"   {mensagem}\n")

# ==================== LOAD ====================
print("=" * 50)
print("ETAPA 3: LOAD (Carregamento dos Dados)")
print("=" * 50)

# Salvando em arquivo JSON (substitui o PUT na API)
nome_arquivo = 'clientes_atualizados.json'

try:
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(clientes, arquivo, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Dados salvos com sucesso em '{nome_arquivo}'!")
    print(f"   Total de clientes atualizados: {len(clientes)}")
    print(f"   Total de mensagens geradas: {sum(len(c['news']) for c in clientes)}")
    
except Exception as erro:
    print(f"\n❌ Erro ao salvar arquivo: {erro}")

# ==================== RESUMO ====================
print("\n" + "=" * 50)
print("RESUMO DO PIPELINE ETL")
print("=" * 50)
print("""
✅ EXTRACT:  Dados dos clientes carregados
✅ TRANSFORM: Mensagens personalizadas geradas
✅ LOAD:      Dados salvos em arquivo JSON

Pipeline executado com sucesso! 🎉
""")

# Exibindo uma amostra do resultado final
print("📄 Amostra do arquivo gerado:\n")
print(json.dumps(clientes[0], indent=2, ensure_ascii=False))
