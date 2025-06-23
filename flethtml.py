import flet as ft


def main(page: ft.Page):
    page.title = "Zim Hamburgueria"
    page.bgcolor = ft.colors.GREY_200
    page.scroll = ft.ScrollMode.AUTO

    carrinho = []

    def adicionar_ao_carrinho(e):
        produto = e.control.data["produto"]
        preco = e.control.data["preco"]
        carrinho.append((produto, preco))
        atualizar_carrinho()

    def atualizar_carrinho():
        itens.value = "\n".join([f"{p} - R$ {preco}" for p, preco in carrinho])
        total = sum([preco for _, preco in carrinho])
        total_txt.value = f"Total: R$ {total:.2f}"
        page.update()

    def limpar_carrinho(e):
        carrinho.clear()
        atualizar_carrinho()

    produtos = [
        {"nome": "Hamburguer Gourmet", "preco": 39.99, "img": "hamburguer1.webp"},
        {"nome": "Hamburguer Horto", "preco": 39.99, "img": "hamburguer1.webp"},
        {"nome": "Hamburguer Cheddar", "preco": 44.99, "img": "hamburguer3.jpeg"},
        {"nome": "Hamburguer Crispy", "preco": 59.99, "img": "2xhamburguer.jpg"},
        {"nome": "Porção Batatas", "preco": 59.99, "img": "porçãobatatasfritas.webp"},
        {"nome": "Batatas Fritas", "preco": 34.99, "img": "batatasfritas.webp"},
        {"nome": "Coca Zero 2L", "preco": 15.99, "img": "coca2lzero.webp"},
        {"nome": "Coca 2L", "preco": 15.99, "img": "coca2l.jpg"},
        {"nome": "Guaraná Zero 2L", "preco": 11.99, "img": "guarana2lzero.jpeg"},
        {"nome": "Guaraná 2L", "preco": 11.99, "img": "guarana2l.png"},
        {"nome": "Guaraná Lata 350ml", "preco": 8.99, "img": "guarana350.jpeg"},
        {"nome": "Coca Lata 350ml", "preco": 8.99, "img": "coca350ml_800x.webp"},
    ]

    lista_produtos = []

    for p in produtos:
        lista_produtos.append(
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Image(src=f"/static/{p['img']}", width=150, height=150),
                        ft.Text(p["nome"], weight="bold", size=16),
                        ft.Text(f"R$ {p['preco']:.2f}"),
                        ft.ElevatedButton(
                            "Adicionar ao Carrinho",
                            data={"produto": p["nome"], "preco": p["preco"]},
                            on_click=adicionar_ao_carrinho
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER),
                    padding=10,
                    width=200,
                )
            )
        )

    itens = ft.Text("")
    total_txt = ft.Text("Total: R$ 0.00", weight="bold", size=16)

    page.add(
        ft.Column([
            ft.Text("Zim Hamburgueria", size=30, weight="bold"),
            ft.Text("Rua Trinta e Sete, 81 - São Luiz, BH", size=16),
            ft.Divider(),
            ft.Text("Cardápio", size=24, weight="bold"),
            ft.Wrap(lista_produtos, spacing=20, run_spacing=20),
            ft.Divider(),
            ft.Text("Carrinho", size=24, weight="bold"),
            itens,
            total_txt,
            ft.Row([
                ft.ElevatedButton("Limpar Carrinho", on_click=limpar_carrinho),
                ft.ElevatedButton("Finalizar Pedido")
            ]),
        ],
        scroll=ft.ScrollMode.AUTO)
    )


ft.app(target=main)
