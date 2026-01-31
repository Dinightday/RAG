from langchain_core.documents import Document

def documento():
    docs = [
        Document(
            page_content="""A cobertura para o procedimento de Implante de Cardiodifusor (ICD-99) 
            é obrigatória para todos os planos da categoria 'Ouro'. 
            O prazo de carência estipulado para novos beneficiários é de 180 dias. 
            O reembolso é limitado ao teto de R$ 12.000,00.""",
            metadata={
                "Id": "001",
                "Categoria": "Regulamentação Geral",
                "Data": "15/05/2015"          
            }
        ),
        Document(
            page_content="""Fica estabelecido que, a partir desta data, o procedimento ICD-99 
            (Implante de Cardiodifusor) passa a exigir autorização prévia da junta médica. 
            O teto de reembolso foi reajustado para R$ 15.000,00, mantendo-se as carências 
            do documento de 2023.""",
            metadata={
                "Id": "002",
                "Categoria": "Aditivo Contratual",
                "Data": "10/11/2024"
            }
        ),
        Document(
            page_content="""Nova diretiva: Para casos classificados como 'Emergência Nível 1', 
            o procedimento ICD-99 deve ter carência zerada, independentemente do contrato original. 
            O teto de reembolso para estes casos específicos de emergência sobe para R$ 22.000,00. 
            Esta norma sobrepõe-se a qualquer manual de 2023 ou 2024.""",
            metadata={
                "Id": "003",
                "Categoria": "Urgência e Emergência",
                "Data": "20/01/2025"
            }
        ),
        Document(
            page_content="""Tabela de Referência de Custos Adicionais: 
            Procedimento ICD-99 - Custo Operacional: R$ 5.000,00; 
            Taxa de Internação: R$ 2.500,00.""",
            metadata={
                "Id": "004",
                "Categoria": "Auditoria",
                "Data": "22/01/2025"
            }
        )
    ]
    return docs