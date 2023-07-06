from flet import *
def router(page:Page):
    page.title = Text("Home")
    alunos = ["maria"]

    def cadastrar():
        name =TextField.key("teste")
        alunos.append(name)
        print(alunos)


    def mudancaderotas(route):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(
                        leading_width=40,
                        title=Text("Sorteio CDD", color=colors.WHITE),
                        center_title=True,
                        bgcolor=colors.BLUE_400),
                    Row(
                        [
                            ElevatedButton(text="Adicionar Aluno", color=colors.ORANGE_500,
                                           on_click=lambda _: page.go("/addaluno")),
                            ElevatedButton(text="Remover Aluno", color=colors.ORANGE_500),
                            ElevatedButton(text="Listar Alunos", color=colors.ORANGE_500),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                    Row(
                        [
                            Image(
                                src=f"image/cddv.png",
                                width=300,
                                height=400,
                                border_radius=50,
                                fit=ImageFit.CONTAIN,
                            )
                        ],
                        alignment=MainAxisAlignment.CENTER
                    ),
                    Row(
                        [
                            ElevatedButton(text="Sorteio", color=colors.WHITE, bgcolor=colors.ORANGE_500, width=200,
                                           height=35)
                        ],
                        alignment=MainAxisAlignment.CENTER
                    )
                ]
            )
        )
        if page.route == "/addaluno":
            page.views.append(
                View(
                    "/addaluno",
                    [
                        AppBar(
                            leading_width=40,
                            title=Text("Cadastro", color=colors.WHITE),
                            center_title=True,
                            bgcolor=colors.BLUE_400),
                        Row(
                            [
                                TextField(label="Nome",key="teste"),
                                ElevatedButton("Adicionar Aluno",on_click=cadastrar())
                            ],
                            alignment=MainAxisAlignment.CENTER,
                        ),



                    ]
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = mudancaderotas
    page.on_view_pop = view_pop
    page.go(page.route)

app(target=router)
