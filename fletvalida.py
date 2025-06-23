import flet as ft
from datetime import datetime


def main(page: ft.Page):
    page.title = "Zim Hamburgueria"
    page.bgcolor = ft.colors.GREY_200
    page.scroll = ft.ScrollMode.AUTO

    carrinho = []

    nome = ft.TextField(label="Seu nome")
    endereco = ft.TextField(label="Endereço")
    telefone = ft.TextField(label="Telefone", keyboard_type=ft.KeyboardType.NUMBER)

    itens = ft.Text("")
    total_txt = ft.Text("Total: R$ 0.00", weight="bold")

    def verificar_horario():
        hora = datetime.now().hour
        return 17 <= hora < 23

    def atualizar_carrinho():
        itens.value = "\n".join(
            [f"{p['nome']} x{p['qtd']} - R$ {p['preco']*p['qtd']:.2f}" for p in carrinho]
        )
        total = sum([p["preco"] * p["qtd"] for p in carrinho])
        total_txt.value = f"Total: R$ {total:.2f}"
        page.update()

    def adicionar_produto(produto, preco):
        for item in carrinho:
            if item["nome"] == produto:
                item["qtd"] += 1
                break
        else:
            carrinho.append({"nome": produto, "preco": preco, "qtd": 1})
        atualizar_carrinho()

    def remover_produto(produto):
        for item in carrinho:
            if item["nome"] == produto:
                if item["qtd"] > 1:
                    item["qtd"] -= 1
                else:
                    carrinho.remove(item)
                break
        atualizar_carrinho()

    def finalizar_pedido(e):
        if not verificar_horario():
            page.dialog = ft.AlertDialog(
                title=ft.Text("Loja fechada!"),
                content=ft.Text("Desculpe, a hamburgueria está fechada."),
            )
            page.dialog.open = True
            page.update()
            return

        if len(carrinho) == 0:
            page.dialog = ft.AlertDialog(
                title=ft.Text("Carrinho vazio"),
                content=ft.Text("Adicione produtos antes de finalizar."),
            )
            page.dialog.open = True
            page.update()
            return

        if nome.value.strip() == "" or len(nome.value) < 3:
            page.snack_bar = ft.SnackBar(
                ft.Text("Por favor, preencha seu nome corretamente!")
            )
            page.snack_bar.open = True
            page.update()
            return

        if endereco.value.strip() == "" or len(endereco.value) < 3:
            page.snack_bar = ft.SnackBar(
                ft.Text("Por favor, preencha seu endereço completo!")
            )
            page.snack_bar.open = True
            page.update()
            return

        if telefone.value.strip() == "" or len(telefone.value) != 11:
            page.snack_bar = ft.SnackBar(
                ft.Text("Telefone deve ter 11 dígitos. Ex.: 31999990000")
            )
            page.snack_bar.open = True
            page.update()
            return

        # Simular envio para WhatsApp
        pedido = "\n".join(
            [
                f"{p['nome']} - Qtd: {p['qtd']} - R$ {p['preco']*p['qtd']:.2f}"
                for p in carrinho
            ]
        )
        total = sum([p["preco"] * p["qtd"] for p in carrinho])

        mensagem = (
            f"Pedido:\n{pedido}\n\nTotal: R$ {total:.2f}\n"
            f"Nome: {nome.value}\nEndereço: {endereco.value}\nTelefone: {telefone.value}"
        )

        page.dialog = ft.AlertDialog(
            title=ft.Text("Pedido Finalizado"),
            content=ft.Text(f"Pedido enviado com sucesso!\n\n{mensagem}"),
        )
        page.dialog.open = True
        page.update()

        carrinho.clear()
        atualizar_carrinho()

    # ---------------------------- UI ----------------------------

    produtos = [
        ("Hamburguer Gourmet", 39.99),
        ("Hamburguer Horto", 39.99),
        ("Hamburguer Cheddar", 44.99),
        ("Hamburguer Crispy", 59.99),
        ("Porção Batatas", 59.99),
        ("Batatas Fritas", 34.99),
        ("Coca Zero 2L", 15.99),
        ("Coca 2L", 15.99),
        ("Guaraná Zero 2L", 11.99),
        ("Guaraná 2L", 11.99),
        ("Guaraná Lata 350ml", 8.99),
        ("Coca Lata 350ml", 8.99),
    ]

    cards = []
    for nome_produto, preco in produtos:
        cards.append(
            ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(nome_produto, size=16, weight="bold"),
                            ft.Text(f"R$ {preco:.2f}"),
                            ft.Row(
                                [
                                    ft.ElevatedButton(
                                        "Adicionar",
                                        on_click=lambda e, p=nome_produto, pr=preco: adicionar_produto(
                                            p, pr
                                        ),
                                    ),
                                    ft.ElevatedButton(
                                        "Remover",
                                        on_click=lambda e, p=nome_produto: remover_produto(
                                            p
                                        ),
                                        style=ft.ButtonStyle(
                                            bgcolor=ft.colors.RED_ACCENT
                                        ),
                                    ),
                                ]
                            ),
                        ]
                    ),
                    padding=10,
                    width=200,
                )
            )
        )

    page.add(
        ft.Column(
            [
                ft.Text("Zim Hamburgueria", size=30, weight="bold"),
                ft.Divider(),
                ft.Text("Cardápio", size=24, weight="bold"),
                ft.Wrap(cards, spacing=20, run_spacing=20),
                ft.Divider(),
                ft.Text("Carrinho", size=24, weight="bold"),
                itens,
                total_txt,
                ft.Row([nome, endereco, telefone]),
                ft.Row(
                    [
                        ft.ElevatedButton(
                            "Finalizar Pedido", on_click=finalizar_pedido
                        ),
                    ]
                ),
            ],
            scroll=ft.ScrollMode.AUTO,
        )
    )


ft.app(target=main)
