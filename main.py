from flet import *
def router(page:Page):
    page.title = "Sorteio"
    alunos = ["maria","joao"]

    def fechar_banner(e):
        page.banner.open = False
        page.update()

    def excluirAluno(a):

        listExcluirAluno()

    lv = ListView(expand=1,spacing=10,item_extent=50)

    def listAlunos():
        lv.controls.clear()
        for i in range(len(alunos)):
            lv.controls.append(
                Container(
                    Text(f"{alunos[i]}"),
                    alignment=alignment.center,
                    bgcolor=colors.AMBER_100,
                    border=border.all(2, colors.AMBER_400),
                    padding=5,
                    margin=2
                )
            )

        page.update()



    def listExcluirAluno():
        lv.controls.clear()
        for i in range(len(alunos)):
            lv.controls.append(
                Container(
                    Text(alunos[i],color=colors.RED_400),
                    on_click=excluirAluno,
                    alignment=alignment.center,
                    bgcolor=colors.AMBER_100,
                    border=border.all(2, colors.AMBER_400),
                    padding=5,
                    margin=2,
                )
            )

        page.update()

    bannervazio = Banner(
        bgcolor=colors.AMBER_100,
        leading=Icon(icons.DANGEROUS_SHARP, color=colors.RED_400, size=40),
        content=Text(
            "O Campo abaixo deve ser preenchido"
        ),
        actions=[
            TextButton("OK", on_click=fechar_banner),
        ],
    )

    bannerjaexistente = Banner(
        bgcolor=colors.AMBER_100,
        leading=Icon(icons.DANGEROUS_SHARP, color=colors.RED_400, size=40),
        content=Text(
            "Nome já existente"
        ),
        actions=[
            TextButton("OK", on_click=fechar_banner),
        ],
    )

    bannerfinalizado = Banner(
        bgcolor=colors.GREEN_400,
        leading=Icon(icons.DANGEROUS_SHARP, color=colors.RED_400, size=40),
        content=Text(
            "Nome Adicionado"
        ),
        actions=[
            TextButton("OK", on_click=fechar_banner),
        ],
    )

    name = TextField(label="Nome", autofocus=True)
    def validacaoNome(name):
        for n in alunos:
            if n.__eq__(name):
                page.banner = bannerjaexistente
                page.banner.open = True
                page.update()
                break
        else:
            if not name:
                page.banner = bannervazio
                page.banner.open = True
                page.update()
            else:
                alunos.append(name)
                page.banner = bannerfinalizado
                page.banner.open = True
                page.update()

    def cadastrar(e):
        validacaoNome(name.value)
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
                            ElevatedButton(text="Listar Alunos", color=colors.ORANGE_500,
                                           on_click=lambda _: page.go("/listAluno")),
                            ElevatedButton(text="Remover Aluno", color=colors.ORANGE_500,
                                           on_click= lambda _:page.go("/deleteAluno")),
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
                            controls = [
                                name,
                                ElevatedButton("Adicionar Aluno",on_click=cadastrar)
                            ],
                            alignment=MainAxisAlignment.CENTER,
                        ),

                    ]
                )
            )
        elif page.route == "/listAluno":
            listAlunos()
            page.views.append(
                View(
                    "/listAluno",
                    [

                        AppBar(
                            leading_width=40,
                            title=Text("Lista de Alunos", color=colors.WHITE),
                            center_title=True,
                            bgcolor=colors.BLUE_400),
                        lv
                    ]
                )
            )
        elif page.route == "/deleteAluno":
            listExcluirAluno()
            page.views.append(
                View(
                    "/deleteAluno",
                    [
                        AppBar(
                            leading_width=40,
                            title=Text("Remover Aluno", color=colors.WHITE),
                            center_title=True,
                            bgcolor=colors.BLUE_400),

                        lv
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
